amount = int(input())
ranges = []
colWidths = []
for i in range(amount):
	ranges.append([int(time) for time in input().split(' ')])
	colWidths.append(1)
print(ranges)


def overlap(range1, range2):
	return list(range(range2[0], range1[1]+1))


for index, mRange in enumerate(ranges[:-1]):
	for nRange in ranges[index+1:]:
		dynOverlap = overlap(mRange, nRange)
		if not dynOverlap:
			break
		colWidths[index] += 1

print(overlap(ranges[0], ranges[1]))
print(colWidths)
