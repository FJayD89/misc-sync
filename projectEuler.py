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

bigFibSums = []


def S(x):
    # x is the index of the wanted fib num
    sSum = 0
    for i in range(1,x+1):
        sSum += ss[i]
        sSum %= bigNum
    return sSum


def s(x):
    mod = 1
    pain = x//9

    for index, d in enumerate(str(pain)):
        pow = len(str(pain)) - index - 1
        d = int(d)
        mod *= mod10pow10(pow, d, bigNum)
        mod = mod % bigNum

    multi = (1 + x - 9 * pain) % bigNum

    mod = (mod * multi - 1) % bigNum  # and THIS is s(f(90))

    return mod


def mod10pow10(p, c, m):
    # 10^(10^p)*c mod m, c < 10
    X = 10
    for i in range(p):
        X = X**10 % m
    return X**c % m


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

trigger = True

mList = []

mSum = 0
count = 0
largest = 0
smallest = 0
n = 1
flag = -1

startTime = time()

fib = [0,1]

bigNum = 1000000007

for i in range(88):
    fib.append(fib[-1] + fib[-2])

# ss = [s(f) for f in fib] # s(0), s(1), s(1), s(2), ...
# SS = [S(f) for f in fib] # S(0), S(1), S(1), S(2)


# print(bigSum(fib[23]) % bigNum)

# for i in range(2,91):
#     mSum += bigSum(fib[i]) % bigNum

# print(fib[89])
# print(floor(fib[89]/9))

# pain = floor(fib[89]/9)
# p = 1.97775490667190
# rem = 464*10**(-17)
# X = 10
# mod = 1

# for index, d in enumerate(str(pain)):
#     pow = len(str(pain)) - index - 1
#     d = int(d)
#     mod *= mod10pow10(pow, d, bigNum)
#     mod = mod%bigNum
#
#
#
# print(mod) # 10^pain mod bN
#
# multi = (1+fib[89]+9*pain) % bigNum
#
# mod = (mod*multi)%bigNum  # and THIS is s(f(90))
#
# print(mod)




print(mod10pow10(0, 5, bigNum))
print(s(fib[89]))
# print(S(50))


print('This took', time()-startTime)