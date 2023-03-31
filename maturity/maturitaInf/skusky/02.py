# 4 < len <= 12
#
# lower & upper chars
# AlphaNum
# pass.has_substr('123') == false

def is_good(pwd,substr):
	if len(pwd) < 4:
		print('Too short!')
		return False
	if len(pwd) > 12:
		print('Too long!')
		return False
		
	hasUpper = False
	hasLower = False
	hasNum = False
	foundIndex = 0
	for char in pwd:
		if 97 <= ord(char) <= 97+25:
			hasLower = True
		if 65 <= ord(char) <= 65+25:
			hasUpper = True
		if 48 <= ord(char) <= 57:
			hasNum = True
			# if char != substr[foundIndex]:
			# 	foundIndex = 0
			# 	if char == substr[0]:
			# 		foundIndex = 1
			# 	continue
			# foundIndex += 1
			# if foundIndex == len(substr):
			# 	print('Contains illegal substring!')
			# 	return False
		if not (hasLower and hasUpper and hasNum):
			print('Either an uppercase, lowercase or num character is missing!')
			return False
		if testPwd.find(substr) != -1:
			print('Contains illegal substring!')
		return False
		
	print('Password is acceptable!')
	return True



print('You need a stronger password.')
testPwd = input("Enter a password to be judged:\n")

print(is_good(testPwd, '123'))





