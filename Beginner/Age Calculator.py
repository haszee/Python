import datetime
from datetime import date

input_birthday = input("Enter your birthday in the following format DD-MM-YYYY: ")

birthday_list = input_birthday.split("-",) 

current_year = datetime.now().year

age = current_year - birthday_list[2]

print(f"Your are {age} years old.")

# -------------------------------------------

input_birthday = input("Enter your birthday in the following format DD-MM-YYYY: ")

birthday_list = input_birthday.split("-",) 

while birthday_list == []:
	input_birthday = input("Enter your birthday in the following format DD-MM-YYYY: ")
	birthday_list = input_birthday.split("-",) 

birthday = birthday_list[::-1]

birthday = [int(x) for x in birthday]

today = date.today()

age = (today - date(birthday[0], birthday[1], birthday[2])).days//365

print(age)



