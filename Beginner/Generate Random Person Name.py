import random

f = open("names.txt", "r")

content = f.readlines()

num_lines = len(content)

name = content[random.randint(0,num_lines)]

print(name)