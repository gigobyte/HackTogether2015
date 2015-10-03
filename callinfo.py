class CallInfo(object):
	def check_if_calling(self):
		out = run_command(adb_commands['check-callstate'])
		return out[-2] == '1'

	def get_caller_number(self):
		out = run_command(adb_commands['check-callnumber'])
		return out.split('=')[1]

	def accept_call(self):
		run_command(adb_commands['accept-call'])

	def decline_call(self):
		run_command(adb_commands['decline-call'])
