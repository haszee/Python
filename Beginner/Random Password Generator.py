import random

length = int(input("Enter the desired password length: "))

include_uppers = input("Include uppercase letters (y/n): ").strip()
include_numbers = input("Include numbers (y/n): ").strip()
include_symbols = input("Include symbols (y/n): ").strip()

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+=?.,<>}{[]|~'

characters = list('abcdefghijklmnopqrstuvwxyz')

if include_uppers == 'y':
	characters.extend(list(uppercase))

if include_numbers == 'y':
	characters.extend(list(numbers))

if include_symbols == 'y':
	characters.extend(list(symbols))

password = ''

while length > 0:
	choice = random.choice(characters)
	password += choice
	length -=1

print(password)