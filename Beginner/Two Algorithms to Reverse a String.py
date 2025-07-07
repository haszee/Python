text = "Python is fun!"


print(text[::-1])

#-----------------------

newtext = ''

for char in text:
	newtext = char + newtext

print(newtext)