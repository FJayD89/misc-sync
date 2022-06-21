from math import sqrt, floor, ceil, factorial
from time import time
from itertools import permutations, product


def zeroEval(numStr):
    if numStr[0] == '0':
        return zeroEval(numStr[1:])
    return int(numStr)


f = open('eulerText.txt')
nums = f.read().split(',')
nums = [int(num) for num in nums]
# nums = [int(attempt) for attempt in lines]
# lines = [line.split(' ') for line in lines]
# lines = [[zeroEval(numStr) for numStr in line] for line in lines]


def decode(cipherNums, key):
    # cN[i] = pN[i]^k[i mod keyLen]

    plainNums = ""
    keyLen = len(key)
    keyIndex = 0
    for num in cipherNums:
        binNum = int(bin(num), 2)
        modKeyIndex = keyIndex % keyLen
        binKey = int(bin(key[modKeyIndex]), 2)
        plainNum = binNum ^ binKey
        if not (32 <= plainNum <= 57 or 65 <= plainNum <= 90 or 97 <= plainNum <= 122) : # if decodes to a control char
            keyPossibilities[modKeyIndex].remove(key[modKeyIndex]) # remove part of key from possibilities
            return ['fail', modKeyIndex]
        plainNums += chr(plainNum)
        keyIndex += 1
    return plainNums


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


trigger = True

mList = []

mSum = 0
count = 0
largest = 0
smallest = 0
n = 1

startTime = time()

# print(sqareSum(9999999)
keyPossibilities = []
for i in range(3):
    keyPossibilities.append(list(range(97,124)))

possibleKey = [0,0,0]


def main():
    global trigger
    if not trigger:
        return ''
    for possibleKey[0] in keyPossibilities[0]:
        for possibleKey[1] in keyPossibilities[1]:
            for possibleKey[2] in keyPossibilities[2]:
                decoded = decode(nums, possibleKey)
                if decoded[0] == 'fail':
                    main()
                    trigger = False
                print(possibleKey, '→', decoded)
# print(count)
# print(nums)
# print( int(bin(107),2) ^ int(bin(42),2))

# chr(a), 32 <= a <= 126

# print(keyPossibilities)

# print(decode(nums, [111,111,97]))

print('This took', time()-startTime)