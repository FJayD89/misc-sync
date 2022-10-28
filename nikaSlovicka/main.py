from pathlib import Path
from random import randint

base_path = Path(__file__).parent
file_path_nika = (base_path / "../nikaSlovicka/wordlistU1.txt").resolve()
file_path_joni_eng = (base_path / "../nikaSlovicka/Prj2_U2_eng.txt").resolve()
file_path_joni_svk = (base_path / "../nikaSlovicka/Prj2_U2_svk.txt").resolve()


with open(file_path_nika, errors='ignore') as f:
	wordsNika = f.read().split('\n')
with open(file_path_joni_eng, errors="ignore", encoding='utf-16') as f:
	wordsJoniEng = f.read().split('\n')
with open(file_path_joni_svk, errors="ignore", encoding='utf-16') as f:
	wordsJoniSvk = f.read().split('\n')


def splitSlashJoni(string):
	sLen = len(string)
	ipaEnd = -2
	ipaStart = sLen
	for charIndex in range(sLen):
		char = string[charIndex]
		if char == '/':
			ipaStart = charIndex
			break
	# for charIndex in range(sLen-1, -1, -1):
	# 	char = string[charIndex]
	# 	if char == '/':
	# 		ipaEnd = charIndex
	# 		break
	return string[:ipaStart]


# sourceNika: https://www.macmillan.sk/images/slovnicky/sl-Gateway-to-Maturita-B2.pdf
wordsNika = [[word.split('/')[0], splitSlashJoni(word)] for word in wordsNika]
wordsJoni = [[splitSlashJoni(wordsJoniEng[i]), splitSlashJoni(wordsJoniSvk[i])] for i in range(len(wordsJoniEng))]

learned = []


def revisionNika():
	seen = []
	while len(seen)+len(learned) < len(wordsNika):
		index = randint(0, len(wordsNika) - 1)
		if (index in seen) or (index in learned):
			continue
		seen.append(index)
		pair = wordsNika[index]
		print(pair[1], end='')
		input()
		print(pair[0], end='')
		if input() == 'w':
			learned.append(index)
	print('Super, vies vsetko!')
	if input('Este raz? (ano/nie)') == 'ano':
		revisionNika()



def revisionJoni():
	seen = []
	while len(seen)+len(learned) < len(wordsJoni):
		index = randint(0, len(wordsJoni) - 1)
		if (index in seen) or (index in learned):
			continue
		seen.append(index)
		pair = wordsJoni[index]
		print(pair[1], end='')
		input()
		print(pair[0], end='')
		if input() == 'w':
			learned.append(index)
	print('Super, vies vsetko!')
	if input('Este raz? (ano/nie)') == 'ano':
		revisionJoni()


revisionJoni()
# print(splitSlash('abc  /aiwndfie/ d'))