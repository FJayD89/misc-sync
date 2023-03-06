# eratostenes
from math import floor, sqrt, log, ceil

inp = input().split(' ')
L = int(inp[0])
R = int(inp[1])

# sitko az po sqrt10^6 = 10^3

k = ceil(log(R, 10))


primeList = [True for i in range(ceil(10**k) + 1)]
primeList[0] = False
primeList[1] = False

for i in range(2,ceil(10**(k//2)) + 1):
    if primeList[i]:
        if L < 2*i:
            L = 2*i
        else:
            L = i*(L//i)
        for j in range(L,ceil(10**k) + 1,i):
            primeList[j] = False

print(primeList)

for i in range(L, R+1):
    if primeList[i]:
        print(i)

# mas pole true
# prechadzas nim az po sqrt(len)
# ak je prime, zmen vsetky jeho nasobky L <= n <= R na False
# tym padom to trva bud sqrt(len)
# alebo 
