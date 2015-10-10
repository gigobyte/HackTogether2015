import time
from datetime import *
import googlemaps
import requests

api_keys = {'google' : 'AIzaSyC6CsQc6B6nBvURAuqc53dLy8YVpgdXkOg' , 'timezonedb' : '7B2YJOH7HNP4'}

gmaps = googlemaps.Client(key = api_keys['google'])

def req(city):
    geo = gmaps.geocode(city)
    geo = geo[0]['geometry']['location']
    url = 'http://api.timezonedb.com/'
    query = {'key' : api_keys['timezonedb'], 'lat' : geo['lat'], 'lng' : geo['lng'], 'format' : 'json'}
    resp = requests.get(url, params = query)
    return resp.json()

def GetTime(city):
    local = req(city)
    time = local['timestamp']
    zone = datetime.utcfromtimestamp(time)
    return zone

def Clock(city):
    t = GetTime(city)
    fmt = '%Y.%m.%d %H : %M : %S'
    second = 0
    while 1:
        local = datetime.now()
        l_sec = local.second
        if l_sec > second or l_sec == 0 and second == 59:
            second = l_sec
            t = t + timedelta(seconds = 1)
            print t.strftime(fmt)

Clock('Harare')
