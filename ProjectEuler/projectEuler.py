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


def is_permuted(num1, num2):
	str_num1 = str(num1)
	str_num2 = str(num2)
	digits = {digit:0 for digit in str_num1}
	for digit in str_num1:
		digits[digit] += 1
	for digit in str_num2:
		if not digit in digits:
			return False
		digits[digit] -= 1
	for digitCount in digits.values():
		if digitCount != 0:
			return False
	return True


def largest_permutation(num):
	num_str = str(num)
	num_str = sorted(num_str, reverse=True)
	num_str = ''.join(num_str)
	return int(num_str)


def sum_combinations(num):
	global allCombins
	combins = [0 for _ in range(num+1)]
	for k in range(1,num//2 +1):
		# i is the smallest number in the sum
		# in the list, the index is <= the smallest num in the sum and the value is how many such sums there are
		# so we want the following
		# for 1
		sumCount = allCombins.get(k, -1)
		if sumCount == -1:
			allCombins[num-k] = (sum_combinations(num-k))
		combins[k] = sum(allCombins[num-k][k:])
	combins[num] = 1
	# if combin in
	
	return combins


def factorial_digit_sum(num):
	facts = [factorial(int(i)) for i in str(num)]
	return sum(facts)

def len_factorial_chain(start_num):
	global factSums
	encountered = [start_num]
	next = start_num
	while True:
		getNext = factSums.get(next, -1)
		if getNext == -1:
			factSums[next] = factorial_digit_sum(next)
			getNext = factSums[next]
		next = getNext
		if next in encountered:
			# take all the nums encountered and add them to the dict, with the value as inverse index
			for encIndex in range(len(encountered)):
				factSums[encountered[encIndex]] = encIndex
			return len(encountered)
		encountered.append(next)


f = open('eulerText.txt')
lines = f.read().split('\n')
lines = [line.split(',') for line in lines]
lines = [[int(numStr) for numStr in line] for line in lines]

# numPairs = [[int(num) for num in numPair.split(',')] for numPair in numPairs]
# print(numPairs)
# nums = [int(attempt) for attempt in lines]
# lines = [line.split(' ') for line in lines]
# lines = [[zeroEval(numStr) for numStr in line] for line in lines]


# <editor-fold desc="misc-funcs">


def areConsecutive(num_list):
	if len(num_list) != 5:
		return False
	num_list = sorted(num_list)
	for index in range(4): # 5 = len(hand)
		if num_list[index]+1 != num_list[index+1]:
			return False
	return True


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


def minMaxPolygonal(k, a, b):
	min = (k-4+sqrt((4-k)**2 + 8*(k-2)*a))/(2*(k-2))
	max = (k-4+sqrt((4-k)**2 + 8*(k-2)*b))/(2*(k-2))
	return [ceil(min), ceil(max)]


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
n = 8
flag = True
a = 1
b = 1
allCombins = {}  # protected
factSums = {}  # protected

if __name__ == '__main__':
	startTime = time()
	
	# print(len_factorial_chain(69))
	
	for i in range(10**5):
		if len_factorial_chain(i) == 60:
			count += 1
	
	print(len(factSums))
	# print(count)
	print("done")
	print('This took', time() - startTime)
