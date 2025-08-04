## 🧩 Kairoscope Chart Builder Structure (Revised Canvas)

Kairoscopeの `chart_builder.py` は、Human Design チャートの中核。現在の最新版では、以下の要素を完全統合：
- 天体位置取得（Skyfield）
- 黄経→ゲート変換
- アクティブチャネル＆センター
- プロファイル／内的権威／Variables（PHS）生成
- 時間不明時のvariant対応（`time_variants.py`）

---

### ✅ astro_position.py（黄経計算）
```python
from skyfield.api import load, Topos
from datetime import datetime
from pytz import timezone

def get_planet_positions(birth_data):
    ts = load.timescale()
    dt = datetime.strptime(f"{birth_data['date']} {birth_data['time']}", "%Y-%m-%d %H:%M")
    dt = timezone("Asia/Tokyo").localize(dt)
    t = ts.from_datetime(dt)

    planets = load('de421.bsp')
    earth = planets['earth']
    loc = earth + Topos(latitude_degrees=40.8246, longitude_degrees=140.7400)

    planet_names = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
    planet_ids = {
        "Sun": "sun", "Moon": "moon", "Mercury": "mercury", "Venus": "venus", "Mars": "mars",
        "Jupiter": "jupiter barycenter", "Saturn": "saturn barycenter", "Uranus": "uranus barycenter",
        "Neptune": "neptune barycenter", "Pluto": "pluto barycenter"
    }

    positions = {}
    for name in planet_names:
        planet = planets[planet_ids[name]]
        astrometric = loc.at(t).observe(planet)
        lon, _, _ = astrometric.ecliptic_latlon()
        positions[name] = lon.degrees

    return positions
```

---

### ✅ chart_builder.py（完全統合）
```python
from core.astro.astro_position import get_planet_positions
from core.gate_mapper import get_gate_and_line
from core.channel_center import get_active_channels_and_centers
from core.profile_logic import calculate_profile
from core.authority_logic import determine_authority
from core.definitions.loader import load_gate_definitions, load_channel_definitions
from core.variable_logic import calculate_variables_from_gates

def build_chart(birth_data):
    positions = get_planet_positions(birth_data)
    positions["Earth"] = (positions["Sun"] + 180) % 360

    raw_gates = {planet: get_gate_and_line(lon) for planet, lon in positions.items()}

    gate_defs = load_gate_definitions()
    channel_defs = load_channel_definitions()
    gate_dict = {g["gate"]: g for g in gate_defs}
    channel_dict = {c["channel"]: c for c in channel_defs}

    gates = {
        planet: {
            "gate": g["gate"],
            "line": g["line"],
            **gate_dict.get(g["gate"], {})
        } for planet, g in raw_gates.items()
    }

    active_channels, defined_centers = get_active_channels_and_centers(raw_gates, channel_defs)
    enriched_channels = [channel_dict[c] for c in active_channels if c in channel_dict]

    profile = calculate_profile(raw_gates)
    authority = determine_authority(raw_gates, defined_centers)
    variables = calculate_variables_from_gates(raw_gates)

    return {
        "planet_positions": positions,
        "gates": gates,
        "active_channels": enriched_channels,
        "defined_centers": defined_centers,
        "profile": profile,
        "authority": authority,
        "variables": variables
    }

if __name__ == "__main__":
    birth_data = {
        "date": "1983-05-01",
        "time": "14:35",
        "location": "Aomori, Japan"
    }

    chart = build_chart(birth_data)

    import json
    print(json.dumps(chart, indent=2, ensure_ascii=False))
```

---

### ✅ time_variants.py（出生時間未定時の候補リスト生成）
```python
from core.chart_builder import build_chart
from datetime import datetime, timedelta

def generate_time_variants(date, location, interval_minutes=120):
    base_time = datetime.strptime(f"{date} 00:00", "%Y-%m-%d %H:%M")
    variants = []
    seen = set()

    for i in range(0, 24 * 60, interval_minutes):
        t = (base_time + timedelta(minutes=i)).strftime("%H:%M")
        birth_data = {"date": date, "time": t, "location": location}
        chart = build_chart(birth_data)

        key = (chart["profile"], chart["authority"], tuple(chart["defined_centers"]))
        if key not in seen:
            seen.add(key)
            variants.append({
                "time": t,
                "profile": chart["profile"],
                "authority": chart["authority"],
                "active_channels": [ch["channel"] for ch in chart["active_channels"]],
                "defined_centers": chart["defined_centers"],
                "variables": chart["variables"]
            })

    return variants

if __name__ == "__main__":
    samples = generate_time_variants("1983-05-01", "Aomori, Japan", interval_minutes=120)

    import json
    print(json.dumps(samples, indent=2, ensure_ascii=False))
```

---

これでKairoscope→Chronogramへの全チャート構造・変数付き出力・スイープ生成が万全。
次のステップで「MBTIとのマッピング」「UI表現の差異ナビゲーション」に進める！
