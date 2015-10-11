from dictionary import (adb_commands, commands)
import webbrowser
from get_location import get_city

location = get_city()

def show_weather():
	webbrowser.open('https://www.google.bg/#q='+location+'+weather ', new = 1,autoraise = True)

show_weather()
