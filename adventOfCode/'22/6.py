def areUnique(lst):
	for index in range(len(lst)):
		val = lst[index]
		if val in lst[index+1:]:
			return False
	return True

f = open('adventText.txt')
buffer = f.read()
# markerLength = 4  # Part I
markerLength = 14  # Part II
readIndex = markerLength-1
while True:
	readChar = buffer[readIndex]
	
	if areUnique(buffer[readIndex-markerLength+1:readIndex+1]):
		print(readIndex +1)
		break

	readIndex += 1

