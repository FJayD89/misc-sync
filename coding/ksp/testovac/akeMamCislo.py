# ake mam cislo

inp = input().split(' ')
a = int(inp[0])
b = int(inp[1])
n = int(inp[2])

def customFib(a,b,n):
    for i in range(n-2):
        a,b = b,a+b
    return b

print(customFib(a,b,n))
