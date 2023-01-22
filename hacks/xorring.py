key = ''
plaintext = 'This is a sentence'
textLength = len(plaintext)
keyLength = len(key)
# key_extended =

def evalHexArray(str):
	hexArray = []
	length = len(str)
	if length % 2 == 1:
		str += '0'
	for strIndex in range(length//2):
		strByte = str[2*strIndex:2*strIndex+2]
		strByte = '0x' + strByte
		hexArray.append(eval(strByte))
	return hexArray


# for i in range(textLength):
# 	char = plaintext[i]
# 	char_code = ord(char)
# 	encoded = char_code & key[i % keyLength]

print(evalHexArray("c1b2"))
print()