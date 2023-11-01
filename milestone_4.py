
import random
import itertools

#This defines the hangman game class
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        print(self.word)
        self.word_guessed = list(itertools.repeat('_', len(self.word)))
        print(self.word_guessed)
        self.num_letters = int()
        self.list_of_guesses = []

    #This defines a function that checks that the user input is in the secret word
    def check_guess(self, guess):
        self.guess.lower()
        if self.guess in self.word:
            print(f'Good guess! {self.guess} is in the word.')
            word_index = self.word.index(self.guess)
            #Check if working
            print(word_index)
            #Replace letters in word_guessed list
            for letter in self.word:
                if letter == self.guess:
                    self.word_guessed[word_index] = self.guess
            self.num_letters -= 1
            #check if working
            print(self.word_guessed)
            print(self.num_letters)
        else:
            self.num_lives -= 1
            print(f'Sorry, {self.guess} is not in the word. Try again\nYou have {self.num_lives} lives left.')
            
    # Continuously asks the user for a new letter for the hangman game
    def ask_for_input(self):
        while True:
            self.guess = input('Enter a single letter: ')

            if len(self.guess) != 1 and not self.guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif self.guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(self.guess)
                #Will the below run if the above function is called first?
                self.list_of_guesses.append(self.guess)
                
word_list = ['kiwi', 'grape', 'apple', 'passion fruit', 'banana']

my_call = Hangman(word_list)

my_call.ask_for_input()
