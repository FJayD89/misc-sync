from math import sqrt, ceil

def makeSieve(sieveSize):
	sieve = [True for i in range(sieveSize)]
	sieve[0] = False
	sieve[1] = False

	# declare all multiples of two nonprime
	for composite in range(4, sieveSize, 2):
		sieve[composite] = False

	for num in range(3, int(sqrt(sieveSize))):
		# print(num)
		if not sieve[num]:
			continue
		for composite in range(num ** 2, sieveSize, 2 * num):
			sieve[composite] = False
	return sieve

def roots(a,b,c):
	pos = -b+sqrt(b**2 - 4*a*c)/(2*a)
	neg = pos - sqrt(b**2 - 4*a*c)/a
	return [pos, neg]


def one():
	print('Zadaj dve cisla vo formate x,y')
	nums = [int(num) for num in input().split(',')]
	if nums[0] > nums[1]:
		nums[0],nums[1] = nums[1],nums[0]
	min = nums[0]//3 + 1
	max = nums[1]//3 + 1
	threeven = []
	for i in range(min, max):
		threeven.append(3*i)
	print (threeven)
	
	primeList = []
	mySieve = makeSieve(nums[1]+1)
	for i in range(nums[0], nums[1]+1):
		if mySieve[i]:
			primeList.append(i)
	print (primeList)
	
def two():
	num = input('Daj cislo\n')
	out = ''
	for digit in num[:-1]:
		out += digit+'*'
	out += num[-1]
	print(out)
	binary = str(bin(int(num)))[2:]
	print(binary)

def three():
	print('Zadaj tri cisla vo formate a,b,c')
	nums = [int(num) for num in input().split(',')]
	A = nums[0]
	B = nums[1]
	C = nums[2]
	if B**2 < 4*A*C:
		print('nemá korene')
		return
	if B**2 >= 4*A*C:
		root = roots(A,B,C)
		print(root[0])
	if B**2 > 4*A*C:
		print(root[1])

def four():

	f = open('04.txt')
	txt = f.read()
	str = input('Prosim retazec:\n')
	wasFound = False
	for charIndex in range(len(txt)-len(str)):
		char = txt[charIndex]
		if char == str[0]:
			found = True
			for index in range(len(str)):
				if not txt[charIndex+index] == str[index]:
					found = False
					break
			if found:
				wasFound = True
					
	out = ''
	if not wasFound:
		out += 'ne'
	out += 'bol najdeny'
	print(out)
		
def six():
	f = open('06.txt')
	txt = f.read().split('\n')[:-1]
	scores = []
	for line in txt:
		name = line[:23]
		time1 = int(line[23:25]) + 0.1*int(line[26])
		time2 = int(line[28:30]) + 0.1*int(line[31])
		scores.append([name, min(time1, time2)])
	top3 = [[0,100],[0,100],[0,100]]
	print(scores)
	for score in scores:
		if score[1] <= top3[0][1]:
			top3[2], top3[1], top3[0] = top3[1], top3[0], score
			continue
		if score[1] <= top3[1][1]:
			top3[2], top3[1] = top3[1], score
			continue
		if score[1] <= top3[2][1]:
			top3[2] = score
			continue
			
	print(top3)
	
def seven():
	a = open('07pdm.txt')
	pdm = a.read().split('\n')
	b = open('07prdm.txt')
	prdm = b.read().split('\n')
	c = open('07pris.txt')
	pris = c.read().split('\n')
	d = open('07privl.txt')
	privl = d.read().split('\n')
	for p1 in pdm:
		for p2 in pris:
			for p3 in privl:
				for p4 in prdm:
					print(p1, p2, p3, p4)
	print('Dokopy je ich', len(pdm)*len(pris)*len(privl)*len(prdm))
	
def eight():
	vstup = input('Prosim si znak a cislo vo formate ?,20\n').split(',')
	znak = vstup[0]
	cislo = int(vstup[1])
	for i in range(cislo):
		out = ''
		for j in range (cislo):
			out += znak
		print(out)
	
	bigOut = ''
	for i in range(cislo):
		out = ''
		for j in range(i+1):
			out += znak
		bigOut += out+'\n'
		
	print(bigOut)
	print(bigOut)
	
	
	for 


eight()



