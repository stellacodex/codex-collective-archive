# /core/astro/astro_position.py

from skyfield.api import load, Topos
from datetime import datetime, timedelta
from pytz import timezone

def get_planet_positions(birth_data, include_design=False):
    ts = load.timescale()
    dt = datetime.strptime(f"{birth_data['date']} {birth_data['time']}", "%Y-%m-%d %H:%M")
    dt = timezone("Asia/Tokyo").localize(dt)
    t = ts.from_datetime(dt)
    t_design = ts.from_datetime(dt - timedelta(days=88))  # Design chart用

    planets = load('de421.bsp')
    earth = planets['earth']
    loc = earth + Topos(latitude_degrees=40.8246, longitude_degrees=140.7400)

    planet_names = [
        "Sun", "Moon", "Mercury", "Venus", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"
    ]  # ← Earthを除外！

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
        # EarthはSunの反対側
        positions["Earth"] = (positions["Sun"] + 180) % 360
        return positions

    if include_design:
        return {
            "Personality": calc_positions(t),
            "Design": calc_positions(t_design)
        }
    else:
        return calc_positions(t)
