init = [int(num) for num in input().split(' ')]
islandCount = init[0]
queryCount = init[1]
archipelagae = [{i} for i in range(islandCount)]

def mergeArches(a,b):
	for island in archipelagae[a]:
		archipelagae[b].append(island)
	for island in archipelagae[b]:
		archipelagae[a].append(island)

def makeBridge(a,b):
	for island in [a,b]:
		if isSpecial[island] == 2:
			continue
		isSpecial[island] += 1

def countSpecials(island):
	score = 0
	if isSpecial[island] == 0:
		score = 0
	print(score)

def parseLine(line):
	args = line.split(' ')
	cmd = args[0]
	if cmd == '!':
		makeBridge(int(args[1]), int(args[2]))
	if cmd == '?':
		countSpecials(int(args[1]))

isSpecial = [0 for _ in range(islandCount)]  # 0 = isolated, 1 = special, 2 = not special

for _ in range(queryCount):
	parseLine(input())