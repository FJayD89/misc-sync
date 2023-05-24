#MatInf

#1 
#CaesarCipher
text = 'AbCdEfGh'
setting = input('encrypt or decrypt? (e/d)')
# setting = 'd'
shift = -1
if setting == 'c':
	shift = 1
	# encrypt 
encrypted = ''
upperStart = ord('A')  # 65
lowerStart = ord('a') # 97
alphabetLength = 26

for char in text:
	code = ord(char)
	if 65 <= code <= 65+25:
		newCode = code+3*shift
		if newCode > 65+25:
			newCode -=26
		if newCode < 65:
			newCode +=26
		encrypted += chr(newCode)
		continue
	
	if 97 <= code <= 97+25:
		newCode = code+3*shift
		if newCode > 97+25:
			newCode -=26
		if newCode < 97:
			newCode +=26
		encrypted += chr(newCode)
		continue
		
print(encrypted)