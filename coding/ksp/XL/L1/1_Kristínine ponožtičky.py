stepCount = int(input())

steps = []

for _ in range(stepCount):
	line = input().split(' ')
	step = [int(stepHalf) for stepHalf in line]
	steps.append(step)

dirtSum = [0,0]

for firstStep in [0,1]:
	foot = firstStep
	for step in steps:
		dirtSum[firstStep] += step[foot]
		foot = 1 - foot

if dirtSum[0] == dirtSum[1]:
	print("je to jedno")

if dirtSum[0] > dirtSum[1]:
	print("prava")

if dirtSum[0] < dirtSum[1]:
	print("lava")