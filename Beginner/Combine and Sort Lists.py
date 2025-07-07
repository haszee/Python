list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]

list1.extend(list2)

newlist = list(set(list1))

print(newlist)

