word = input("Enter a word to count: ")

f = open("book.txt", "r",encoding = 'utf-8') # utf-8 is added b/c it was giving UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d 

wordlist = f.read().split()

wordcount = wordlist.count("word")

print(f"The word {word} appears {wordcount} times in the book")
