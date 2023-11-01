
import random
import itertools

class Hangman:
    '''
    This class is used to play the Hangman game.

    Attributes:
        word_list (list): a variety of words to be chosen at random.
        num_lives (int): the number of remaining lives in each instance of the game.
        word (str): a random word selected from the word_list.
        word_guessed (list): list of dashes corresponding to the characters in the word.
        num_letters int(): number of unique letters in the word.
        list_of_guesses: list to record previously guessed letters.
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        See help(Hangman) for accurate signature.
        '''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = list(itertools.repeat('_', len(self.word)))
        print(self.word_guessed)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def play_game(self, word_list):
        '''
        This method checks if there are remaining lives, in which case the game continues.
        If not, the game is ended and the user is notified that the game is lost.
        If all the letters in the word are guessed then the user is notified that the game is won and then it terminates.
        '''
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
        
    def check_guess(self, guess):
        '''
        This method checks that the letter guesses are in the secret word and updates the `word_guessed` variable accordingly.
        When correct letters are guessed, the number in the num_letters variable is reduced.
        This allows the game to know when you have won.
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
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
           
    def ask_for_input(self):
        '''
        This method asks for user input, checks that it is a valid single letter and continues the game.
        It also checks if the letter has already been guessed and appends the list_of guesses variable if not.
        '''
        self.guess = input('Enter a single letter: ')

        if len(self.guess) != 1 or not self.guess.isalpha():
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif self.guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess)

 '''
 The list below provides the game with a variety of strings to select at random.
 The list is then passed as an argument into the Hangman class and the play_game method to initiate the game.
 '''               
word_list = ['kiwi', 'grape', 'apple', 'strawberry', 'banana']

game = Hangman(word_list)

game.play_game(word_list)
