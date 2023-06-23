from math import sqrt, floor, ceil, factorial, log10, log
from time import time
from itertools import permutations, product


def prettify(tree_list):
	strList = str(tree_list)
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


def zeroEval(num_str):
	if num_str[0] == '0':
		return zeroEval(num_str[1:])
	return int(num_str)



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


def is_permuted(num1, num2):
	str_num1 = str(num1)
	str_num2 = str(num2)
	if len(str_num1) != len(str_num2):
		return False
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


def largest_digit_permutation(num):
	num_str = str(num)
	num_str = sorted(num_str, reverse=True)
	num_str = ''.join(num_str)
	return int(num_str)


def least_digit_permutation(num):
	num_str = str(num)
	num_str = sorted(num_str)
	num_str = ''.join(num_str)
	return int(num_str)


def ldp(num):
	# somehow this is almost exactly as good as the other one
	# thought sorted was going to take longer, apparently not
	digitCounts = {str(digit):0 for digit in range(10)}
	num_str = str(num)
	for num_digit in num_str:
		digitCounts[num_digit] += 1
	leastPermutation = ''
	for digit in digitCounts.keys():
		leastPermutation += digit*digitCounts[digit]

	return int(leastPermutation)


def len_factorial_chain(start_num, do_print = False):
	
	global factSums  # required factSums = [-1 for _ in range(neededSize)]
	encountered = [start_num]
	nextNum = start_num
	while True:
		# first, check if there's an entry for the num
		foundChainLen = factSums[nextNum]

		if foundChainLen != -1:
			# if there is, cool!
			# we can go back through all the encounters and add them to the list
			# excluding this last
			# say we have an encountered = [A,B,FOUND] and fcl
			# fcl[A] = len(enc)-index - 1 + fcl
			# fcl[B] = len(enc)-index - 1 + fcl
			for encIndex in range(len(encountered)-1):
				encounteredNum = encountered[encIndex]
				factSums[encounteredNum] = len(encountered) -1 - encIndex + foundChainLen
			# and return
			if do_print:
				print(encountered)
			return factSums[start_num]

		nextNum = factorial_digit_sum(nextNum)
		if nextNum in encountered:
			# take all the nums encountered and add them to the dict, with the value as inverse index
			# since we want the len of the unique num string
			# so for instance if we have 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
			# encIndex(363600) == 1
			# expected value == 4 == len - encIndex
			for encIndex in range(len(encountered)):
				encounteredNum = encountered[encIndex]
				factSums[encounteredNum] = len(encountered) - encIndex
			if do_print:
				print(encountered)
			return len(encountered)
		encountered.append(nextNum)


def sum_combinations(num):
	global allCombins  # required external empty dict
	combins = [0 for _ in range(num + 1)]
	for k in range(1, num // 2 + 1):
		# i is the smallest number in the sum
		# in the list, the index is <= the smallest num in the sum and the value is how many such sums there are
		# so we want the following
		# for 1
		sumCount = allCombins.get(k, -1)
		if sumCount == -1:
			allCombins[num - k] = (sum_combinations(num - k))
		combins[k] = sum(allCombins[num - k][k:])
	combins[num] = 1
	# if combin in

	return combins


def factorial_digit_sum(num):
	facts = [factorial(int(i)) for i in str(num)]
	return sum(facts)


def areConsecutive(num_list):
	if len(num_list) != 5:
		return False
	num_list = sorted(num_list)
	for index in range(4): # 5 = len(hand)
		if num_list[index]+1 != num_list[index+1]:
			return False
	return True


def makeSieve(sieve_size):
	sieve = [True for i in range(sieve_size)]
	sieve[0] = False
	sieve[1] = False

	# declare all multiples of two nonprime
	for composite in range(4, sieve_size, 2):
		sieve[composite] = False

	for num in range(3, int(sqrt(sieve_size))):
		# print(num)
		if not sieve[num]:
			continue
		for composite in range(num ** 2, sieve_size, 2 * num):
			sieve[composite] = False
	return sieve


def minMaxPolygonal(k, lim_low, lim_high):
	# returns the smallest polygNum > a, and the largest < b
	minPolygonal = (k-4+sqrt((4-k)**2 + 8*(k-2)*lim_low))/(2*(k-2))
	maxPolygonal = (k-4+sqrt((4-k)**2 + 8*(k-2)*lim_high))/(2*(k-2))
	return [ceil(minPolygonal), ceil(maxPolygonal)]


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
	# what black magic is this
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


def isAPermutation(num_str1, num_str2):
	if not len(num_str1) == len(num_str2):
		return False

	for digit in num_str1:
		if not digit in num_str2:
			return False
	for digit in num_str2:
		if not digit in num_str1:
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

def prime_multiplicity(num, prime):
	multip = 0
	while True:
		if num % prime**(multip+1) != 0:
			break
		multip += 1
	return multip

trigger = True

mList = []
sList = []

mSum = 0
count = 0
largest = [0,0]
smallest = 0
bigNum = 10**7
largestPrime = bigNum
# so ceil(sqrt(bigNum)) mistakenly adds 2 nums
n = 8
flag = True
a = 1
b = 1
allCombins = {}  # protected
factSums = [-1 for _ in range(2540160)]  # protected

Sieve = makeSieve(largestPrime+1)
Primes = [potential for potential in range(largestPrime) if Sieve[potential]]

def eulerPhi(num, sieve, primes):
	if sieve[num]:
		return num-1
	totient = num
	primeProd = 1
	for p in primes:
		if p >= sqrt(num):
			break
		if num%p == 0:
			primeProd *= p**prime_multiplicity(num, p)
			totient -= totient//p
	largePrime = num // primeProd
	if largePrime == 1:
		return totient
	# totient -= (primeProd*totient)//num
	totient *= 1 - 1 / (num / primeProd)
	return totient
		

if __name__ == '__main__':
	startTime = time()
	print("started")
	# print(primes)
	# 62716
	# someNum = 87109
	for i in range(1,10**6):
		phi = eulerPhi(i, Sieve, Primes)
		if is_permuted(i, phi):
			ratio = i/phi
			if ratio > largest[0]:
				largest[1] = i
	print(largest[1])
	# print(i, i/phi)

	# for i in range(7):
	# # i = 5 # i != 2
	# 	print(7**i,eulerPhi(7**i, Sieve, Primes))

	# print(eulerPhi(someNum))

	print("done")
	print('This took', time() - startTime)

