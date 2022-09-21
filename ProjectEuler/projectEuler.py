from math import sqrt, floor, ceil, factorial, log10, log
from time import time
from itertools import permutations, product


def prettify(treeList):
	strList = str(treeList)
	strOut = ''
	tabLevel = 0
	for charIndex in range(len(strList)):
		char = strList[charIndex]
		strOut += char
		if char == ']':
			if charIndex + 1 >= len(strList):
				continue
			nextChar = strList[charIndex + 1]
			if nextChar == ']':
				strOut += '\n'
				tabLevel -= 1
				for i in range(tabLevel):
					strOut += '\t'
				continue
		if char == ',':
			strOut += '\n'
			if strList[charIndex - 1] != ']':
				tabLevel += 1
			for i in range(tabLevel):
				strOut += '\t'
	return strOut


def zeroEval(numStr):
	if numStr[0] == '0':
		return zeroEval(numStr[1:])
	return int(numStr)


# f = open('C:/aCoding/Python/PycharmProjects/misc-sync/ProjectEuler/eulerText.txt')
# numPairs = f.read().split('\n')


# numPairs = [[int(num) for num in numPair.split(',')] for numPair in numPairs]
# print(numPairs)
# nums = [int(attempt) for attempt in lines]
# lines = [line.split(' ') for line in lines]
# lines = [[zeroEval(numStr) for numStr in line] for line in lines]


def cyclePolygons(k, m):
	polygons = []
	minIndex = minMaxStart(k, m)[0]
	maxIndex = minMaxStart(k, m)[1]
	maxNum = polygonNum(maxIndex, k)
	index = minIndex
	num = polygonNum(index, k)
	while num <= maxNum:
		polygons.append(num)
		num += index*(k-2)+1
		index += 1
	return polygons


def minMax4Digit(k):
	max = (k-4+sqrt((4-k)**2 + (k-2)*8*10**4))/(2*(k-2))
	min = (k-4+sqrt((4-k)**2 + (k-2)*8*10**3))/(2*(k-2))
	return [ceil(min), floor(max)]

def minMaxStart(k,m):
	min = (k-4+sqrt((4-k)**2 + (k-2)*m*800))/(2*(k-2))
	max = (k-4+sqrt((4-k)**2 + 8*(k-2)*(m*100+99)))/(2*(k-2))
	return [ceil(min), floor(max)]

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


# <editor-fold desc="misc-funcs">

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


def polygonNum(n, degree):
	return n*(n*(degree-2) + 4 - degree)/2

def mod10pow10(p, c, m):
	# 10^(10^p)*c mod m, c < 10
	X = 10
	for i in range(p):
		X = X ** 10 % m
	return X ** c % m


def mathReplace(x, digit, index):
	log = 10 ** (floor(log10(x)) - index)
	ret = x + log * (10 * (x // (10 * log)) - x // log + digit)
	return ret


def bigSum(num):
	bSum = 0
	for i in range(1, num + 1):
		bSum += smallestDSum(i)
	return bSum


def smallestDSum(num):
	x = floor(num / 9)
	return (1 + num - x * 9) * 10 ** x - 1


def sqareSum(num):
	numStr = str(num)
	nSum = 0
	for digit in numStr:
		nSum += int(digit) ** 2
	return nSum


def isPalindromic(num):
	strNum = str(num)
	for digit in range(ceil(len(strNum) / 2)):
		if not strNum[digit] == strNum[-digit - 1]:
			return False
	return True


def revSum(num):
	rev = ''
	for digit in str(num):
		rev = digit + rev
	return zeroEval(rev) + num


def isLychrel(num, iteration):
	num = revSum(num)
	print(num, iteration)
	if iteration == 50:
		return True
	if isPalindromic(num):
		return False

	return isLychrel(num, iteration + 1)


def digitSum(numStr):
	nSum = 0
	for digit in numStr:
		nSum += int(digit)
	return nSum


def merge(l1, l2):
	for item in l2:
		l1.append(item)
	return l1


def isCool(a0, d):
	if not (isPrime(a0) and isPrime(a0 + d) and isPrime(a0 + 2 * d)):
		return False
	if not isAPermutation(str(a0), str(a0 + d)):
		return False
	if not isAPermutation(str(a0), str(a0 + 2 * d)):
		return False
	return True


def isAPermutation(numStr1, numStr2):
	if not len(numStr1) == len(numStr2):
		return False

	for digit in numStr1:
		if not digit in numStr2:
			return False
	for digit in numStr2:
		if not digit in numStr1:
			return False

	return True


def factors(num):
	if num in [2, 3]:
		return [num]
	fList = []
	for i in range(2, floor(sqrt(num)) + 1):
		if num % i == 0:
			fList.append(i)
			break
		if i == floor(sqrt(num)):
			return [num]

	for factor in factors(num / fList[0]):
		if not factor in fList:
			fList.append(factor)
	return fList


def isPrime(num):
	# if num == 1:
	#     return False
	for i in range(2, floor(sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True


def conjecture(num):
	for i in range(2, floor(sqrt(num / 2)) + 1):
		if isPrime(num - 2 * i ** 2):
			return True
	return False


# </editor-fold>

trigger = True

mList = []
sList = []

mSum = 0
count = 0
largest = 0
smallest = 0
bigNum = 99
n = 1
flag = True
a = 1
b = 1

if __name__ == '__main__':
	startTime = time()
	maxMin = minMax4Digit(3)
	startIndex = maxMin[0]
	endIndex = maxMin[1]
	tris = []
	index = startIndex
	num = polygonNum(index, 3)
	while index <= endIndex:
		tris.append(num)
		num += index+1
		index += 1

	kChoices = [4,5,6,7,8]
	# kChoices = [4,5]
	for tri in tris:
		m1 = tri - 100*(tri//100)
		for k1 in list(kChoices):
			kChoices.remove(k1)
			for p1 in cyclePolygons(k1, m1):
				# if p1 < 1000:
				# 	continue
				for k2 in list(kChoices):
					kChoices.remove(k2)
					m2 = p1 - 100*(p1//100)
					for p2 in cyclePolygons(k2, m2):
						if p2 < 1000:
							continue
						for k3 in list(kChoices):
							kChoices.remove(k3)
							m3 = p2 - 100*(p2//100)
							for p3 in cyclePolygons(k3, m3):
								if p3 < 1000:
									continue
								for k4 in list(kChoices):
									kChoices.remove(k4)
									m4 = p3 - 100*(p3//100)
									for p4 in cyclePolygons(k4, m4):
										if p4 < 1000:
											continue
										k5 = kChoices[0]
										m5 = p4 - 100*(p4//100)
										for p5 in cyclePolygons(k5, m5):
											if p5 < 1000:
												continue
											if p5 - 100*(p5//100) == p1//100:
												print(p1, p2, p3, p4, p5)
									kChoices.append(k4)
							kChoices.append(k3)
					kChoices.append(k2)
			kChoices.append(k1)

	# desmos https://www.desmos.com/calculator/ivixfwuuks





	print("done")
	print('This took', time() - startTime)
