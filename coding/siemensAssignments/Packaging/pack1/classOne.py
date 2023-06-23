print('ClassOne module is loaded')

class One:
	def __init__(self, num_one, str_one):
		self.numOne = num_one
		self.strOne = str_one
		print(self.strOne)

	def getNumOne(self):
		return self.numOne

	def getStrOne(self):
		return self.strOne

	def sayHello(self):
		print("SayHello from class one")