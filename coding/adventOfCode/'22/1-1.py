f = open('adventText.txt')
lines = f.read().split('\n')

largest = 0
mSum = 0
for line in lines:
	if line == '':
		if mSum > largest:
			largest = mSum
		mSum = 0
		continue
	mSum+= int(line)
print(largest)
	