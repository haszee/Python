contacts = []

while True:
	name = input("Enter contact name (or type 'done' to finish): ").strip()

	if name.lower() == 'done':
		break

	phone = input(f"Enter phone number for {name} separated by '-': ").strip()

	contacts.append(f"{name}: {phone}")

	with open("Contacts.txt", "w") as f:
		for contact in contacts:
			f.write(contact + "\n")

	print("Your Contacts have been saved to Contacts.txt")