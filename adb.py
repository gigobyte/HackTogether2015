import subprocess
from dictionary import (adb_commands, commands)
from time import sleep
import re

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

def run(cmd):
	if cmd == commands['take-picture']:
		subprocess.Popen(adb_commands['camera-image-capture'], stdout=subprocess.PIPE, shell=True)
		subprocess.Popen(adb_commands['take-picture'], stdout=subprocess.PIPE, shell=True)

def get_device_model():
	info = subprocess.Popen(adb_commands['devices'], stdout=subprocess.PIPE, shell=True)
	try:
		return info.stdout.read().split('model:')[1].split(' ')[0] 
	except:
		return 'LG_D802'