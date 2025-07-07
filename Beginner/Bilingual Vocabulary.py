dictionary = {}

while True:
	language_1 = input("Enter a word in language 1 (or type 'done' to finish): ").strip()

	if language_1.lower() == 'done':
		break


	language_2 = input(f"Enter the translation of '{language_1}' in language 2: ").strip()

	dictionary[language_1] = language_2

	with open("Dictionary.csv", "w", newline='') as f:
		writer = csv.writer(f)
		writer.writerow(['Language 1', 'Language 2'])
		for word, translation in dictionary.items():
			writer.writerow([word, translation])

