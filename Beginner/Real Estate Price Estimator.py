size = float(input("Enter the size of the property in square feet: "))

location = input("Do you live in a city or suburb? ")

cityprice = 250*size
suburbprice = 150*size

if location == "city":
	print(f"The estimated price for a {size} sq ft property in the city is ${cityprice}")
else:
	print(f"The estimated price for a {size} sq ft property in the suburbs is ${suburbprice}")