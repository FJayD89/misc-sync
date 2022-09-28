Alpha = list('abcdefghijklmnopqrstuvwxyz')

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

for subTable in allSubs('a', ['b', 'g']):
    print(substitute('abhdabsaaba', subTable))

    
