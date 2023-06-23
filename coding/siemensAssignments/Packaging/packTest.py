import pack1
import pack2

objOne = pack1.classOne.One(5, 'dataOne')
# objTwo = pack2.classTwo.Two(8, 'dataTwo') # raises error, pack2 has no attribute classTwo
objTwo = pack2.classTwo.Two(8, 'dataTwo')

modifiedObjOne = pack2.classModifyOne.ModifyOne('addendum')

added = modifiedObjOne.appendString(objOne)

print(added)

tester = pack1.testerModule.TestAll()
tester.testAllTypes()