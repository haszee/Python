def count_vowels(text):
	return sum(text.count(letter) for letter in "aeiou")


text1 = "how many vowels are in this sentence?"
text2 = "aeioummmnnnaeiou"
text3 = "mbbvvzx"

print(count_vowels(text1))
print(count_vowels(text2))
print(count_vowels(text3))