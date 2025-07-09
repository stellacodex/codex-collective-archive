# astro.py
from skyfield.api import load, Topos
from datetime import datetime, timedelta
import pytz

def get_planet_positions(date_utc, latitude, longitude):
    ts = load.timescale()
    t = ts.utc(date_utc.year, date_utc.month, date_utc.day, date_utc.hour, date_utc.minute)
    planets = load('de421.bsp')
    observer = Topos(latitude_degrees=latitude, longitude_degrees=longitude)
    
    planet_list = ['sun', 'moon', 'mercury', 'venus', 'mars',
                   'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
    
    result = {}
    for name in planet_list:
        body = planets[name.capitalize()]
        astrometric = body.at(t).observe(observer).ecliptic_latlon()
        result[name] = round(astrometric[1].degrees, 2)

    return result

def get_design_date(birth_datetime_utc):
    return birth_datetime_utc - timedelta(days=88)
