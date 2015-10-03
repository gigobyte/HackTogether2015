import voice_recognition as vr
import adb
from memory import CommandQueue
from time import sleep

hardcoded = [
	'Take a picture and save it to my computer'
]

mem = CommandQueue()

for usr_input in hardcoded:
	real_commands = vr.extract_possible_commands(usr_input)
	mem = adb.run(real_commands, mem)