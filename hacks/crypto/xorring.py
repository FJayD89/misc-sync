plaintext = 'This is a sentence'
hex_plaintext = '1653474602117a555b0719053f165c1305422e4452021e1633595d071b423b42470f03173e53131218422e5e5646140d3445471402012e5f5c08570d3c164314180528575e154d421358401212033e165c00570b3757540f190b345113121f032e165c13054237575a0857163b4558461e117a425c461e0c2942411314167a571305180f2a43470305422d5e52125716351657095b423653474602117a555c0814073442410703077a4452121f0728165c08570722465f071e0c33585446030d7a5e460b160c7a54560f19052916440e16167a4156460003344213075701355b431303072816470957063518'
# key_extended =
short_hex_plaintext = '28fa7f8cd83e8c5b0719053f165c1305422e4452021e1633595d071b423b42470'

banned_chars = '@#$%^&*(){}[]|\\<>`~_=+/'
banned_nums = [ord(char) for char in banned_chars]


def eval_hex_array(hex_str):
	hexArray = []
	length = len(hex_str)
	if length % 2 == 1:
		hex_str += '0'
	for strIndex in range(length//2):
		strByte = hex_str[2 * strIndex:2 * strIndex + 2]
		strByte = '0x' + strByte
		hexArray.append(eval(strByte))
	return hexArray


def get_texts(encrypted_nums, key_length, mod):
	key_chars = [True for _ in range(128)]

	text_length = len(encrypted_nums)
	
	for key_char in range(128):
		for num_index in range(text_length):
			if num_index % 6 != mod:
				continue
			num = encrypted_nums[num_index]
			xor = num ^ key_char
			if xor < 32 or xor == 127 or xor in banned_nums:
				key_chars[key_char] = False
				continue
		
	key_char_options = [i for i in range(128) if key_chars[i]]
	
	texts = []
	
	for key_char in key_char_options:
		new_text = str(key_char) + ' '
		for num_index in range(text_length):
			if num_index % 6 != mod:
				continue
			num = encrypted_nums[num_index]
			xor = num ^ key_char
			new_text += chr(xor)
		texts.append(new_text)
	return texts


nums = eval_hex_array(hex_plaintext)

key = [90, 54, 51, 102, 119, 98]

decoded = ''
for i in range(len(nums)):
	decoded_num = nums[i] ^ key[i % len(key)]
	decoded_char = chr(decoded_num)
	decoded += decoded_char

# print(key_char_options)
for mod_choice in range(6):
	texts = get_texts(nums, 6, mod_choice)
	[print(text) for text in texts]
	print('')
# print(decoded)
# 90, 54, 51, 102, 119, 98
