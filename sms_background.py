import voice_recognition as vr
import adb
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


def display_message(message):
	global win
	win = Tkinter.Tk()
	win.overrideredirect(1)
	win.title("Last Message")
	
	width = 200
	height = 200
	win.resizable(width=FALSE, height=FALSE)
	ws = win.winfo_screenwidth() # width of the screen
	hs = win.winfo_screenheight() # height of the screen
	x = (ws/1.2) - (width/2)
	y = (hs/1.5) - (height/2)
	win.geometry('%dx%d+%d+%d' % (width, height, x, y))
	win.configure(background='white')
	
	Label(win, text=message, background="white",
	 font=tkFont.Font(family="Helvetica", size=15), wraplength=200, justify=CENTER).pack()

	global play_sound_thread
	play_sound_thread = Process(target=playSound)
	play_sound_thread.start()

	win.mainloop()

def playSound():
		winsound.PlaySound('recordings/sms_sound.wav', winsound.SND_FILENAME)

def main():
	message = "GG NO RE MUTHA FUCKA !!!"
	display_message(message)
	'''call = CallInfo()
	check_call = False
	while(not check_call):
		check_call = call.check_if_calling()
		if(check_call == True):
			respondCall()'''

	adb.

if __name__ == '__main__':
	main()