import voice_recognition as vr

test_inputs = [
	'can you please take a picture',
	'take a picture please',
	'could you take a picture please',
	'save it to my computer',
	'could you save it to my computer please',
	'i want you to save it to my computer',
	'would you take a picture and save it to my computer',
	'could you save it to my pc please',
	'i want you to save it to my pc',
	'would you take a picture and save it to my pc',
	'can you show my messages please',
	'i hope that you can show me my messages',
	'show my sms',
	'i want you to show my sms',
	'take a screenshot',
	'take a screenshot right now',
	'can you please take a screenshot',
	'record my screen for 10 seconds',
	'i want you to record my screen for 10 seconds and save it to my computer please'
]

for input in test_inputs:
	#print input
	_ =  vr.extract_possible_commands(input)

print 'test:can you please take a picture'
print vr.filter_kind_words('test:can you please take a picture')