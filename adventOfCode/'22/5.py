f = open('adventText.txt')
lines = f.read().split('\n')
lineIndex = 0
line = lines[lineIndex]
setupEnd = 0
for line in lines:
	if line[:2] == ' 1':
		break
	setupEnd += 1
	
print(setupEnd)

stacksDiagram = list(reversed(lines[:setupEnd]))

stackCount = (len(stacksDiagram[0])-3)//4 + 1

stacks = [[] for i in range(stackCount)]

print(stackCount)

for line in stacksDiagram:
	lastStack = (len(line)-3)//4 + 1
	for i in range(lastStack):
		crate = line[1+4*i]
		if crate != ' ':
			stacks[i].append(crate)
			
	# print(line)
for stack in stacks:
	print(stack)

instructions = lines[setupEnd+2:]
instructions = [instruction.split(' ') for instruction in instructions]
instructions = [[int(instruction[i]) for i in [1,3,5]] for instruction in instructions]

for instruction in instructions:
	crateCount = instruction[0]
	origin = instruction[1]-1
	destination = instruction[2]-1
	#  Part I
	# for i in range(crateCount):
	# 	stacks[destination].append(stacks[origin].pop())
	
	#  Part II
	stacks[destination] += stacks[origin][-crateCount:]
	stacks[origin] = stacks[origin][:-crateCount]
	
	

print(instructions)

topCrates = ''

for stack in stacks:
	print(stack)
	topCrates += stack[-1]

print(topCrates)