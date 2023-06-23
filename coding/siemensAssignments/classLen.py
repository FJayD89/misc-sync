class TestType:
	def __init__(self, title, number, data):
		self.title = title
		self.number = number
		self.data = data

	def getString(self):
		return self.title

	# def __len__(self):
	# 	return len(self.data)


testDict = {
	4: 5,
	6: 3
}

# testInt = 654
#
# testBitLen = testInt.bit_length()
#
# print (testBitLen)

newObj = TestType('OBJ', 5, 'someData')

print(len(newObj))

