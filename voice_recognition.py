import speech_recognition as sr
import dictionary
from fuzzywuzzy import fuzz

def get_mic_input():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	print 'audio done'

	try:
		return r.recognize_google(audio)
	except:
		pass

def get_text_from_wav(path):
	r = sr.Recognizer()

	with sr.WavFile(path) as source:
		audio = r.record(source)

	return r.recognize_google(audio)

def filter_kind_words(command):
	for kind_word in dictionary.kind_words:
		command = command.replace(kind_word, '')

	return command

def extract_possible_commands(inputs):
	possible_commands = []

	for input in inputs.split(' and '):
		input = filter_kind_words(input)
		for command in dictionary.commands.values():
			if fuzz.ratio(command, input) > 75 or command in input:
				possible_commands.append(command)

	return possible_commands