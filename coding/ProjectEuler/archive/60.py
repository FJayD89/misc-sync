from math import sqrt


def makeSieve(sieveSize):
	sieve = [True for i in range(sieveSize)]
	sieve[0] = False
	sieve[1] = False

	# declare all multiples of two nonprime
	for composite in range(4, sieveSize, 2):
		sieve[composite] = False

	for num in range(3, int(sqrt(sieveSize))):
		# print(num)
		if not sieve[num]:
			continue
		for composite in range(num ** 2, sieveSize, 2 * num):
			sieve[composite] = False
	return sieve


def primeConc(a, b, sieve):
	strA, strB = str(a), str(b)
	return sieve[int(strA + strB)] and sieve[int(strB + strA)]


def existsPrimeConcatenation(primeListList, sieve):
	for i in range(len(primeListList)):
		for j in range(i + 1, len(primeListList)):
			if primeConc(primeListList[i][0], primeListList[j][0], sieve):
				return [True, [primeListList[i][0], primeListList[j][0]]]
	return [False]


def list60(leastPrime, upLimit, primeSieve):
	mList = [leastPrime]
	sList = [leastPrime]

	nextPrime = 7  # if leastPrime == 3
	if leastPrime != 3:
		i = leastPrime + 6
		while True:
			if primeSieve[i]:
				nextPrime = i
				break
			i += 6

	for j in range(nextPrime, upLimit, 6):
		if primeSieve[j]:
			if primeConc(leastPrime, j, primeSieve):
				mList.append([j])
	# print(mList)
	for subListIndex in range(1, len(mList)):
		hasChild = False
		subList = mList[subListIndex]
		lead = subList[0]
		for j in mList[subListIndex + 1:]:
			potentialConc = j[0]
			if primeConc(lead, potentialConc, primeSieve):
				subList.append([potentialConc])
				hasChild = True
		if hasChild:
			sList.append(subList)
	# print(sList)
	mList = [leastPrime]

	for subListIndex1 in range(1, len(sList)):
		hasChild1 = False
		subList1 = list(sList[subListIndex1])
		mSubList1 = list([subList1[0]])
		for subListIndex2 in range(1, len(subList1)):
			hasChild2 = False
			subList2 = list(subList1[subListIndex2])
			lead = subList2[0]
			for j in subList1[subListIndex2 + 1:]:  # maybe start from +1
				potentialConc = j[0]
				if primeConc(lead, potentialConc, primeSieve):
					subList2.append([potentialConc])
					hasChild1 = True
					hasChild2 = True
			if hasChild2:  # hasChild2
				if len(subList2) >= 3:
					concatenation = existsPrimeConcatenation(subList2[1:], primeSieve)
					if concatenation[0]:
						print('FOUND!!!')
						setSum = sum([leastPrime, subList1[0], subList2[0],
								concatenation[1][0], concatenation[1][1]])
						return setSum
					# return True
					mSubList1.append(subList2)
		if hasChild1:  # hasChild1
			mList.append(mSubList1)

	# return mList
	return False