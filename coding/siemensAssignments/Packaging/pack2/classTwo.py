print("ClassTwo module is loaded")

class Two:
	def __init__(self, num_two, str_two):
		self.numTwo = num_two
		self.strTwo = str_two
		print(self.strTwo)

	def getNumTwo(self):
		return self.numTwo

	def getStrTwo(self):
		return self.strTwo

	def sayHello(self):
		print("SayHello from class Two")