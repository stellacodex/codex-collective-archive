# /core/astro/astro_position.py

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