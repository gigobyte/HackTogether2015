import subprocess
from dictionary import (adb_commands, commands)
from time import sleep
from memory import Command
import re
import os

def setup():
	subprocess.Popen(adb_commands['kill-server'], stdout=subprocess.PIPE, shell=True)
	subprocess.Popen(adb_commands['start-server'], stdout=subprocess.PIPE, shell=True)

	subprocess.Popen(adb_commands['tcpip'], stdout=subprocess.PIPE, shell=True)
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

def run(cmd, context):
	location = None
	requested_command = None

	if cmd == commands['take-picture']:
		subprocess.Popen(adb_commands['take-picture'], stdout=subprocess.PIPE, shell=True)
		requested_command = commands['take-picture']
		sleep(3)
		location = subprocess.Popen(adb_commands['open-pictures'], stdout=subprocess.PIPE, shell=True)
		location = '/sdcard/DCIM/Camera/' + location.stdout.read().split('\n')[-2].replace('\r', '')
	if cmd == commands['save-computer'] or cmd == commands['save-pc']:
		what_to_save = context.commands[-1].action
		where_to_save = context.commands[-1].location

		if what_to_save == commands['take-picture']:
			save_command = adb_commands['pull'] + where_to_save + ' ' + os.environ['USERPROFILE']
			print save_command
			#subprocess.Popen(save_command, stdout=subprocess.PIPE, shell=True)


	cmd_obj = Command(cmd, location)

	return cmd_obj

def get_device_model():
	info = subprocess.Popen(adb_commands['devices'], stdout=subprocess.PIPE, shell=True)
	try:
		return info.stdout.read().split('model:')[1].split(' ')[0] 
	except:
		return 'LG_D802'