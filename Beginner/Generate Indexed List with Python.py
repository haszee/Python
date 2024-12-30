# This project involves creating a program that takes a list of elements, processes it using list comprehension, and returns a new list that pairs each element with its index in the original list.


def new_List(myList):
	newlist = [(mylist[x],x) for x in range(len(mylist))]

	return newlist


mylist = ['a', 'b', 'c']

print(new_List(mylist))