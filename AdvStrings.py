#!/bin/python3

#Advanced Strings

my_name = "Basil"
print(my_name[0])
print(my_name[-1])

sentence = "Python is easy to learn"
print(sentence[:7])
print(sentence.split())

sentence_split = sentence.split()
sentence_join = ''.join(sentence_split)
print(sentence_join)

#To add quotes
#quote = "He said, 'She is very beautiful'"

#or

#quote = 'He said, "She is very beautiful"'

#or

quote = "He said, \"She is very beautiful\""
print(quote)

too_much_space = "              hello               "
print(too_much_space.strip())

print("A" in "Apple") #true
print("a" in "Apple") #false

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #true

movie = "The Hangover"
print("My favourite movie is {}.".format(movie))
