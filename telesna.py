# telesna

n = int(input())
numsA = input().split(' ')
numsA = [int(num) for num in numsA]

m = int(input())
numsB = input().split(' ')
numsB = [int(num) for num in numsB]

out = ''

a = 0
b = 0

if numsA[a] < numsB[b]:
    out += str(numsA[a])
    a += 1
else:
    out += str(numsB[b])
    b += 1


while not (a == n or b == m):
    out += ' '
    # print('using ', a, b)
    if numsAd[a] < numsB[b]:
        out += str(numsA[a])
        a += 1
        # print(out)
        continue
    out += str(numsB[b])
    b += 1
    # print(out)

for num in numsA[a:]:
    out += ' ' + str(num)

for num in numsB[b:]:
    out += ' ' + str(num)

print(out)
