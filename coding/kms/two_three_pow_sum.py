def isSimple(x):
	varX = x
	exp = [0,0]
	while varX % 2 == 0:
		exp[0] += 1
		varX /= 2
	while varX % 3 == 0:
		exp[1] += 1
		varX /= 3
	if varX == 1:
		return exp
	return False

def isSumLegit(current_sum, added):
	# deduce future placement
	if not current_sum:
		return 0  # this is the actual index to be used

	maxIndex =  len(current_sum)
	newIndex = 0
	while added[0] > current_sum[newIndex][0]:
		if added[0] == current_sum[newIndex][0]:
			return -1
		newIndex += 1
		if newIndex == maxIndex:
			if added[1] < current_sum[maxIndex - 1][1]:
				return newIndex
			return -1

	if current_sum[newIndex][0] == added[0]:  # liable
		return -1

	threeExpUpperLimit = added[1]+1
	if newIndex != 0:
		threeExpUpperLimit = current_sum[newIndex-1][1]
	threeExpLowerLimit = -1
	if newIndex != maxIndex:
		threeExpLowerLimit = current_sum[newIndex][1]

	if not threeExpLowerLimit < added[1] < threeExpUpperLimit:
		return -1
	return newIndex

def islComplex(current_sum, added_list):
	dynSum = current_sum
	for item in added_list:
		newIndex = isSumLegit(dynSum, item)
		if newIndex == -1:
			return False
		dynSum = addToSum(dynSum, item, newIndex)
	return dynSum

def addToSum(old_sum, added, new_index):
	newSum = old_sum[:new_index]
	newSum.append(added)
	newSum += old_sum[new_index:]
	return newSum

sumList = []

def build_num(goal, min_num, sum_so_far):
	global sumList
	"""
	take the start_total, add the next sums, if possible
	"""
	sum_sum = sum([2**elem[0] * 3**elem[1] for elem in sum_so_far])
	if sum_sum == goal:
		return sum_so_far

	if sum_sum + min_num+1 > goal:
		return -1

	for i in range(min_num, len(sumList)):
		TBA = sumList[i]
		newSum = islComplex(sum_so_far, TBA)
		if not newSum:
			continue

		res = build_num(goal, i+1, newSum)
		if res != -1:
			# if min_num == 1:
			# 	print(goal, "can be written as", res)
			# 	continue
			# 	pass

			return res
	return -1

def format_num_list(n_list):
	betterList = [2 ** elem[0] * 3 ** elem[1] for elem in n_list]
	formatted = ''
	for sum_num in betterList[:-1]:
		formatted += str(sum_num) + ' + '
	formatted += str(betterList[-1])
	return formatted

for num in range(1,50):
	# fix 14
	simplified = isSimple(num)
	if simplified:
		sumList.append([simplified])
		print(num, '->', sumList[num-1])
		continue
	# else:
	sumList.append(build_num(num, 1, []))
	print(num, '->', sumList[num-1], '=', format_num_list(sumList[num-1]))

# print(sumList)

# csum = [[0,2], [2,1]]
# print(isSumLegit(csum, [0,3]))