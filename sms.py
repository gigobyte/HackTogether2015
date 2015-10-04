class SMS(object):
	def __init__(self, path):
		self.file = open(path).read()
		self.smss = []

	def last(self):
		return self.all()[0]

	def all(self):
		self.smss = []

		for line in self.file.split('\n'):
			try:
				self.smss.append(
					[line.split('body=')[1].split(', service_center')[0], line.split('address=')[1].split(' ')[0]]
				)
			except IndexError:
				pass

		return self.smss