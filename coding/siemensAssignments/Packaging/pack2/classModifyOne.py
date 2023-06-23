import pack1.classOne as cOne

print("ClassModifyOne is loaded")

class ModifyOne:
	def __init__(self, str_add):
		self.stringToAdd = str_add

	def appendString(self, one_obj):
		oneStr = one_obj.getStrOne()
		return oneStr + ' ' + self.stringToAdd

	def makeObjectOne(self):
		objOne = cOne.One(5, 'text')
		objOne.sayHello()