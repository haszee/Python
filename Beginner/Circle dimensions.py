from math import pi

def circle_area(radius):
	print(round(pi*radius**2,2))


def circle_circumference(radius):
	print(round(2*pi*radius,2))


circle_area(10)
circle_area(5)
circle_area(1)
circle_area(2)


print("----------------------------------------------------------")

circle_circumference(10)
circle_circumference(5)
circle_circumference(1)
circle_circumference(2)