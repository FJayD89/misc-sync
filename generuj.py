# generuj

chars = [chr(num) for num in range(65, 65+26)]
# print(chars)

inp = input().split(' ')
n = int(inp[0])
k = int(inp[1])

strList = []

def makeString(mStr):
    if len(mStr) == n:
        strList.append(mStr)
        return
    for char in chars:
        makeString(mStr+char)
    
chars = chars[:k]
makeString('')
for retaz in strList:
    print(retaz)
