from python_enigma import enigma
from itertools import permutations

rotors = 'KYB'
positions = 'FLI'

# use_these = [("I", "K"), ("II", "Y"), ("III", "B")]  # rotors

vowels = 'AEIOUY'

numerals = {1: 'I',
			2: 'II',
			3: 'III',
			4: 'IV',
			5: 'V',
			6: 'VI',
			7: 'VII',
			8: 'VIII'
}

rotor_count = 5


def decrypt(rotor_setup, position_setup):
	machine = enigma.Enigma(catalog="default", stecker="BC UF LE XT IR GN ZJ",
			rotors=list(rotor_setup), reflector="Reflector C", operator=True, word_length=5, stator="military")
	machine.set_wheels(position_setup)
	
	encrypted = 'OBZAS DUUVL WEDCN NGXSD FJZFI CQELT TKJXM HTFFX DBVIA E'
	encrypted.upper()
	# print(encrypted)
	# print("If I feed that back through, it decrypts to:")
	machine.set_wheels(position_setup)
	decrypted = machine.parse(encrypted)
	return decrypted


def vowel_test(text):
	length = len(text)
	words = text.split(' ')
	for word in words[:-1]:
		flag = False
		for char in word:
			if char in vowels:
				flag = True
		if not flag:
			return False
	return True


def q_test(text):
	length = len(text)
	for char_index in range(length):
		char = text[char_index]
		if char == 'Q':
			if char_index == length - 1:
				return False
			if text[char_index + 1] != 'U':
				return False
	return True


def list_to_str(str_list):
	char_str = ''
	for char in str_list:
		char_str += char
	return char_str
	

rotor_perms = list(permutations([numerals[num] for num in range(1, rotor_count+1)], 3))
rotor_perms = [[[rotor_perm[i], rotors[i]] for i in range(3)] for rotor_perm in rotor_perms]
# print(rotor_perms)

pos_list = []
for char in positions:
	pos_list.append(char)

position_perms = list(permutations(pos_list))

position_perms = [list_to_str(perm) for perm in position_perms]

print(position_perms)


for rotor_perm in rotor_perms:
	for position_perm in position_perms:
		decrypted = decrypt(rotor_perm, position_perm)
		if vowel_test(decrypted) and q_test(decrypted):
			print(decrypted)
# print(decrypt(use_these, position_perms[-1]))


# print(decrypt([['I', 'K'], ['II', 'Y'], ['III', 'B']], 'LIF'))
#
# print(decrypt([['I', 'K'], ['II', 'Y'], ['III', 'B']], 'LIF'))

exit()

