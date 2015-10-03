import subprocess
from dictionary import (adb_commands, commands)
from time import sleep
from memory import Command
from sms import SMS
import re
import os

def run_command(command):
	out = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	return out.stdout.read()

def setup():
	run_command(adb_commands['kill-server'])
	run_command(adb_commands['start-server'])
	run_command(adb_commands['tcpip'])
	#sleeping so that the phone can connect
	sleep(3)

	try:
		netcfg = subprocess.Popen(adb_commands['netcfg'], stdout=subprocess.PIPE, shell=True)
		for ip in netcfg.stdout.read().split('\n'):
			if ip.split(' ')[0] == 'wlan0':
				device_ip = re.search('192.168.0.\d+', ip).group()
				connect_command = adb_commands['connect'] + device_ip + ':5556'
	except:
		connect_command = adb_commands['connect'] + '10.10.10.242:5556'

	subprocess.Popen(connect_command, stdout=subprocess.PIPE, shell=True)
	print 'Setup ready!'

def run(command_list, context):
	def take_picture(cmd, context):
		print 'take_picture() called'
		subprocess.Popen(adb_commands['take-picture'], stdout=subprocess.PIPE, shell=True)
		requested_command = commands['take-picture']
		sleep(5)
		location = subprocess.Popen(adb_commands['open-pictures'], stdout=subprocess.PIPE, shell=True)
		return '/sdcard/DCIM/Camera/' + location.stdout.read().split('\n')[-2].replace('\r', '')

	def save(cmd, context):
		print 'save() called'
		what_to_save = context.commands[-1].action
		where_to_save = context.commands[-1].location

		if what_to_save == commands['take-picture']:
			save_dir = os.environ['USERPROFILE'] + '\\Desktop\\picture.jpg'
			save_command = adb_commands['pull'] + where_to_save + ' ' + save_dir
			subprocess.Popen(save_command, stdout=subprocess.PIPE, shell=True)
			sleep(2)
			os.system(save_dir)

		return where_to_save

	def show_messages(cmd, context):
		save_dir = os.environ['USERPROFILE'] + '\\Desktop\\sms.db'
		run_command(adb_commands['transfer-sms'])
		save_command = adb_commands['pull'] + '/sdcard/sms.db' + ' ' + save_dir
		run_command(save_command)
		sms = SMS(save_dir)

	def screen_capture(cmd, context, screen, command, sec):
		s = 'screen.' + screen
		save_dir = os.environ['USERPROFILE'] + '\\Desktop\\' + s
		run_command(adb_commands[command])
		save_command = adb_commands['pull'] + '/sdcard/' + s + ' ' + save_dir
		sleep(sec)
		run_command(save_command)
		return save_dir

	def take_screenshot(cmd, context):
		return screen_capture(cmd, context, 'png', 'take-screenshot', 5)

	def take_screenrecord(cmd, context):
		return screen_capture(cmd, context, 'mp4', 'take-screenrecord', 200)

	location = None
	requested_command = None
	print command_list
	for cmd in command_list:
		if cmd == commands['take-picture']:
			location = take_picture(cmd, context)
		elif cmd == commands['save-computer'] or cmd == commands['save-pc']:
			location = save(cmd, context)
		elif cmd == commands['show-msg'] or cmd == commands['show-sms']:
			location = show_messages(cmd, context)

		context.add(Command(cmd, location))

	return context

def get_device_model():
	info = subprocess.Popen(adb_commands['devices'], stdout=subprocess.PIPE, shell=True)
	try:
		return info.stdout.read().split('model:')[1].split(' ')[0]
	except:
		return 'LG_D802'

def check_if_calling():
	out = run_command(adb_commands['check-callstate'])
	return out[-2] == 1

def accept_call():
	run_command(adb_commands['accept-call'])

def decline_call():
	run_command(adb_commands['decline-call'])