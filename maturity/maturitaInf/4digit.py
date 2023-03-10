def dupeFree(str):
	found = []
	for char in str:
		if char in found:
			return False
		found.append(char)
	return True


for i in range(10**3, 10**4):
	if dupeFree(str(i)):
		print(i)