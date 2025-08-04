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
        "Sun": "sun",
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

    positions = {}
    for name in planet_names:
        target = planet_ids[name]
        planet = planets[target]
        astrometric = loc.at(t).observe(planet)
        lon, _, _ = astrometric.ecliptic_latlon()
        positions[name] = lon.degrees

    return positions
