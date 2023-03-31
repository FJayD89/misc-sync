a = int(input('Poprosím rozmer šachovnice:\n'))
b = int(input('Aj veľkosť štvorčeka:\n'))

sach = []

def makeLine(start):
	outList = []
	[outList.append((' ' if i%2 == start else '*')*b) for i in range(a)]
	outLine = ''
	for seg in outList:
		outLine += seg
	return outLine


for rowIndex in range(a):
	[sach.append(makeLine(rowIndex%2)) for _ in range(b)]
	
[print(line) for line in sach]