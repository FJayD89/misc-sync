from math import sqrt, floor, ceil, factorial, log10, log
from time import time
from itertools import permutations, product


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





def p1(L, length, a):
	while True:
		if str(2 ** a)[:length] == L:
			break

		a += 1
	return a


def p(L, n):
	length = len(L)
	i = 0
	a = 0
	for counter in range(n):
		a = p1(L, length, a) + 1
	return a - 1


def mod10pow10(p, c, m):
	# 10^(10^p)*c mod m, c < 10
	X = 10
	for i in range(p):
		X = X ** 10 % m
	return X ** c % m


# <editor-fold desc="misc-funcs">
def mathReplace(x, digit, index):
	log = 10**(floor(log10(x)) - index)
	ret = x + log*(10*(x//(10*log)) - x//log + digit)
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

mSum = 0
count = 0
largest = 0
smallest = 0
bigNum = 99
n = 1
flag = -1
a = 1
b = 1

if __name__ == '__main__':

	startTime = time()


	print("done")
	print('This took', time() - startTime)
