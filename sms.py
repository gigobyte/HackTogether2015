	#'send sms' : 'platform-tools\\adb shell "am start -a android.intent.action.SENDTO -d sms:0894466198 --es sms_body \"SMS4E\" --ez exit_on_sent true && input keyevent 22 && input keyevent 66"',
import sqlite3

class SMS(object):
	def __init__(self, db):
		print db
		self.smss = sqlite3.connect(db)
		self.smss = self.smss.cursor()
		self.smss = self.smss.execute('SELECT * FROM sqlite_master;')

	def last(self):
		return self.smss[0]

	def all(self):
		return self.smss