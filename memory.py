class Command(object):
	def __init__(self, cmd, location):
		self.action = cmd
		self.location = location

class CommandQueue(object):
	commands = []

	def add(self, cmd):
		self.commands.append(cmd)