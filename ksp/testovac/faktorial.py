# faktorial

from math import log, ceil, floor

def factorial(x):
    if x == 1:
        return 1
    return factorial(x-1)*x

def zerosInFact(x):
    zeros = 0

    log5 = floor(log(num,5))+1
    for i in range(1,log5):
        zeros += num // 5**i
    return zeros

num = int(input())

fives = num
log5 = floor(log(num,5))

# print(log5)

for i in range(1,log5+1):
    fives -= num // 5**i
    
# print(fives)
print(zerosInFact(num))

# zeros = 0

# log5 = floor(log(num,5))+1
# for i in range(1,log5):
#     zeros += num // 5**i
# print(zeros)
# print(factorial(num))

# num = 5, expected result 5
# log5 = 0
#


# num = 6, expected result 5
# log5 = 1
#

# unm = 9 expected 8

