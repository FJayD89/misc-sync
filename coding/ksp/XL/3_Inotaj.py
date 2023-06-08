init = [int(num) for num in input().split(' ')]
iCount = init[0]
maxLen = init[1]

inotaje = []

def allTuples(max_len, so_far):
	if len(so_far) == max_len:
		return so_far
	toAdd = []
	for comb in so_far:
		add = comb
		add.append(True)
		notAdd = comb
		notAdd.append(False)
		toAdd.append(add)
		toAdd.append(notAdd)
	return


for _ in range(iCount):
	inotaje.append(input())

for inotajLen in range(maxLen):


print(inotaje)