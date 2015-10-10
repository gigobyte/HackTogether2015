import subprocess
from pygeocoder import Geocoder
from dictionary import (adb_commands, commands)
from adb import run_command

def loc():
	a = run_command(adb_commands['get-location'])
	a = a.split("Location[network")[1].split("acc")[0]
	latitude = a.split(",")[0]
	longitude = a.split(",")[1]
	#print "latitude:", latitude
	#print "longitude:", longitude

	results = Geocoder.reverse_geocode(float(latitude),float(longitude))
	return str(results).split(',')[0].decode('unicode_escape').encode('ascii','ignore')