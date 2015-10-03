import subprocess
from dictionary import (adb_commands, commands)
from time import sleep
from memory import Command
from sms import SMS
import re
import os

def run_command(command):
	return subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.read()

def setup():
	run_command(adb_commands['kill-server'])
	run_command(adb_commands['start-server'])
	run_command(adb_commands['tcpip'])
	#sleeping so that the phone can connect
	sleep(3)

	try:
		netcfg = run_command(adb_commands['netcfg'])
		for ip in netcfg.split('\n'):
			if ip.split(' ')[0] == 'wlan0':
				device_ip = re.search('192.168.0.\d+', ip).group()
				connect_command = adb_commands['connect'] + device_ip + ':5556'
	except:
		connect_command = adb_commands['connect'] + '10.10.10.242:5556'

	run_command(connect_command)
	print 'Setup ready!'

def run(command_list, context, original_input):
	def take_picture(cmd, context):
		print 'take_picture() called'
		run_command(adb_commands['take-picture'])
		requested_command = commands['take-picture']
		sleep(5)
		location = run_command(adb_commands['open-pictures'])
		return '/sdcard/DCIM/Camera/' + location.split('\n')[-2].replace('\r', '')

	def save(cmd, context):
		print 'save() called'
		what_to_save = context.commands[-1].action
		where_to_save = context.commands[-1].location

		if what_to_save == commands['take-picture']:
			save_dir = os.environ['USERPROFILE'] + '\\Desktop\\picture.jpg'
			save_command = adb_commands['pull'] + where_to_save + ' ' + save_dir
			run_command(save_command)
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

		if command == 'take-screenrecord':
			run_command(adb_commands[command] + ' --time-limit ' + str(sec))
			save_command = adb_commands['pull'] + '/sdcard/' + s + ' ' + save_dir
			sleep(sec+5)
		run_command(save_command)
		os.system(save_dir)
		return save_dir

	def take_screenshot(cmd, context):
		return screen_capture(cmd, context, 'png', 'take-screenshot', 5)

	def take_screenrecord(cmd, context, seconds):
		return screen_capture(cmd, context, 'mp4', 'take-screenrecord', seconds)

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
		elif cmd == commands['take-screenshot']:
			location = take_screenshot(cmd, context)
		elif cmd == commands['record-screen']:
			seconds = [int(i) for i in original_input.split() if i.isdigit()][0]
			print seconds
			location = take_screenrecord(cmd, context, seconds)

		context.add(Command(cmd, location))

	return context

def get_device_model():
	info = run_command(adb_commands['devices'])
	try:
		return info.split('model:')[1].split(' ')[0]
	except:
		return 'LG_D802'