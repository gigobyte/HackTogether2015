import speech_recognition as sr

def get_mic_input():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	try:
		return r.recognize_google(audio)
	except sr.UnknownValueError:
		print "Google Speech Recognition could not understand audio"
	except sr.RequestError:
		print "Could not request results from Google Speech Recognition service"

while True:
	usr_input = get_mic_input()
	print usr_input