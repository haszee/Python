#This program asks the user to enter as many numbers as they wish, adds them together, and then displays the result.



num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

numSum = num1+num2

ans = input('Do you wish to add another number (y/n): ')

while ans == 'y':
	num = int(input('Enter another number: '))
	ans = input('Do you wish to add another number (y/n): ')
	numSum += num

print(numSum)