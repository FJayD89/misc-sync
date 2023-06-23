init = [int(num) for num in input().split(' ')]
islandCount = init[0]
queryCount = init[1]
archipelagae = [{i} for i in range(islandCount)]
color = [i for i in range(islandCount)]
archipelagos = [{i} for i in range(islandCount)]
archSpecialCount = [0 for i in range(islandCount)]
# references
# indexes represent islands
# if the reference is >=0, it's pointing to another island
# if negative, do -x-1, that's the # of specials connected to it
ref = [i for i in range(islandCount)]




def mergeArches(a,b):


	archA = color[a]
	archB = color[b]
	for island in archipelagos[archB]:
		color[island] = archA

	archipelagos[archA].update(archipelagos[archB])

	archSpecialCount[archA] += isSpecial[a] + isSpecial[b]
	if archA != archB:
		archSpecialCount[archA] += archSpecialCount[archB]


def makeBridge(a,b):
	global isSpecial
	mergeArches(a, b)
	for island in [a,b]:
		if isSpecial[island] == 1:
			isSpecial[island] = -1
			continue
		if isSpecial[island] == 0:
			continue
			
		isSpecial[island] += 1
	


def countSpecials(island):
	print(archSpecialCount[color[island]])


def parseLine(line):
	args = line.split(' ')
	cmd = args[0]
	if cmd == '!':
		makeBridge(int(args[1]), int(args[2]))
	if cmd == '?':
		countSpecials(int(args[1]))


isSpecial = [1 for _ in range(islandCount)]  # 0 = isolated, 1 = special, 2 = not special

for _ in range(queryCount):
	parseLine(input())