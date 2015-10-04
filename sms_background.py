import voice_recognition as vr
import adb
from dictionary import adb_commands
from callinfo import CallInfo
from memory import CommandQueue
from time import sleep
import itertools, glob
import winsound, sys
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
from multiprocessing import Process

def respond_to_sms(receiver, msg):
	print adb.run_command(adb_commands['send-sms'].format(receiver,msg[:-1]))
	global win
	win.destroy()

def display_message(message, mob_number):
	global win
	win = Tkinter.Tk()
	win.overrideredirect(1)
	win.title("Last Message")
	
	width = 200
	height = 300
	win.resizable(width=FALSE, height=FALSE)
	ws = win.winfo_screenwidth() # width of the screen
	hs = win.winfo_screenheight() # height of the screen
	x = (ws/1.2) - (width/2)
	y = (hs/1.5) - (height/2)
	win.geometry('%dx%d+%d+%d' % (width, height, x, y))
	win.configure(background='white')

	''' SHOW EXIT ICON '''
	exit_image = ImageTk.PhotoImage(file="images/exit.png")
	exit_button = Tkinter.Button(win, image =exit_image, command = onClosing, background = "white", bd = 0)
	exit_button.pack(anchor = "se")

	call_info = "You received new message from:\n" + mob_number
	Label(win, text=call_info, background="white",
	 font=tkFont.Font(family="Helvetica", size=12), wraplength=200, justify=CENTER).pack()
	
	message = "\"" + message + "\""
	Label(win, text=message, background="white",
	 font=tkFont.Font(family="Helvetica", size=13), wraplength=200, justify=CENTER).pack()

	tbox = Text(win, height=3 , width=180)

	respond_image = ImageTk.PhotoImage(file="images/respond.png")
	respond = Tkinter.Button(win, image =respond_image, command = lambda: respond_to_sms(mob_number, tbox.get("1.0",'end-1c')), background = "white", bd = 0)
	tbox.pack()
	respond.pack(fill="x", anchor="s")

	global play_sound_thread
	play_sound_thread = Process(target=playSound)
	play_sound_thread.start()

	win.mainloop()

def onClosing():
	global win
	win.destroy()

def playSound():
		winsound.PlaySound('recordings/sms_sound.wav', winsound.SND_FILENAME)

def main():
	last_sms = "dfjgksldf"
	check = True
	while(check):
		check_sms = adb.get_sms('content://sms/inbox').last()[0]
		if(last_sms != check_sms):
			mob_number = adb.get_sms('content://sms/inbox').last()[1]
			display_message(check_sms, mob_number)
			check = False


if __name__ == '__main__':
	main()