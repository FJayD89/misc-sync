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

if __name__ == "__main__":
	from time import time
	startTime = time()
	sieve = makeSieve(10**7)
	# primeList = []
	# for num in range(10**7):
	# 	if sieve[num]:
	# 		primeList.append(num)
	# print(primeList)

	print("done")
	print('This took', time() - startTime)