
def check_username_validity(username):
	if len(username) < 5 or len(username) > 15:
		return "Invalid Username: name is not betwen 5 & 15 characters"
	if username[0].isalpha() == False:
		return "Invalid Username: first character is not a letter"
	if username.isalnum() == False:
		return "Invalid Username: name is not alphanumeric"

	return "Valid Username"


print(check_username_validity("213232"))
print(check_username_validity("dcwqdww"))
print(check_username_validity("lnjnjn423423knlknlnkln322nn3"))
print(check_username_validity("ddcbrs!_"))
print(check_username_validity("njn13123kn"))
