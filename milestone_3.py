
#Checks if the guess is in the word: `frantic`        
secret_word = 'frantic'

def check_guess(guess):
    guess.lower()
    if guess in secret_word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')


# Continuously asks the user for a new letter for the hangman game
def ask_for_input():
    while True:
        guess = input('Enter a single letter: ')

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

    check_guess(guess)

ask_for_input()