import voice_recognition as vr
import adb
from callinfo import CallInfo
from memory import CommandQueue
from time import sleep

hardcoded = [
	'get contacts'
]

mem = CommandQueue()

for usr_input in hardcoded:
	real_commands = vr.extract_possible_commands(usr_input)
	mem = adb.run(real_commands, mem, usr_input)
