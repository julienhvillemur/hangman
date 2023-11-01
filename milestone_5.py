
import random
import itertools

#This defines the hangman game class
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = list(itertools.repeat('_', len(self.word)))
        print(self.word_guessed)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def play_game(self, word_list):
        self.num_lives = 5
        while True:
            if self.num_lives == 0:
               print('You lost!')
               break
            elif self.num_letters > 0:
               self.ask_for_input()
            else:
               print('Congratulations. You won the game.')
               break
        
    #This defines a function that checks that the user input is in the secret word
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            #Replace letters in word_guessed list
            position_in_word = 0
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[position_in_word] = guess
                position_in_word += 1
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again\nYou have {self.num_lives} lives left.')
           
            
    # Continuously asks the user for a new letter for the hangman game
    def ask_for_input(self):
        self.guess = input('Enter a single letter: ')

        if len(self.guess) != 1 or not self.guess.isalpha():
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif self.guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self.check_guess(self.guess)
            #Will the below run if the above function is called first?
            self.list_of_guesses.append(self.guess)
                
word_list = ['kiwi', 'grape', 'apple', 'strawberry', 'banana']

game = Hangman(word_list)

game.play_game(word_list)
