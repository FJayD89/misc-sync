# factorisation
from math import sqrt, floor

n = int(input())

def factors(x):
    facts = []
    for i in range(2,floor(sqrt(x))+1):
        if x % i == 0:
            facts.append(i)
            for fact in factors(x/i):
                facts.append(fact)
                
            return facts

    return [int(x)]

def outP(lst):
    if not lst:
        print('')
        return
    out = str(lst[0])
    for num in lst[1:]:
        out += ' x ' + str(num)
    return out

for i in range(n):
    inp = input()
    print(inp, '=', outP(factors(int(inp))))
