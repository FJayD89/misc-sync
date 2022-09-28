mTable = {
    'a':'d'
    }

mText = input()

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
            text[index] = subTable[key]

print(characters(mText))
    
