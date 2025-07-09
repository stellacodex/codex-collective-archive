from skyfield.api import load, Topos
from datetime import datetime, timedelta
import pytz

# Skyfieldデータロード（グローバルキャッシュ用）
_planets = None

def load_planets():
    global _planets
    if _planets is None:
        _planets = load('de421.bsp')
    return _planets

def get_planet_positions(date_utc, latitude, longitude):
    ts = load.timescale()
    t = ts.utc(date_utc.year, date_utc.month, date_utc.day, date_utc.hour, date_utc.minute)
    planets = load_planets()
    observer = Topos(latitude_degrees=latitude, longitude_degrees=longitude)

    planet_list = ['sun', 'moon', 'mercury', 'venus', 'mars',
                   'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']

    result = {}
    for name in planet_list:
        body = planets[name.capitalize()]
        astrometric = body.at(t).observe(observer).ecliptic_latlon()
        result[name] = round(astrometric[1].degrees, 2)

    # Earthは太陽の黄経 + 180度で計算
    result['earth'] = (result['sun'] + 180) % 360

    # ノースノード・サウスノードは補完ロジックで計算
    result.update(get_lunar_nodes(ts, t))

    return result

def get_design_date(birth_datetime_utc):
    return birth_datetime_utc - timedelta(days=88)

def get_lunar_nodes(ts, t):
    # TODO: ノースノード・サウスノードを計算するロジックをここに実装する
    # 現状は仮の値（例として0度・180度）
    return {
        'north_node': 0.0,
        'south_node': 180.0
    }
