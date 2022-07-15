# mod exp
from math import log, ceil

n = int(input())

def modExp(a, b, c):
    prod = 1
    d = 0
    while True:
        if prod == 0:
            break
        l = ceil(log(c,a) - log(prod,a))
        # print('l =', l)
        if d+l > b:
            break
        prod *= a ** l
        # print('prod =', prod)
        prod %= c

        # print('prodMod =', prod)
        d += l 

    prod *= a**(b-d)
    prod %= c
    
    return prod
        

for i in range(n):
    x = [int(num) for num in input().split()]
    out = modExp(*x)
    print(out)

