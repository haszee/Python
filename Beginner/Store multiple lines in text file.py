sentence1 = input('Enter a sentence: ')
sentence2 = input('Enter another sentence: ')
sentence3 = input('Enter the final sentence: ')

f = open('store_sentences.txt', "w")

f.write(sentence1)
f.write('\n---------------\n')
f.write(sentence2)
f.write('\n---------------\n')
f.write(sentence3)

f.close()

print('Your Sentences have been saved in store_sentences.txt')