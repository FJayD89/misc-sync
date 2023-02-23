from primeSieve import makeSieve
from math import log2, floor

# for(let myIterator = 0; myIterator <= 19; myIterator++){
#     i = (2**myIterator -1)%19;
#     ret = 0;
#     if (i == 0){
#         ret = 1;
#     }
#     nums[myIterator] += ret;
# }

sieve = makeSieve(10**6)
primes = []

for num in range(len(sieve)):
	if sieve[num]:
		primes.append(num)

upLimit = floor(log2(10**6 -1))
advNums = [0 for i in range(upLimit)]

for prime in primes:
	for i in range(1,upLimit+1):
		if (2**i -1)%prime == 0:
			advNums[i - 1] += 1
			if (2 ** i - 1) % prime**2 == 0:
				advNums[i - 1] += 1
print(advNums)

advSum = 0

for index in range(upLimit):
	if advNums[index] == 2:
		advSum += 2**(index+1) -1
print(advSum)
