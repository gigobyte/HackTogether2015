import webbrowser
import subprocess
from geolocation.google_maps import GoogleMaps
from dictionary import (adb_commands, commands)
from adb import (run_command)

# def get_location():
# 	google_maps = GoogleMaps(api_key = 'AIzaSyC6CsQc6B6nBvURAuqc53dLy8YVpgdXkOg')
# 	address = ""
# 	location = google_maps.search(location=address)
# 	my_location = location.first()
# 	print my_location
# 	print(my_location.route)
# 	print(my_location.street_number)
# 	print(my_location.postal_code)

location = 'varna'

def show_hotels(loc):
	hotels = webbrowser.open('https://www.google.bg/maps/search/hotel+' + location, new = 1,autoraise = True)
	return hotels

def show_restaurants(loc):
	rastaurants = webbrowser.open('https://www.google.bg/maps/search/restaurant+' + location, new = 1,autoraise = True)
	return restaurants

def show_bars(loc):
	bars = webbrowser.open('https://www.google.bg/maps/search/bar+' + location, new = 1,autoraise = True)
	return bars

def show_coffees(loc):
	coffees = webbrowser.open('https://www.google.bg/maps/search/coffee+' + location, new = 1,autoraise = True)
	return coffees

a = run_command(adb_commands['get-location'])
a = a.split("Location[network")[1].split("acc")[0]
latitude = a.split(",")[0]
longitude = a.split(",")[1]
print "latitude:", latitude
print "longitude:", longitude