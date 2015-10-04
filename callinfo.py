from adb import run_command
from dictionary import adb_commands
import os

class CallInfo(object):
	def check_if_calling(self):
		out = run_command(adb_commands['check-callstate'])
		return out[-2] == '1'

	def get_caller_number(self):
		out = run_command(adb_commands['check-callnumber'])
		return out.split('=')[1].replace('\n', '')

	def accept_call(self):
		run_command(adb_commands['accept-call'])

	def decline_call(self):
		run_command(adb_commands['decline-call'])

	def get_caller_name(self):
		export = os.environ['USERPROFILE'] + '\\Desktop\\db'
		run_command(adb_commands['db'] + 'content://com.android.contacts/data/phones/filter/' + self.get_caller_number() + ' --projection sort_key' + ' > ' + export)
		
		return open(export).read().split('sort_key=')[1].replace('\r', '').replace('\n', '')