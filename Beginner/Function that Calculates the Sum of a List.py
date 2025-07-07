# Build a program that has a function that takes a list of numbers and calculates their sum, providing the total sum as output to the user.

def sum_List(numList):
	result = 0

	for num in numList:
		result += num

	return result


numList = [12,23,34,56,34,25,534,5]

print(sum_List(numList))