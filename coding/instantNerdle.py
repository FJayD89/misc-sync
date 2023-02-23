OG = [3,8,7,2,1,6]
doubles = [0,0]
for i in range(6):
	numbers = list(OG)
	single = numbers.pop(i)

	for j in range(5):
		doubles[0] = numbers.pop(j)
		for k in range(4):
			doubles[1] = numbers.pop(k)
			num = single*(10*doubles[0]+doubles[1])
			if len(str(num)) != 3:
				numbers.append(doubles[1])
				continue
			flag = True
			for digit in str(num):
				if int(digit) not in numbers:
					flag = False
					break
			if flag:
				print(single, ',', doubles, num)
			numbers.append(doubles[1])
		numbers.append(doubles[0])
	numbers.append(single)
