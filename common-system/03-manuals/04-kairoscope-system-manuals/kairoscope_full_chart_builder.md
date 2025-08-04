## 🧩 Kairoscope Chart Builder Structure (Revised Canvas - コピペ対応版)

Kairoscopeの `chart_builder.py` は、Human Design チャートの中核。現在の最新版では、以下の要素を完全統合：

- 天体位置取得（Skyfield）
- 黄経→ゲート変換
- アクティブチャネル＆センター
- プロファイル／内的権威／Variables（PHS）生成
- MBTI連携テンプレートによる性格推定（2025-07-15 追加）
- 時間不明時のvariant対応（`time_variants.py`）
- 🔄 **Design Chart（88日前）の天体位置も算出・PHS用に導入済み**（← New）

---

### ✅ astro\_position.py

```python
from skyfield.api import load, Topos
from datetime import datetime, timedelta
from pytz import timezone

def get_planet_positions(birth_data):
    ts = load.timescale()
    dt = datetime.strptime(f"{birth_data['date']} {birth_data['time']}", "%Y-%m-%d %H:%M")
    dt = timezone("Asia/Tokyo").localize(dt)
    t = ts.from_datetime(dt)
    t_design = ts.from_datetime(dt - timedelta(days=88))  # Design chart用

    planets = load('de421.bsp')
    earth = planets['earth']
    loc = earth + Topos(latitude_degrees=40.8246, longitude_degrees=140.7400)

    planet_names = ["Sun", "Earth", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
    planet_ids = {
        "Sun": "sun", 
        "Moon": "moon", 
        "Mercury": "mercury", 
        "Venus": "venus", 
        "Mars": "mars",
        "Jupiter": "jupiter barycenter", 
        "Saturn": "saturn barycenter", 
        "Uranus": "uranus barycenter",
        "Neptune": "neptune barycenter", 
        "Pluto": "pluto barycenter"
    }

    def calc_positions(t):
        positions = {}
        for name in planet_names:
            planet = planets[planet_ids[name]]
            astrometric = loc.at(t).observe(planet)
            lon, _, _ = astrometric.ecliptic_latlon()
            positions[name] = lon.degrees
        positions["Earth"] = (positions["Sun"] + 180) % 360
        return positions

    positions = {
        "Personality": calc_positions(t),
        "Design": calc_positions(t_design)
    }
    return positions
```

---

※ `chart_builder.py` 側では：

```python
positions = get_planet_positions(birth_data)
personality = positions["Personality"]
design = positions["Design"]
```

これで Personality / Design 両方の惑星データにアクセス可能となり、PHS Variables の正式ロジック実装の基盤が整いました。

---

次は `variable_logic.py` の本格ロジック強化に進みます 🔬

