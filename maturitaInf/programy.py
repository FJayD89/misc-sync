from math import sqrt, ceil
from random import randint

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
		print('nema korene')
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
	
	bigOut = ''
	for i in range(cislo):
		out = ''
		for j in range (cislo):
			out += znak
		bigOut += out+'\n'
	print(bigOut)

	
	
	bigOut = ''
	for i in range(cislo):
		out = ''
		for j in range(i+1):
			out += znak
		bigOut += out+'\n'
		
	print(bigOut)
	
	bigOut = ''
	for i in range(cislo):
		line = ''
		for j in range(cislo-1-i):
			line += ' '
		out = line
		for j in range(2*i+1):
			out += znak
		out += line
		bigOut += out + '\n'
	
	print(bigOut)
	out = ''
	outEmpty = znak
	for i in range(cislo):
	  out += znak
	for i in range(cislo-2):
	  outEmpty += ' '
	outEmpty += znak
	
	print(out)
	for i in range(cislo-2):
	  print(outEmpty)
	print(out)
	
def experiments():
	count = 0
	for i in range(10):
		rand = randint(1,10)
		if rand > 5:
			count += 1
	return count
	
def ten():
	success = [0 for i in range(11)]
	for i in range(400):
		success[experiments()] += 1
	print(success)

def eleven():
	pScore = 0
	aiScore = 0
	plays = {
		'r':0,
		'p':1,
		's':2
		}
	choices = ['rock', 'paper', 'scissors']
	counter = int(input('How many iterations?\n'))
	for i in range(counter):
		choice = input('Rock, paper, scissors! (r/p/s)\n')
		choice = plays[choice]
		print('Player chose', choices[choice],'!')
		aiChoice = randint(0,2)
		print('Computer chose', choices[aiChoice], '!')
		if choice == aiChoice:
			print('tie')
			continue
		if choice+1 % 3 == aiChoice:
			pScore += 1
			print('You won!')
			continue
		print('You lost!')
		aiScore += 1
	print('Results:')
	print('You:', pScore)
	print('Computer:', aiScore)
	winText = 'You win!'
	if pScore < aiScore:
		winText = 'Computer wins!'
	if pScore == aiScore:
		winText = 'It\'s a tie!'
	print(winText)
		
def twelve():
	m = int(input('Zadaj cislo:\n'))
	n = int(input('Este jedno:\n'))
	c = input('A este znak:\n')
	
	line1 = ''
	for i in range(m*n-m+1):
		line1 += c
	
	
	line2 = c
	for i in range(n-2):
		line2 += ' '
	line3 = ''
	for i in range(m):
		line3 += line2
	line3 += c
	
	line4 = line1 + '\n'
	for i in range(n-3):
		line4 += line3+'\n'
	line4 += line3
	
	for i in range(m):
		print(line4)
	print(line1)
	
def thirteen():
	attempts = 1
	done = False
	cislo = randint(1,100)
	tip = int(input('Tipni si cislo: \n'))
	if tip == cislo:
		print('Super, vyhral si na 1. pokus!')
		return 0
	if tip > cislo:
		print('To je vela')
	if tip < cislo:
		print('To je malo')	
	while True:
		attempts += 1
		if input('Nechces sa vzdat?\n') == 'ano':
			if attempts == 2:
				print('ts, ty lemra')
				break
			print('Ok, ani mne uz sa nechce')
			print('BTW, vzdal si sa po', attempts-1, 'pokusoch')
			break
		tip = int(input('Skus este raz: \n'))
		if tip == cislo:
			print('Super, uhadol si na', attempts, 'pokusov!')
			break
		if tip > cislo:
			print('To je vela')
			continue
		print('To je malo')
	
def fifteen():
	hodnoty = [a*10**i for i in range(2,-3, -1) for a in [5,2,1]]
	
	pocty = {a:0 for a in hodnoty}
	
	suma = float(input('Zadaj sumu vo formate 123.45 \n'))
	# print(hodnoty)
	# print (pocty)
	
	while suma != 0:
		for hodnota in hodnoty:
			if hodnota <= suma:
				suma -= hodnota
				pocty[hodnota] += 1
				break
	for hodnota in hodnoty:
		if pocty[hodnota] != 0:
			print(hodnota, pocty[hodnota])
	
	

fifteen()



