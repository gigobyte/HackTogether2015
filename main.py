import voice_recognition as vr
import adb

adb.setup()

while True:
	usr_input = vr.get_mic_input()
	if usr_input:
		real_command = vr.extract_possible_command(usr_input)
		adb.run(real_command)