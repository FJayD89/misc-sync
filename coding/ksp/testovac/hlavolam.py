inp = input().split(' ')
n = int(inp[0])
k = int(inp[1])
symbols = []
for i in range(k):
    symbols.append(int(input()))

symbols.sort()
symbols.reverse()

# print(symbols)
stacked = []
for i in range(k):
    stacked.append(symbols[i])
print('least stacked =', stacked[-1])
removeLayer = list(symbols)


for i in range(n,0,-1):
    flag = True
    useful = []
    symbols = list(removeLayer)
    while symbols[-1] >= i and flag:
        for j in range(k):
            if symbols[j] >= i:
                useful.append(k)
                symbols[j] -= i
                print('len before check is', len(useful))
                if len(useful) == n:
                    print('broke')
                    flag = False
                    break
    print('useful =', useful)
print('ended')
            

# print(removeLayer)
