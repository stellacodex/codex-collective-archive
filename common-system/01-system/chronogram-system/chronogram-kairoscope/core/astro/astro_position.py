from skyfield.api import load, Topos
from datetime import datetime
from pytz import timezone

def get_planet_longitude(year, month, day, hour, minute, lat, lon, planet_name="Sun"):
    ts = load.timescale()
    time = ts.utc(year, month, day, hour, minute)
    planets = load('de421.bsp')
    observer = Topos(latitude_degrees=lat, longitude_degrees=lon)
    astro_position = planets[planet_name].at(time).observe(observer).ecliptic_latlon()
    return astro_position[1].degrees
