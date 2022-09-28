from pathlib import Path
from random import randint
import pyttsx3
engine = pyttsx3.init()
# engine.say('Ahoy Nicola')
engine.runAndWait()

base_path = Path(__file__).parent
file_path = (base_path / "../nikaSlovicka/wordlistU1.txt").resolve()

with open(file_path) as f:
	words = f.read().split('\n')

def splitSlash(string):
	count = 0
	for charIndex in range(len(string)):
		char = string[charIndex]
		if char == '/':
			count += 1
			if count == 2:
				return string[charIndex+2:]

# source: https://www.macmillan.sk/images/slovnicky/sl-Gateway-to-Maturita-B2.pdf
words = [[word.split('/')[0], splitSlash(word)] for word in words]


learned = []
def revision():
	seen = []
	while len(seen)+len(learned) < len(words):
		index = randint(0, len(words) - 1)
		if (index in seen) or (index in learned):
			continue
		seen.append(index)
		pair = words[index]
		print(pair[1], end='')
		input()
		print(pair[0], end='')
		if input() == 'w':
			learned.append(index)
	print('Super, vies vsetko!')
	if input('Este raz? (ano/nie)') == 'ano':
		revision()

revision()