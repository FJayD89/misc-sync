f = open('AoC.txt')
rucksacks = f.read().split('\n')
# rucksacks = [[rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]] for rucksack in rucksacks]
rucksacks = [rucksacks[i:i+3] for i in range(len(rucksacks) // 3)]
print(rucksacks)
def priority(itemType):
	typeId = ord(itemType)
	if typeId < 97:
		return typeId-38
	return typeId-96


prioritySum = 0

# for rucksack in rucksacks:
# 	for char in rucksack[1]:
# 		if char in rucksack[0]:
# 			prioritySum += priority(char)
# 			break

for rucksackTriple in rucksacks:
	for itemType in rucksackTriple[0]:
		if itemType in rucksackTriple[1]:
			if itemType in rucksackTriple[2]:
				prioritySum += priority(itemType)


print(prioritySum)