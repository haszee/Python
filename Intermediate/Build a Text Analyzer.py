import math
import re

text = input("Enter a block of text for analysis: ")

wordList = re.split("[?.!, ]", text)
wordList = [x for x in wordList if x != ""]

sentenceList = re.split("[?.!]", text)
sentenceList = [x.strip() for x in sentenceList if x != ""]

Frequency = {}
for i in range(len(wordList)):
	if wordList[i] not in Frequency:
		Frequency[wordList[i]] = wordList.count(wordList[i])
	else:
		pass
maxCount = 0
for key,value in Frequency.items():
	if value > maxCount:
		maxCount = value
		mostFrequent = key


word_len = 0
for word in wordList:
	word_len += len(word)
word_len = word_len/len(wordList)

sentence_len = 0
for sentence in sentenceList:
	sentence_len += len(sentence)
sentence_len = sentence_len/len(sentenceList)

print("\nText Analysis Results")
print("-----------------------")
print(f"Total characters: {len(text)}")
print(f"Total Words: {len(text.split())}")
print(f"Total sentences: {text.count(".")+text.count("!")+text.count("?")}")
print(f"Most Frequent Word: {mostFrequent}: used {maxCount} times")
print(f"Average Word Length: {word_len}")
print(f"Average Sentence Length: {sentence_len}")