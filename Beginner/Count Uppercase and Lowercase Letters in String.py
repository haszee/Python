text = "This Sentence Has Mixed CASE Letters!"

upper = 0
lower = 0

for char in text:
	if char.isupper():
		upper += 1
	elif char.islower():
		lower += 1

print(f"The number of uppercase letters is {upper}")

print(f"The number of lowercase letters is {lower}")
