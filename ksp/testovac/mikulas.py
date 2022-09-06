# mikulas

inp = input().split(' ')
n = int(inp[0])
p = int(inp[1])

zasluhy = input().split(' ')
zasluhy = [int(num) for num in zasluhy]
numList = []

def binSearch(x, start = 0, end = len(numList)-1):
    
    if start == end:
        if numList[start] == x:
            return start
        return -1
    n = end-start
    mid = start + n//2
    
    
    if x <= numList[mid]:
        return binSearch(x, start, mid)
        
    if x > numList[mid]:
        return binSearch(x, mid+1, end)

flag = True

rewards = list(zasluhy)
najZasluznejsi = 0
ans = ''
while sum(rewards) != p:
    if sum(rewards) < p:
        ans = 'Nic nedostanete'
        break
    najZasluznejsi = 0
    zasluzni = []
    for i in range(len(zasluhy)):
        if rewards[i] > rewards[najZasluznejsi]:
            najZasluznejsi = i
            zasluzni = []
        if rewards[i] == rewards[najZasluznejsi]:
            zasluzni.append(i)
    for z in zasluzni[:sum(rewards)-p]:
        rewards[z] -= 1
#   print(rewards)

if ans == '':
    ans = rewards[zasluzni[-1]]

print (ans)
