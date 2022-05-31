# from time import time

inputs = [int(inp) for inp in input().split(' ')]
amount = inputs[0]
startDog = inputs[1]
dogRange = inputs[2]
steps = inputs[3]
dogs = [int(dog) for dog in input().split(' ')]
dogPos = dogs[inputs[1]]


def getHighEnd(dogs, startDog):
	highEnd = amount-1
	for index, dog in enumerate(dogs[startDog:-1], start=startDog):
		if dogs[index + 1] - dog > dogRange:
			highEnd = index
			break
	return highEnd


def getLowEnd(dogs, startDog):
	lowEnd = 0
	enumed = enumerate(dogs[1:startDog+1], start=1)

	for index, dog in reversed(tuple(enumed)):
		if dog - dogs[index - 1] > dogRange:
			lowEnd = index
			break
	return lowEnd


endPos = dogs[startDog]

mHighEnd = getHighEnd(dogs, startDog)
mLowEnd = getLowEnd(dogs, startDog)

if not mHighEnd == mLowEnd:
	steps = steps % (2*amount - 2)
	currentDog = startDog
	direction = 1
	for i in range(steps):
		if currentDog == mLowEnd or currentDog == mHighEnd:
			direction = -direction
		currentDog = currentDog + direction
	endPos = dogs[currentDog]

print(endPos)
# print(time() - startTime)
