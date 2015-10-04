import voice_recognition as vr
import adb
from callinfo import CallInfo
from memory import CommandQueue
from time import sleep
import itertools, glob

from system_tray_lib import *
import Tkinter
import sys
from Tkinter import *
from PIL import Image, ImageTk
import urllib
import adb
import requests
import threading
import tkFont
import tkMessageBox
import subprocess

listening = False

def startSystemTray():
	global device
	icons = itertools.cycle(glob.glob('images/*.ico'))
	hover_text = "Smartphone Voice"
	menu_options = (('Show',None,Remake),
						('Start/Stop', None, microphoneAction),)
	SysTrayIcon(icons.next(), hover_text, menu_options, on_quit=Terminate, default_menu_index=1)

def onClosing():
	global top
	top.destroy()

def Terminate():
	sys.exit()

def Remake():
	main()

def microphoneAction():
	global microphone_check
	global microphone
	global device
	global listening
	microphone_check = not microphone_check
	if microphone_check:
		image = ImageTk.PhotoImage(Image.open('images/button_activated.gif'))
		microphone.config(image=image, background = "white", bd = 0)
		microphone.image = image
		threading.Thread(target=listen_and_do).start()
		listening = True
	else:
		image = ImageTk.PhotoImage(Image.open('images/1.png'))
		microphone.config(image=image, background = "white", bd = 0)
		microphone.image = image
		listening = False

def listen_and_do():
	result = vr.get_text_from_wav('recordings/take_a_picture.wav')
	print result
	mem = CommandQueue()
	real_commands = vr.extract_possible_commands(result)
	mem = adb.run(real_commands, mem, result)
	result = vr.get_text_from_wav('recordings/send_computer.wav')
	real_commands = vr.extract_possible_commands(result)
	mem = adb.run(real_commands, mem, result)

	'''
	print 'listen_and_do() called'
	mem = CommandQueue()
	global listening

	while listening:
		usr_input = vr.get_mic_input()
		print usr_input
		real_commands = vr.extract_possible_commands(usr_input)
		mem = adb.run(real_commands, mem, usr_input)'''

def gui():
	global top
	top = Tkinter.Tk()

	global microphone_check
	global microphone
	global device
	flag = 0
	top.overrideredirect(1)
	top.title("Smartphone Voice")
	top.wm_iconbitmap('images/voice15.ico')
	top.configure(background='white')
	image = Image.open('phone.jpg')
	
	image_size = image.size
	width = image_size[0]
	height = image_size[1]
	set_width = width - 125
	
	top.resizable(width=FALSE, height=FALSE)
	ws = top.winfo_screenwidth() # width of the screen
	hs = top.winfo_screenheight() # height of the screen
	x = (ws/1.05) - (width/2)
	y = (hs/1.28) - (height/2)
	top.geometry('%dx%d+%d+%d' % (width+10, height+92, x, y))

	''' SHOW EXIT ICON '''
	exit_image = ImageTk.PhotoImage(file="images/exit.png")
	exit_button = Tkinter.Button(top, image =exit_image, command = onClosing, background = "white", bd = 0)
	exit_button.pack(anchor = "se")

	''' SHOW SMARTPHONE '''
	image = Image.open('phone.jpg')
	image_size = image.size
	photoImage = ImageTk.PhotoImage(image)
	label = Label(image=photoImage, background = 'white')
	label.image = photoImage
	label.pack(fill="x")

	''' SHOW TEXT '''
	connect_to_string = "Connected to " + device + ":"
	connect_to = Label(text=connect_to_string, background = 'white', font=tkFont.Font(family="Helvetica", size=10))
	if len(device) <= 9:
		connect_to = Label(text=connect_to_string, background = 'white', font=tkFont.Font(family="Helvetica", size=10))
	else:
		connect_to_string = "Connected to " + "\n" + device + ":"
		connect_to = Label(text=connect_to_string, background = 'white', font=tkFont.Font(family="Helvetica", size=9))
	connect_to.text = connect_to_string
	connect_to.pack(fill="x")

	''' SHOW/UPDATE BUTTON '''
	microphone_image = ImageTk.PhotoImage(file="images/1.png")
	microphone = Tkinter.Button(top, image =microphone_image, command = microphoneAction, background = "white", bd = 0)
	microphone.pack(fill="x")

	top.protocol("WM_DELETE_WINDOW", onClosing)
	
	top.mainloop()

def main():
	global device
	device = adb.get_device_model()
	url = "http://www.gsmarena.com/results.php3?sQuickSearch=yes&sName=" + device
	scraped_page = requests.get(url).text
	model_name = scraped_page.split("specs-phone-name-title")[1].split("h1")[0].split(">")[1].split("<")[0]
	print model_name
	device = model_name
	scraped_page = scraped_page.split("http://cdn2.gsmarena.com/vv/bigpic/")[1].split("alt=")[0].split(";")[0]
	scraped_gsm_image = scraped_page[:-1]
	global microphone_check
	microphone_check = 0
	urllib.urlretrieve("http://cdn2.gsmarena.com/vv/bigpic/%s" % scraped_gsm_image, "phone.jpg")
	system_tray_thread = threading.Thread(target=startSystemTray)
	system_tray_thread.daemon = True
	system_tray_thread.start()
	gui()
	

if __name__ == '__main__':
	subprocess.Popen(["python", 'calls_background.py'])
	main()
