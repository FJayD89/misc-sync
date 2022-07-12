# otocenie

sqr = []
a = int(input())

for i in range(a):
    line = input().split(' ')
    line = [int(num) for num in line]
    sqr.append(line)

sqr2 = []
for i in range(a):
    sqr2.append([])
    for j in range(a):
        sqr2[i].append(sqr[j][(a-1)-i])
        
for i in range(a):
    out = ''
    for j in sqr2[i][:-1]:
        out += str(j) + ' '
    out += str(sqr2[i][-1])
    print(out)

# ok
# [0,1] z [1,2]
# [2,2] z [2,0]
