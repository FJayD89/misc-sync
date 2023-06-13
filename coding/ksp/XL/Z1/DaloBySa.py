cars = input()
leftEdge = 0
rightEdge = 0
zrazky = 0
for i in range(len(cars)):
	car = cars[i]
	if car != '<':
		leftEdge = i
		break
for i in range(len(cars)-1, -1, -1):
	car = cars[i]
	if car != '>':
		rightEdge = i
		break
for car in cars[leftEdge:rightEdge+1]:
	if car != '=':
		zrazky += 1
print(zrazky)


