# Hangman

## Description:
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation:
Save the `milestone_5.py` file in your selected directory and open the file within a python interpreter. Ensure that the `random` and `itertools` modules are available for import into the hangman file. The game will make use of the available `Hangman` class to run.

## Playing The Game:
Run the `milestone_5.py` file and a prompt will appear. Enter a single letter as prompted. If more than one character is entered or a non-alphabetical character is used, the game will prompt the user to try again. If the letter is in the word, the game will present where in the word it is matched and you will be prompted for another guess. If the letter is not in the word, you will lose one life and be prompted to re-guess. If you lose all available lives, the game will end and you will have to restart by running `milestone_5.py` again. If all the letters in the word are guessed, you will received a prompt to say that you have won the game and it will terminate.

## File Structure:
The file contains three methods under the `Hangman` class: `play_game()` `check_guess()` and `ask_for_input()`. The first method checks if there are remaining lives, in which case the game continues. If not, the game is ended and the user is notified that the game is lost. If all the letters in the word are guessed then the user is notified that the game is won and then it terminates. The second method checks that the letter guesses are in the secret word and updates the `word_guessed` variable accordingly. The final method asks for user input, checks that it is a valid single letter and continues the game. It also checks if the letter has already been guessed and appends the list_of guesses variable if not.

## License Information:
### MIT License

Copyright (c) [2023] [Julien Hamilton - Villemr]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
