f = open('adventText.txt')
lines = f.read().split('\n')

top3 = [0,0,0]
mSum = 0
for line in lines:
	if line == '':
		if not mSum > top3[2]:
			mSum = 0
			continue
		top3[2] = mSum
			
		if not mSum > top3[1]:
			mSum = 0
			continue
		top3[2], top3[1] = top3[1], mSum
		
		if not mSum > top3[0]:
			mSum = 0
			continue
		top3[1], top3[0] = top3[0], mSum
		
		mSum = 0
		continue
	mSum += int(line)
print(sum(top3))
	