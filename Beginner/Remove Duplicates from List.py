numbers = [3, 1, 2, 3, 4, 1, 5, 2]

count = {}
cleaned_numbers = []

for num in numbers:
	if num not in count:
		count[num] = 1
		cleaned_numbers.append(num)
		
print(cleaned_numbers)