grocery_list = {
    "apples": 5,
    "bananas": 2,
    "milk": 1,
    "bread": 1
}

for item in grocery_list.keys():
    grocery_list[item] *= 10

print(grocery_list)