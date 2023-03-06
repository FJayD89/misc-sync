# mergSort

n = int(input())
nums = input().split(' ')
nums = [int(num) for num in nums]

def merge(numsA, numsB):
    merged = []
    a = 0
    b = 0

    while not (a == len(numsA) or b == len(numsB)):
        if numsA[a] < numsB[b]:
            merged.append(numsA[a])
            a += 1
            continue
        merged.append(numsB[b])
        b += 1
    
    for num in numsA[a:]:
        merged.append(num)

    for num in numsB[b:]:
        merged.append(num)
        
    return merged


def outP(lst):
    out = str(lst[0])
    for num in lst[1:]:
        out += ' ' + str(num)
    print(out)

def doSplit(lst):
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]

    mid = len(lst) // 2
    return merge(doSplit(lst[:mid]), doSplit(lst[mid:]))

outP(doSplit(nums))

