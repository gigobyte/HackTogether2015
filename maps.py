import webbrowser
import subprocess
from get_location import loc
from pygeocoder import Geocoder
from dictionary import (adb_commands, commands)
from adb import (run_command)


location = loc()


def show_hotels():
	hotels = webbrowser.open('https://www.google.bg/maps/search/hotel+' + location, new = 1,autoraise = True)
	return hotels

def show_restaurants():
	rastaurants = webbrowser.open('https://www.google.bg/maps/search/restaurant+' + location, new = 1,autoraise = True)
	return restaurants

def show_bars():
	bars = webbrowser.open('https://www.google.bg/maps/search/bar+' + location, new = 1,autoraise = True)
	return bars

def show_coffees():
	coffees = webbrowser.open('https://www.google.bg/maps/search/coffee+' + location, new = 1,autoraise = True)
	return coffees

#show_hotels()