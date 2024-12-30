name = input("Hello! What is your name? ")

feeling = input(f"Hello {name}! How are you feeling today?\n1. Happy\n2. Stressed\n3. Tired\nChoose 1, 2 or 3: ")

if feeling == "1":
	print(f"That’s great, {name}! Keep streading your joy")
elif feeling == "2":
	print(f"Take a deep breath, {name}. You're doing amazing!")
else:
	print(f"Rest up, {name}. Tomorrow is a fresh start!")