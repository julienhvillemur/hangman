# Hangman

## Description:
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation:
Ensure that the `random` module is available for import into the hangman file. The game will make use of the available `Hangman` class.

## Playing The Game:
Run the `milestone_4.py` file and a prompt will appear. Enter a single letter as prompted. If more than one character is entered or a non-alphabetical character is used, the game will prompt the user to try again. If the letter is in the word, the game will present where in the word it is matched and you will be prompted for another guess. If the letter is not in the word, you will lose one life and be prompted to re-guess.

## File Structure:
The file contains two methods under the `Hangman` class: `check_guess()` and `ask_for_input()`. The first method check that the letter guesses are in the secret word and updates the `word_guessed` variable accordingly. and that the user input is a valid single letter respectively.

## License Information:
