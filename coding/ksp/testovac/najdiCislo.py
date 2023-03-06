# bin search
# from math import floor, ceil



lol = input()
numList = input().split(' ')
numList = [int(num) for num in numList]
n = int(input())



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
    

for i in range(n):
    q = int(input())
    if binSearch(q) == -1:
        if binSearch(-q) == -1:
            print('N')
            continue
    print('A')


# [1 2 3 4 5]
# bS(4,0,4)
# mid = 2
# 4 >= 3
# ret bS(4,2,4)
# mid = 3
# 4 >= 4
# ret bS(4,3,4)
# mid = 3
# 4 >= 4
# ret bS(8, [8], 7)
# len([8]) == 1
# [8][0] == 8
# ret 7
