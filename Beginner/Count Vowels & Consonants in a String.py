def count_vowels(text):
	return sum(text.count(letter) for letter in "aeiou")


text1 = "how many vowels are in this sentence?"
text2 = "aeioummmnnnaeiou"
text3 = "mbbvvzx"

#-----------------------------------------------

def count_consonants(text):
	return sum(text.count(letter) for letter in "bcdfghjklmnpqrstvwxyz")


text1 = "how many vowels are in this sentence?"
text2 = "aeioummmnnnaeiou"
text3 = "mbbvvzx"


print("There are ", count_vowels(text1), " vowels and ", count_consonants(text1), " consonants.")

print("There are ", count_vowels(text2), " vowels and ", count_consonants(text2), " consonants.")

print("There are ", count_vowels(text3), " vowels and ", count_consonants(text2), " consonants.")