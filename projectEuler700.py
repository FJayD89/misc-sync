from math import sqrt, floor, ceil, factorial, comb
from time import time
from itertools import permutations


def zeroEval(numStr):
    if numStr[0] == '0':
        return zeroEval(numStr[1:])
    return int(numStr)


f = open('eulerText.txt')
lines = f.read().split('\n')
attempts = [int(attempt) for attempt in lines]
# lines = [line.split(' ') for line in lines]
# lines = [[zeroEval(numStr) for numStr in line] for line in lines]


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

trigger = True
mList = []
mSum = 1517926517219802
count = 0
largest = 0
smallest = 10827725432
n = 10543898410+283827021

startTime = time()
# 1517926306270940 1745260759
# 283827021
# while True:
#     seq = (n*1504170715041707) % 4503599627370517
#     if seq < smallest:
#         smallest = seq
#         mSum += seq
#         print(mSum, n)
#     n += 1

# 1517926517477964



print(count)



print('This took', time()-startTime)