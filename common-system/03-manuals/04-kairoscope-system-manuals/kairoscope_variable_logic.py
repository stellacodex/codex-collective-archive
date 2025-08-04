from skyfield.api import load, Topos
from datetime import datetime, timedelta
from pytz import timezone

def get_planet_positions(birth_data, include_design=False, design_offset_days=88):
    ts = load.timescale()
    dt = datetime.strptime(f"{birth_data['date']} {birth_data['time']}", "%Y-%m-%d %H:%M")
    dt = timezone("Asia/Tokyo").localize(dt)

    t_personality = ts.from_datetime(dt)
    t_design = ts.from_datetime(dt - timedelta(days=design_offset_days)) if include_design else None

    planets = load('de421.bsp')
    earth = planets['earth']
    loc = earth + Topos(latitude_degrees=40.8246, longitude_degrees=140.7400)  # TODO: location from birth_data

    planet_ids = {
        "Sun": "sun",
        "Earth": "earth",
        "Moon": "moon",
        "Mercury": "mercury",
        "Venus": "venus",
        "Mars": "mars",
        "Jupiter": "jupiter barycenter",
        "Saturn": "saturn barycenter",
        "Uranus": "uranus barycenter",
        "Neptune": "neptune barycenter",
        "Pluto": "pluto barycenter",
    }

    def observe_planets(time):
        pos = {}
        for name, target in planet_ids.items():
            body = planets[target]
            astrometric = loc.at(time).observe(body)
            lon, _, _ = astrometric.ecliptic_latlon()
            pos[name] = lon.degrees % 360
        return pos

    result = {
        "Personality": observe_planets(t_personality)
    }

    if include_design:
        result["Design"] = observe_planets(t_design)

    return result


def extract_phs_variables(personality, design):
    """
    Extracts core PHS variable categories from personality and design planet positions.
    - Digestion: Based on Design Sun
    - Environment: Based on Design Earth
    - Perspective: Based on Personality Sun
    - Motivation: Based on Personality Earth
    """
    def gate_from_longitude(lon):
        gate_width = 360 / 64
        gate = int(lon // gate_width) + 1
        return min(gate, 64)

    design_sun_gate = gate_from_longitude(design.get("Sun", 0))
    design_earth_gate = gate_from_longitude(design.get("Earth", 0))
    personality_sun_gate = gate_from_longitude(personality.get("Sun", 0))
    personality_earth_gate = gate_from_longitude(personality.get("Earth", 0))

    # Digestion
    digestion = "Alternating" if design_sun_gate % 2 == 0 else "Consecutive"

    # Environment
    environment = "Markets" if design_earth_gate < 33 else "Kitchens"

    # Perspective
    perspective = "Observer" if personality_sun_gate < 16 else "Observed"

    # Motivation
    if personality_earth_gate in [1, 2, 3, 4, 5, 6]:
        motivation = "Hope"
    else:
        motivation = "Fear"

    variable_code = f"{digestion[0]}L-{perspective[0]}R"

    return {
        "Digestion": digestion,
        "Environment": environment,
        "Perspective": perspective,
        "Motivation": motivation,
        "Variable": variable_code
    }


if __name__ == "__main__":
    birth_data = {
        "date": "1983-05-01",
        "time": "14:35",
        "location": "Aomori, Japan"
    }
    positions = get_planet_positions(birth_data, include_design=True)

    variables = extract_phs_variables(
        personality=positions["Personality"],
        design=positions["Design"]
    )

    import json
    print(json.dumps(variables, indent=2, ensure_ascii=False))
