import csv

word1 = input("Enter a word in Language 1 (or type 'done' to finish): ")

dictionary = {}

while word1 != 'done':
	word2 = input(f"Enter the translation of the word '{word1}' in Language 2: ")

	dictionary[word1] = word2

	word1 = input("Enter a word in Language 1 (or type 'done' to finish): ")


with open("translations.csv", "w") as translations:
	for key,value in dictionary.items():
		writer = csv.writer(translations)
		writer.writerow([key, value])