def rectangle_area(width,height):
	return width*height

def rectangle_perimeter(width,height):
	return 2*width + 2*height


width = int(input('Enter a rectangle width: '))
height = int(input('Enter a rectangle height: '))

area = rectangle_area(width,height)
perimeter = rectangle_perimeter(width,height)

print(f"The rectangle's area is {area} and the perimeter is {perimeter}.")
