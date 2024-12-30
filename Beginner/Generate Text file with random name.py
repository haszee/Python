import random
import string

def random_file():
	name = ''.join(random.choices(string.ascii_letters,k=10))
	f = open(name,"w")

random_file()