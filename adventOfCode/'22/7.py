

f = open('adventText.txt')
lines = f.read().split('\n')
currentDirName = '/'
currentPos = []
directories = {'/':{}}
dirSizes = {'/':0}


def locate(dirSequence, dirDictTree):
	tempDir = dirDictTree
	for dirName in dirSequence:
		tempDir = tempDir[dirName]
	return tempDir


listing = False

sumFileSize = 0

for line in lines:
	if line[0] == '$':
		# if listing:
		# 	dirSizes[currentDirName] = sumFileSize
		# 	sumFileSize = 0
		# 	listing = False
		cmd = line[2:4]
		if cmd == 'cd':
			if line[5:7] == '..':
				currentPos.pop()
				continue
			
			currentDirName = line[5:]
			currentPos.append(currentDirName)
		if cmd == 'ls':
			listing = True
		continue
	if line[0:3] == 'dir':
		dirName = line[4:]
		locate(currentPos, directories)[dirName] = {}
		dirSizes[dirName] = 0
		continue
	# must be a file
	fileInfo = line.split(' ')
	fileSize = int(fileInfo[0])
	dirSizes[currentDirName] += fileSize


def recurse(mDir):
	for dirName in mDir.keys():
		for subDirName in mDir[dirName]:
			recurse(mDir[dirName])
			dirSizes[dirName] += dirSizes[subDirName]

recurse(directories['/'])

for dirName in directories['/'].keys():
	dirSizes['/'] += dirSizes[dirName]

print(directories)
print(dirSizes)

sizeSum = 0

for dirSize in dirSizes.values():
	if dirSize <= 100000:
		sizeSum += dirSize

print(sizeSum)