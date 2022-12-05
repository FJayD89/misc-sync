from math import copysign

f = open('infiAoC.txt')
lines = f.read().split('\n')
lines = [line.split(' ') for line in lines]

turns = {
	0: [0,1],
	45: [1,1],
	90: [1,0],
	135: [1,-1],
	180: [0,-1]
}

direction = 180
pos = [0,0]
for line in lines:
	cmd = line[0]
	magnitude = int(line[1])
	if cmd == 'spring' or cmd == 'loop':
		# if cmd == 'loop':
		# 	magnitude *= 2
		pos[0] +=  magnitude * copysign(turns[abs(direction-180)][0], direction)
		pos[1] += magnitude * turns[abs(direction-180)][1]
		continue
	if cmd == 'draai':
		direction = (direction+magnitude)%360
		

print(sum([abs(pos[0]), abs(pos[1])]))
	