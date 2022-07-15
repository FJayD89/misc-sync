# GCD

n = int(input())

def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        a,b = b,a
    return gcd(b, a % b)
        

for i in range(n):
    x = [int(num) for num in input().split()]
    out = gcd(x[0], x[1])
    print(out)
