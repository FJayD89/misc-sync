from math import sqrt, floor, ceil, factorial, log10
from time import time
from itertools import permutations, product
from mathReplace import mathReplace
from projectEuler import makeSieve


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

def dupeFree(str):
	found = []
	for char in str:
		if char in found:
			return False
		found.append(char)
	return True

def fastDupeFree(str):
	return len(set(str)) == len(str)

startTime = time()

# primeSieve = makeSieve(10**8)
# print('Sieve setup done')

for i in range(1,100):
	for j in range(10 ** 3, 10 ** 4):
		if fastDupeFree(str(j)):
			pass
			print(j)

print("done")
print('This took', time()-startTime)