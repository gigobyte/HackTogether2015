import voice_recognition as vr
import adb
from memory import CommandQueue

hardcoded = [
	'Take a picture',
	'Save it to my computer'
]

mem = CommandQueue()

for usr_input in hardcoded:
	real_command = vr.extract_possible_command(usr_input)
	success = adb.run(real_command, mem)
	if success:
		mem.add(success)