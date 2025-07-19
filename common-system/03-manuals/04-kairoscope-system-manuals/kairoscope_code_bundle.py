## 🧬 Kairoscope Code Bundle

このCanvasは、Kairoscopeの全機能に関わる**コアファイルのコード全文**を保存・一元管理するための統合リファレンスです。
各ファイルは、Kairoscopeプロジェクトの核として直接機能し、Chronogramなどのシステムとも連携可能な構造になっています。

---

### 📁 `/core/chart_builder.py`
```python
from core.astro.astro_position import get_planet_positions
from core.gate_mapper import get_gate_and_line
from core.channel_center import get_active_channels_and_centers
from core.profile_logic import calculate_profile
from core.authority_logic import determine_authority
from core.definitions.loader import load_gate_definitions, load_channel_definitions
from core.variable_logic import extract_phs_variables
from core.mbti_templates import suggest_mbti_structure


def build_chart(birth_data):
    positions = get_planet_positions(birth_data, include_design=True)

    personality_pos = positions["Personality"]
    personality_pos["Earth"] = (personality_pos["Sun"] + 180) % 360
    design_pos = positions["Design"]
    design_pos["Earth"] = (design_pos["Sun"] + 180) % 360

    raw_gates = {planet: get_gate_and_line(deg) for planet, deg in personality_pos.items()}

    gate_defs = load_gate_definitions()
    channel_defs = load_channel_definitions()
    gate_dict = {g["gate"]: g for g in gate_defs}
    channel_dict = {c["channel"]: c for c in channel_defs}

    gates = {
        planet: {
            "gate": g["gate"],
            "line": g["line"],
            **gate_dict.get(g["gate"], {})
        }
        for planet, g in raw_gates.items()
    }

    active_channels, defined_centers = get_active_channels_and_centers(raw_gates, channel_defs)
    enriched_channels = [channel_dict[c] for c in active_channels if c in channel_dict]

    profile = calculate_profile(raw_gates)
    authority = determine_authority(raw_gates, defined_centers)
    variables = extract_phs_variables(personality_pos, design_pos)

    mbti_suggestion = suggest_mbti_structure(profile, variables.get("Variable", ""), authority)

    return {
        "planet_positions": personality_pos,
        "gates": gates,
        "active_channels": enriched_channels,
        "defined_centers": defined_centers,
        "profile": profile,
        "authority": authority,
        "variables": variables,
        "mbti_suggestion": mbti_suggestion
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

### 📁 `/core/variable_logic.py`
```python
from core.gate_mapper import get_gate_and_line

def extract_phs_variables(personality_pos, design_pos):
    personality_sun = get_gate_and_line(personality_pos["Sun"])
    personality_earth = get_gate_and_line(personality_pos["Earth"])
    design_sun = get_gate_and_line(design_pos["Sun"])
    design_earth = get_gate_and_line(design_pos["Earth"])

    variables = {
        "Digestion": f"Gate {design_sun['gate']} Line {design_sun['line']}",
        "Environment": f"Gate {design_earth['gate']} Line {design_earth['line']}",
        "Perspective": f"Gate {personality_sun['gate']} Line {personality_sun['line']}",
        "Motivation": f"Gate {personality_earth['gate']} Line {personality_earth['line']}",
        "Variable": derive_variable_type(design_sun, design_earth, personality_sun, personality_earth)
    }
    return variables

def derive_variable_type(design_sun, design_earth, personality_sun, personality_earth):
    def polarity(gate):
        return "L" if gate % 2 == 0 else "R"

    brain = polarity(design_sun["gate"])
    mind = polarity(design_earth["gate"])
    body = polarity(personality_sun["gate"])
    awareness = polarity(personality_earth["gate"])

    return f"{brain}{mind}{body}{awareness}"
```

---

### 📁 `/core/gate_mapper.py`
```python
def get_gate_and_line(degree):
    gate_width = 5.625
    line_width = gate_width / 6

    gate_number = int(degree // gate_width) + 1
    line_number = int((degree % gate_width) // line_width) + 1

    return {"gate": gate_number, "line": line_number}
```

---

### 📁 `/core/astro/astro_position.py`
```python
from skyfield.api import load, Topos
from datetime import datetime, timedelta
from pytz import timezone

planet_names = {
    "Sun": "sun",
    "Moon": "moon",
    "Mercury": "mercury",
    "Venus": "venus",
    "Mars": "mars",
    "Jupiter": "jupiter",
    "Saturn": "saturn",
    "Uranus": "uranus",
    "Neptune": "neptune",
    "Pluto": "pluto",
    "North Node": "mean_node"
}

def get_planet_positions(birth_data, include_design=False):
    ts = load.timescale()
    birth_dt = datetime.strptime(f"{birth_data['date']} {birth_data['time']}", "%Y-%m-%d %H:%M")
    tz = timezone("Asia/Tokyo")
    birth_dt_local = tz.localize(birth_dt)
    birth_time = ts.from_datetime(birth_dt_local)

    planets = load("de421.bsp")
    earth = planets["earth"]
    observer = earth + Topos(latitude_degrees=40.822072, longitude_degrees=140.747364)
    chart_time = observer.at(birth_time)

    personality_positions = {
        name: chart_time.observe(planets[planet_code]).apparent().ecliptic_latlon()[1].degrees % 360
        for name, planet_code in planet_names.items()
    }

    if not include_design:
        return {"Personality": personality_positions}

    design_time = ts.from_datetime(birth_dt_local - timedelta(days=88))
    chart_time_design = observer.at(design_time)

    design_positions = {
        name: chart_time_design.observe(planets[planet_code]).apparent().ecliptic_latlon()[1].degrees % 360
        for name, planet_code in planet_names.items()
    }

    return {
        "Personality": personality_positions,
        "Design": design_positions
    }
```

---

### 📁 `/core/authority_logic.py`
```python
def determine_authority(raw_gates, defined_centers):
    if "Solar Plexus" in defined_centers:
        return "Emotional"
    elif "Sacral" in defined_centers:
        return "Sacral"
    elif "Spleen" in defined_centers:
        return "Splenic"
    elif "Heart" in defined_centers:
        return "Ego"
    elif "Self" in defined_centers:
        return "Self-Projected"
    elif "None" in defined_centers:
        return "Mental"
    else:
        return "Lunar"
```

---

### 📁 `/core/mbti_templates.py`
```python
def suggest_mbti_structure(profile, variable, authority):
    # 簡易ロジックに基づいてMBTI構造を提案
    intro_extro = "I" if variable.startswith("R") else "E"
    judge_perceive = "J" if authority in ["Emotional", "Sacral"] else "P"

    profile_key = str(profile)
    if profile_key in ["1/3", "5/1"]:
        thinking_feeling = "T"
        sensing_intuition = "S"
    elif profile_key in ["4/6", "2/4"]:
        thinking_feeling = "F"
        sensing_intuition = "N"
    else:
        thinking_feeling = "F"
        sensing_intuition = "S"

    return f"{intro_extro}{sensing_intuition}{thinking_feeling}{judge_perceive}"
```

---

### 📁 `/core/mbti_builder.py`
```python
def build_mbti_profile(mbti_type):
    traits = {
        "I": "内向的",
        "E": "外向的",
        "N": "直観的",
        "S": "感覚的",
        "F": "感情的",
        "T": "論理的",
        "J": "計画的",
        "P": "柔軟的"
    }

    description = [traits[c] for c in mbti_type if c in traits]
    return {
        "type": mbti_type,
        "description": description
    }
```
