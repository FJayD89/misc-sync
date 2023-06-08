

pocetVyhladov = int(input())

vyhlady = [int(vyhlad) for vyhlad in input().split(' ')]

bestDS = 2*pocetVyhladov
bestPair = [0,0]

potentialMaxIndex = 0

for vyhladIndex in range(pocetVyhladov):
	if vyhlady[vyhladIndex] > vyhlady[potentialMaxIndex]:
		potentialMaxIndex = vyhladIndex

maxIndex = potentialMaxIndex


center = vyhlady[maxIndex]
diffSum = 0
lI = 0
hI = 0
newSights = vyhlady[maxIndex + 1:] + vyhlady[:maxIndex+1]
# lists the sights from the right of index, then wraps around and ends with index
for lowerIndex in range(pocetVyhladov-2, -1, -1):
	# starts at -2 to exclude center
	diffSum += 1
	lower = newSights[lowerIndex]
	if lower < center:
		lI = (lowerIndex + maxIndex + 1) % pocetVyhladov
		break

for higherIndex in range(pocetVyhladov):
	diffSum += 1
	higher = newSights[higherIndex]
	if higher < center:
		hI = (higherIndex + maxIndex + 1) % pocetVyhladov
		break

# diffSum = hI + pocetVyhladov - lI
if diffSum < bestDS:
	bestDS = diffSum
	bestPair = [lI, maxIndex, hI]



out = str(bestPair[0]) + " " + str(bestPair[1]) + " " + str(bestPair[2])
print(out)
print(bestDS)



