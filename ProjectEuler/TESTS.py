from math import sqrt, floor, ceil, factorial, log10
from time import time
from itertools import permutations, product
from mathReplace import mathReplace
from projectEuler import primeConc, makeSieve, existsPrimeConcatenation


def zeroEval(numStr):
	if numStr[0] == '0':
		return zeroEval(numStr[1:])
	return int(numStr)

def mathConc(a,b, sieve):
	aLen = floor(log10(a))+1
	bLen = floor(log10(b))+1
	return sieve[b*10**aLen + a] and sieve[a*10**bLen + b]


# f = open('eulerText.txt')
# nums = f.read().split(',')
# nums = [int(num) for num in nums]
# nums = [int(attempt) for attempt in lines]
# lines = [line.split(' ') for line in lines]
# lines = [[zeroEval(numStr) for numStr in line] for line in lines]

# <editor-fold desc="misc-funcs">
def bigSum(num):
	bSum = 0
	for i in range(1,num+1):
		bSum += smallestDSum(i)
	return bSum


def smallestDSum(num):
	x = floor(num/9)
	return (1+num-x*9)*10**x - 1


def sqareSum(num):
	numStr = str(num)
	nSum = 0
	for digit in numStr:
		nSum += int(digit)**2
	return nSum


def isPalindromic(num):
	strNum = str(num)
	for digit in range(ceil(len(strNum)/2)):
		if not strNum[digit] == strNum[-digit-1]:
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

	return isLychrel(num, iteration+1)


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
	if not (isPrime(a0) and isPrime(a0 + d) and isPrime(a0+2*d)):
		return False
	if not isAPermutation(str(a0), str(a0+d)):
		return False
	if not isAPermutation(str(a0), str(a0+2*d)):
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
	if num in [2,3]:
		return [num]
	fList = []
	for i in range(2, floor(sqrt(num))+1):
		if num % i == 0:
			fList.append(i)
			break
		if i == floor(sqrt(num)):
			return [num]

	for factor in factors(num/fList[0]):
		if not factor in fList:
			fList.append(factor)
	return fList


def isPrime(num):
	# if num == 1:
	#     return False
	for i in range(2, floor(sqrt(num))+1):
		if num % i == 0:
			return False
	return True


def conjecture(num):
	for i in range(2, floor(sqrt(num/2))+1):
		if isPrime(num - 2 * i**2):
			return True
	return False
# </editor-fold>


startTime = time()

primeSieve = makeSieve(10**8)
print('Sieve setup done')

# for i in range(1,10000):
# 	for j in range(1,10000):
# 		mathConc(i,j,primeSieve) # 134.6022346019745
# 		# primeConc(i,j,primeSieve) # 110.62362289428711
a = 302

if a:
	print('true')

print("done")
print('This took', time()-startTime)