#Imports random module
import random

word_list = ['kiwi', 'grape', 'apple', 'passion fruit', 'banana']

print(word_list)
word = random.choice(word_list)
print(word)
guess = input('Enter a single letter: ')

#Checks if input is 1 character of the alphabet
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')