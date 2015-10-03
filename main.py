import voice_recognition as vr
import adb
from memory import CommandQueue
from time import sleep

while 1:
	

hardcoded = [
	'picture take and save it to my pc'
]

mem = CommandQueue()

for usr_input in hardcoded:
	real_commands = vr.extract_possible_commands(usr_input)
	mem = adb.run(real_commands, mem, usr_input)