# ## ✍️ Author

# Connect with me and check out my other projects!

# * **Abhijeet** - [GitHub Profile](https://github.com/Abhijeet01012002)


# * **Abhijeet** - [Linkdin Profile](https://www.linkedin.com/in/abhijeet-bhagat-4912b2382)


# * **Abhijeet** - [Abhijeet.akj@gmail.com](abhijeet.akj@gmail.com)


# * **Abhijeet** - [Instagram Profile](https://www.instagram.com/abhijeet.official.30/)

# Importing the Random Module

import random

name = input("What is your name? ")

print("Good Luck ! ", name)

# A list of possible words for the guessing game is defined. These words are strings stored in a list called words. Also, the program selects a random word from the words list using random.choice(). The selected word is stored in the variable word.

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")

# The game loop will end either when the user guesses the word correctly (all characters are guessed) or when the user runs out of turns.

# ## ✍️ Author

# Connect with me and check out my other projects!

# * **Abhijeet** - [GitHub Profile](https://github.com/Abhijeet01012002)


# * **Abhijeet** - [Linkdin Profile](https://www.linkedin.com/in/abhijeet-bhagat-4912b2382)


# * **Abhijeet** - [Abhijeet.akj@gmail.com](abhijeet.akj@gmail.com)


# * **Abhijeet** - [Instagram Profile](https://www.instagram.com/abhijeet.official.30/)