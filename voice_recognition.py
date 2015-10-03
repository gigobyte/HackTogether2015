import speech_recognition as sr
import dictionary
from fuzzywuzzy import fuzz

def get_mic_input():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	try:
		return r.recognize_google(audio)
	except:
		pass

def extract_possible_commands(inputs):
	possible_commands = []

	for input in inputs.split(' and '):
		for command in dictionary.commands.values():
			if fuzz.ratio(command, input) > 75 or command in input:
				possible_commands.append(command)

			elif fuzz.token_sort_ratio(command, input) > 75:
				possible_commands.append(command)

			elif fuzz.partial_ratio(command, input) > 90 and fuzz.token_sort_ratio(command, input) > 50:
				possible_commands.append(command)

	return possible_commands