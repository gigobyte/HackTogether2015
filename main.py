import voice_recognition as vr
import adb
print adb.get_device_model()

hardcoded = [
	'Take a picture',
	'Can you please take a picture',
	'Picture take'
]

for usr_input in hardcoded:
	real_command = vr.extract_possible_command(usr_input)
	adb.run(real_command)