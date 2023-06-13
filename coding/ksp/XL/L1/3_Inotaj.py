init = [int(num) for num in input().split(' ')]
iCount = init[0]
maxWordLen = init[1]

words = []
for wordIndex in range(iCount):
	words.append(input())

def wordAllScores(word, chars_list):
	scores = {char:0 for char in chars_list}
	for char in word:
		scores[char] += 1
		continue
	return scores

def wordsScoreCalc(score_char, scores_list):
	scores = []
	# for char in word:
	# 	if char == score_char:
	# 		score += 1
	# 		continue
	# 	score -= 1

	for wordIndex in range(iCount):
		score = 2*scores_list[wordIndex][score_char] - len(words[wordIndex])
		scores.append(score)

	return scores

def listScores(score_char, scores_list):
	scoresList = wordsScoreCalc(score_char, scores_list)
	scoresList.sort()
	return scoresList

def findMaxLen(word_list, score_char, max_found_elsewhere, scores_list):
	listLegth = len(word_list)
	scoresList = listScores(score_char, scores_list)
	scoreSum = sum(scoresList)
	maxInotajLen = 0
	for i in range(listLegth):
		if listLegth - i < max_found_elsewhere:
			break
		if scoreSum >= 0:
			maxInotajLen = listLegth - i
			break
		scoreSum -= scoresList[i]
	return maxInotajLen

def getAllChars(word_list):
	collectedChars = []
	for word in word_list:
		for char in word:
			if not char in collectedChars:
				collectedChars.append(char)

	return collectedChars

charsList = getAllChars(words)

allScoresList = [wordAllScores(word, charsList) for word in words]

maxFoundLen = 0

for tryChar in charsList:
	foundLen = findMaxLen(words, tryChar, maxFoundLen, allScoresList)
	if foundLen > maxFoundLen:
		maxFoundLen = foundLen


print(maxFoundLen)