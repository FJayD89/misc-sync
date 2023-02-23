Alpha = list('abcdefghij')

mTable = {
	'a': 'd'
}

# mText = input()

def characters(text):
	chars = {}
	length = len(text)
	for charIndex in range(length):
		char = text[charIndex]
		if char in chars.keys():
			chars[char].append(charIndex)
			continue
		chars[char] = [charIndex]
	return chars

def substitute(text, subTable):
	indexes = characters(text)
	for key in subTable.keys():
		for index in indexes[key]:
			text = text[:index] + subTable[key] + text[index+1:]
	return text

def allSubs(letters, alphabet):
	if len(letters) == 1:
		return [{letters[0]:letter} for letter in alphabet]
	subs = []
	newLetters = letters
	newLetters = newLetters[1:]
	for letter in alphabet:
		newAlphabet = list(alphabet)
		newAlphabet.remove(letter)
		for sub in allSubs(newLetters, newAlphabet):
			if letters[0] != letter:
				sub[letters[0]] = letter
				subs.append(sub)
	return subs




for subTable in allSubs(['V', 'Q', 'X', 'P', 'M'], Alpha):
	print(substitute('PVXMXQP', subTable))

    
