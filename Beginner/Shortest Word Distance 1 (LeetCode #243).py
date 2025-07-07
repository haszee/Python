def shortest_word_distance(words,word1,word2):

	mindist = float('inf')

	locations_word1 = []
	locations_word2 = []


	for i in range(len(words)):
		if words[i] == word1:
			locations_word1.append(i)
		if words[i] == word2:
			locations_word2.append(i)

	for x in locations_word1:
		for y in locations_word2:
			if mindist > abs(x-y):
				mindist = abs(x-y)

	return mindist


words = ["a", "c", "d", "b", "a"]
word1 = "a"
word2 = "b"

dist = shortest_word_distance(words,word1,word2)


print(dist)