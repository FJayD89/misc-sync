# primes
from math import sqrt, floor

primes = []

n = int(input())

def isPrime(x):
    if x == 1:
        return 'NIE'
    if x == 2:
        return 'ANO'
    if x % 2 == 0:
        return 'NIE'
    for i in range(3,floor(sqrt(x))+1,2):
        if x % i == 0:
            return 'NIE'
    return 'ANO'

for i in range(n):
    print(isPrime(int(input())))
