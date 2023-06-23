print("otherP1Module is loaded")

import pack1.classOne
import pack2 as p2

class TestAll:
	def __init__(self):
		pass

	def testOneObj(self):
		testObj = pack1.classOne.One(100, "Testing obj One")
		testObj.sayHello()
		print(testObj.getNumOne())

	def testTwoObj(self):
		testObj = p2.classTwo.Two(200, "Testing obj Two")
		testObj.sayHello()
		print(testObj.getNumTwo())

	def testModifyOne(self):
		pass

	def testAllTypes(self):
		self.testOneObj()
		self.testTwoObj()
		self.testModifyOne()