import time
from datetime import datetime
import googlemaps
import requests

api_keys = {'google' : 'AIzaSyC6CsQc6B6nBvURAuqc53dLy8YVpgdXkOg' , 'timezonedb' : '7B2YJOH7HNP4'}

gmaps = googlemaps.Client(key = api_keys['google'])
fmt = '%Y.%m.%d %H : %M : %S'

def GetGeo():
    geo = gmaps.geocode('London')
    res = geo[0]
    return res

def GetLocation():
    res = GetGeo()
    return res['geometry']['location']

def req():
    geo = GetLocation()
    url = 'http://api.timezonedb.com/'
    query = {'key' : api_keys['timezonedb'], 'lat' : geo['lat'], 'lng' : geo['lng'], 'format' : 'json'}
    resp = requests.get(url, params = query)
    return resp.json()

def GetTime():
    local = req()
    time = local['timestamp'] + int(local['gmtOffset'])
    zone = datetime.utcfromtimestamp(time)
    now = datetime.now()
    dif = now - zone
    local = now + dif
    return local.strftime(fmt)

print GetTime()
