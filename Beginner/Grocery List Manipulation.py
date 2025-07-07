grocery_list = ["apples", "bread", "milk", "eggs", "bananas"]

grocery_list.append("beans")
grocery_list.remove("bread")

grocery_list.sort()

# print(f"Updated Grocery List:")

print(f"Updated Grocery List:\n\n{'\n'.join(f"{item}" for item in grocery_list)}")