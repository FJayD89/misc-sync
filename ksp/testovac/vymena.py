# vymena

dims = input().split(' ')

a = int(dims[0])
b = int(dims[1])

rect = []

for i in range(a):
    line = input().split(' ')
    line = [int(num) for num in line]
    rect.append(line)

# for i in range(a):
#     print(rect[i])

for i in range(b):
    
    j = 0
    out = ''
    while j < a-1:
        out += str(rect[j][i]) + ' '
        j += 1
    out += str(rect[j][i])
    print(out)
