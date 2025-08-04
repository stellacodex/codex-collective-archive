## 🧩 Kairoscope Chart Builder Structure

Kairoscopeの `chart_builder.py` は、Human Design チャートの中心的ロジックを統合管理するモジュールです。本構成では、HDの惑星計算・チャネル接続・プロファイル生成・Variables（PHS含む）を含むチャート全体を組み立てます。

---

### 📌 モジュール構成一覧（最新版）

#### 1. `astro/astro_position.py`：黄経取得
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

#### 2. `gate_mapper.py`：黄経→ゲート変換
```python
def longitude_to_gate_line(longitude):
    longitude = longitude % 360
    gate_size = 360 / 64
    line_size = gate_size / 6
    gate_number = int(longitude / gate_size) + 1
    within_gate_deg = longitude % gate_size
    line_number = int(within_gate_deg / line_size) + 1
    return gate_number, line_number

def get_gate_and_line(ecliptic_longitude):
    gate, line = longitude_to_gate_line(ecliptic_longitude)
    return {"gate": gate, "line": line}
```

#### 3. `channel_center.py`：チャネル＆センター接続
```python
def get_active_channels_and_centers(gates, channel_defs):
    active_gate_nums = {g["gate"] for g in gates.values()}
    active_channels = []
    defined_centers = set()

    for ch in channel_defs:
        gate_a, gate_b = [int(g) for g in ch["gates"]]
        if gate_a in active_gate_nums and gate_b in active_gate_nums:
            active_channels.append(ch["channel"])
            defined_centers.update(ch["centers"])

    return active_channels, list(defined_centers)
```

#### 4. `profile_logic.py`：プロファイル導出
```python
def calculate_profile(planet_gates):
    sun = planet_gates.get("Sun", {})
    earth = planet_gates.get("Earth", {})
    personality_line = sun.get("line")
    design_line = earth.get("line")

    if personality_line and design_line:
        return f"{personality_line}/{design_line}"
    return "Unknown"
```

#### 5. `authority_logic.py`：内的権威ロジック
```python
def determine_authority(gates, defined_centers):
    if "Solar Plexus" in defined_centers:
        return "Emotional"
    elif "Sacral" in defined_centers:
        return "Sacral"
    elif "Spleen" in defined_centers:
        return "Splenic"
    elif "Ego" in defined_centers:
        return "Ego Projected"
    elif "G" in defined_centers:
        return "Self Projected"
    else:
        return "Unknown"
```

#### 6. `variable_logic.py`（統合済）
```python
def calculate_variables(birth_data):
    hour = int(birth_data["time"].split(":")[0])
    variables = {
        "Digestion": "Consecutive" if hour < 6 else "Alternating",
        "Environment": "Markets" if hour < 12 else "Kitchens",
        "Perspective": "Observer" if hour < 18 else "Observed",
        "Motivation": "Hope" if hour % 2 == 0 else "Fear",
        "Variable": "PLL-DRR"
    }
    return variables
```

---

### 🧪 chart_builder.py（統合本体）
```python
from core.astro.astro_position import get_planet_positions
from core.gate_mapper import get_gate_and_line
from core.channel_center import get_active_channels_and_centers
from core.profile_logic import calculate_profile
from core.authority_logic import determine_authority
from core.definitions.loader import load_gate_definitions, load_channel_definitions

from core.variable_logic import calculate_variables

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
    variables = calculate_variables(birth_data)

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

### 🧪テストコマンド
```bash
cd chronogram-kairoscope
PYTHONPATH=. python3 core/chart_builder.py
```

---

### 🔮 次ステップ予定
- `samples/sample_chart_full.json`：1ユーザー分の全情報
- `samples/sample_chart_variants.json`：出生時間が曖昧な場合の複数候補（time sweep）
- `samples/sample_structure_schema.json`：Chronogram側との接続定義

---

この構成で Kairoscope チャート構造は実行可能になっており、今後は **MBTIとの相関分析・AI対話型チャートナビゲーション** への展開が可能になります。
