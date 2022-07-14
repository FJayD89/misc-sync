# poriadok

n = int(input())
toys = input().split(' ')
toys = [int(size) for size in toys]

ans = ''
zostupne = ''

for i in range(1,n):
    if toys[i] == toys[i-1]:
        continue
    if zostupne == '':
        if toys[i] > toys[i-1]:
            zostupne = False
            continue
        zostupne = True
        continue
    if zostupne != (toys[i] < toys[i-1]):
        ans = 'bordel'
        break
if ans == '':
    ans = 'poriadok'

print(ans)
