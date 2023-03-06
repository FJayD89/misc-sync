from primeSieve import makeSieve
from time import time

def coprimes(primesList, allPrimes):
	primes = [allPrimes[i] for i in range(len(primesList)) if primesList[i] == 1]
	cpList = [int(i%primes[0]!=0) for i in range(1,primes[0]+1)]
	for p in primes[1:]:
		cpList = [cpList[i%len(cpList)] * int((i+1)%p!=0) for i in range(p*len(cpList))]
	# a,b are primes for now
	# mList = [int(i%a!=0 and i%b!=0) for i in range(a*b)]
	return cpList


def binPELToInt(binPEL):
	out = 0
	for bit in binPEL:
		out = (out << 1) | bit
	return out

def conjecture3Prod(sieve, primeCount):
	kSum = 0
	for i in range(primeCount):
		for j in range(i):
			for l in range(j):
				kSum = sum(coprimes([int(k == i or k == j or  k == l) for k in range(i+1)],primeList))
				kProd = (primeList[i]-1)*(primeList[j]-1)*(primeList[l]-1)
				# if mSum != mProd:
				
				print(primeList[i], 'and', primeList[j],'and', primeList[l], '->', mSum, ',', mProd)

bigNum = 10**6+1
# 10**6+1 -> 303963552391
# 10**5+1 -> 3039650753
# 10**4+1 -> 30397485
# 10**3+1 -> 1196061
# 962 892800


if __name__ == '__main__':
	startTime = time()
	
	primeExpList = [[] for i in range(bigNum)]
	cpCounts = [1 for i in range(bigNum)]
	
	sieve = makeSieve(bigNum)
	primeList = []
	for num in range(bigNum):
		if sieve[num]:
			primeList.append(num)
	# case for p = 2 is separate
	a = 1
	while 4 * a < bigNum:
		x = 4*a
		while x % 4 == 0:
			cpCounts[4 * a] *= 2
			x /= 2
		a+=1
		
	for i in range(1,len(primeList)):
		p = primeList[i]
		a = 1
		while p * a < bigNum:
			
			# padLength = i + 1 - len(primeExpList[p * a])
			# for j in range(padLength):
			# 	primeExpList[p * a].append(0)
			#
			# primeExpList[p * a][-1] = 1
			# if len(primeExpList[a]) >= i + 1:
			# 	primeExpList[p * a][-1] = primeExpList[a][i] + 1
			
			cpCounts[p * a]*=(p-1)
			x = int(a)
			while x%p == 0:
				cpCounts[p * a] *= p
				x = x / p

			a += 1
	

	# print(sum(coprimes([1,1],primeList)))
	# print(primeExpList[998])
	# print(primeExpList)
	print(cpCounts)
	print(sum(cpCounts[2:]))
	# print((primeList[99]*primeList[98]))
	print("done")
	print('This took', time() - startTime)