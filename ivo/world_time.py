import time
from datetime import datetime
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
    time = local['timestamp'] + int(local['gmtOffset'])
    zone = datetime.utcfromtimestamp(time)
    now = datetime.now()
    dif = now - zone
    return dif

def Clock(city):
    dif = GetTime(city)
    fmt = '%Y.%m.%d %H : %M : %S'
    second = 0
    while 1:
        local = dif + datetime.utcnow()
        l_sec = local.second
        if l_sec > second or l_sec == 0 and second == 59:
            second = l_sec
            print local.strftime(fmt)

Clock('London')
