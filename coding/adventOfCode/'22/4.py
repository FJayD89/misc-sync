f = open('adventText.txt')
rangePairs = f.read().split('\n')
rangePairs = [[[int(sectionEdge)
				for sectionEdge in section.split('-')]
					for section in pair.split(',')]
						for pair in rangePairs]
# print(rangePairs)
contained = 0
for pair in rangePairs:
	sec1 = pair[0]
	sec2 = pair[1]
	# if (sec1[0] == sec2[0]) or (sec1[1] == sec2[1]) or ( (sec1[0] < sec2[0]) == (sec1[1] > sec2[1])):  # Part I
	if min(sec1[1], sec2[1]) >= sec2[0] and min(sec1[1], sec2[1]) >= sec1[0]: # Part II
		contained += 1

print(contained)
