import voice_recognition as vr
import adb
from memory import CommandQueue
from time import sleep

# hardcoded = [
# 	''
# ]

# mem = CommandQueue()

# for usr_input in hardcoded:
# 	real_commands = vr.extract_possible_commands(usr_input)
# 	mem = adb.run(real_commands, mem)

print vr.extract_possible_commands('Can you please take a picture')
print vr.extract_possible_commands('Could you take picture')