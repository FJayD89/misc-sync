f = open('adventText.txt')
lines = f.read().split('\n')
lines = [line.split(' ') for line in lines]
playVal = {
	'A':0,
	'B':1,
	'C':2,
	'X':-1,
	'Y':0,
	'Z':1
}

winVal = {
	0:0,
	1:3,
	2:6
}

mSum = 0

for line in lines:
	p1 = playVal[line[0]]
	p2 = playVal[line[1]]
	score1 = 0
	score2 = 1 + (p2+p1)%3 + winVal[p2 + 1]
	mSum += score2
print(mSum)

# 1, -2 TRUE
# 0 Draw
# -1, 2 False
# if +2
# 3, 0 TRUE mod3 = 0
# 2 Draw mod3 = 2
# 1, 4 False mod3 = 1