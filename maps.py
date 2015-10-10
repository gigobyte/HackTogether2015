import webbrowser
from get_location import loc
from pygeocoder import Geocoder
from dictionary import (adb_commands, commands)

location = loc()


def show_hotels():
	hotels = webbrowser.open('https://www.google.bg/maps/search/hotels+in+' + location, new = 1,autoraise = True)
	return hotels

def show_restaurants():
	rastaurants = webbrowser.open('https://www.google.bg/maps/search/restaurants+in+' + location, new = 1,autoraise = True)
	return restaurants

def show_bars():
	bars = webbrowser.open('https://www.google.bg/maps/search/bars+in+' + location, new = 1,autoraise = True)
	return bars

def show_coffees():
	coffees = webbrowser.open('https://www.google.bg/maps/search/coffee+in+' + location, new = 1,autoraise = True)
	return coffees

show_bars()