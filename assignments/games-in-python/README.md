# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word guessing game in Python. You will practice string manipulation, loops, conditionals and random selection while handling user input.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Create the starting state of the game: pick a random secret word from a predefined list and prepare the variables that track the player's progress.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Display the hidden word as blanks, one per letter
- Set a limit on the number of incorrect guesses allowed


### 🛠️	Build the Guessing Loop

#### Description
Let the player guess one letter at a time, reveal correct letters and count wrong guesses until the game ends.

#### Requirements
Completed program should:

- Accept a single letter guess from the player on each turn
- Show the current progress of the word after each guess, for example `p y t _ o n`
- Track and display the number of incorrect guesses remaining
- End when the word is fully guessed or the attempts are used up
- Display a clear win or lose message, including the secret word
