f = open('adventText.txt')
lines = f.read().split('\n')
lines = [line.split(' ') for line in lines]
playVal = {
	'A':1,
	'B':2,
	'C':3,
	'X':1,
	'Y':2,
	'Z':3
}

winVal = {
	0:6,
	1:0,
	2:3
}

mSum = 0

for line in lines:
	p1 = playVal[line[0]]
	p2 = playVal[line[1]]
	score = p2 + winVal[(p2 - p1 + 2) % 3]
	mSum += score
print(mSum)

# 1, -2 TRUE
# 0 Draw
# -1, 2 False
# if +2
# 3, 0 TRUE mod3 = 0
# 2 Draw mod3 = 2
# 1, 4 False mod3 = 1