length = int(input())
rad = input()

vCount = 0
tCount = 0

newRad = str(rad)
equalizer = 0
added = 0
for charIndex in range(length):
	char = newRad[charIndex+added]
	
	if char == 'V':
		# vCount += 1
		equalizer += 1
		continue
	# tCount += 1
	equalizer -= 1
	if equalizer < 0:
		newRad = newRad[:charIndex] + 'V' + newRad[charIndex:]
		equalizer += 1
		added += 1

for _ in range(equalizer):
	newRad += 'T'
	
newLength = len(newRad)
added = 0
equalizer = 0
for charIndex in range(newLength-1, -1, -1):
	char = newRad[charIndex-added]
	if char == 'V':
		# vCount += 1
		equalizer -= 1
		continue
	# tCount += 1
	equalizer += 1  # bola videna Torta
	if equalizer < 0:
		added += 1
		equalizer += 1
		if charIndex == newLength -1: # can only happen on rightmost char, so length won't have canged here yet
			newRad += 'T'
			continue
		newRad = newRad[:charIndex+1] + 'T' + newRad[charIndex+1:]

prepend = ''
for _ in range(equalizer):
	prepend += 'V'
	
newRad = prepend + newRad

# print(rad)
print(newRad)


