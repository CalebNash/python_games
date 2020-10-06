import random

with open ('/usr/share/dict/words') as infile:
    words = infile.read()
    wordNum = random.randint(1, 235886)
    wordList = words.split()
    word = wordList[wordNum].lower()

full_word = "_" * len(word)
guessed_letters = []
wrong_guesses = 10
you_won = False
print("Lets Play Hangman!")
print(full_word)
print('\n')

while not you_won & wrong_guesses > 0:
    guess = input('Guess a letter: ')

    if len(guess) == 1 and guess.isalpha():
        print('good')
        guessed_letters.append(guess)
    else:
         print("Not a valid guess.")
    print(guessed_letters)
