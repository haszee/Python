sentence = input("Enter a sentence: ")

wordlist = sentence.split()

for i in range(len(wordlist)):
	if wordlist[i][-1].isalpha() == False:
		wordlist[i] = wordlist[i][:len(wordlist[i])-1]

count = 0

longest_length = 0

longest_word = ''

for i in range(len(wordlist)):

	word = wordlist[i] 

	if word not in "!@#$%^&*()_+?><,.}/;:]'[{|":
		count += 1

		if len(word) > longest_length:
			longest_word = word

	

print(f"The number of words is {count}")

print(f"The longest word is {longest_word}")
