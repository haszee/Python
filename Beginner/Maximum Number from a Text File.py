f = open('numbers.txt')

max = 0 

for number in f:
	if int(number) > max:
		max = int(number)

print(max)	