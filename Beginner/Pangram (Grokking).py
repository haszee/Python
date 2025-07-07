def checkIfPangram(sentence):
		unique_set = set(sentence)

		return len(unique_set) == 26

#--------------------------

def checkIfPangram(sentence):

	for letter in 'abcdefghijklmnopqrstuvwxyz':
		if letter.lower() in sentence or letter.upper() in sentence:
			continue
		else:
			return False

	return True


sentence = "This is not a pangram"

print(checkIfPangram(sentence))

#---------------------------------------------------

def checkIfPangram(sentence):
	# Create a set to store unique characters
	seen = set()

	# Iterate over each character using a normal for loop
	for i in range(len(sentence)):
		# Convert the current character to lowercase
		currChar = sentence[i].lower()
        
		if currChar.isalpha():
			# Add the character to the set
			seen.add(currChar)

	# Return true if set size is 26 (total number of alphabets)
	return len(seen) == 26