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

def extract_possible_command(input):
	for command in dictionary.commands.values():
		if fuzz.ratio(command, input) > 75 or command in input:
			return command

		if fuzz.token_sort_ratio(command, input) > 75:
			return command

		if fuzz.partial_ratio(command, input) > 90 and fuzz.token_sort_ratio(command, input) > 50:
			return command