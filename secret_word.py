import random

with open ('/usr/share/dict/words') as infile:
    words = infile.read()
    wordNum = random.randint(1, 235886)
    wordList = words.split()
    word = wordList[wordNum].lower()
    print(word)

full_word = "_" * len(word)
guessed_letters = []
wrong_guesses = 10
you_won = False
print("Lets Play Hangman!")

while not you_won and wrong_guesses > 0:
    print('\n')
    print(full_word)
    guess = input('Guess a letter: ')

    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You already guessed the letter", guess)
        elif guess not in word:
            print(guess, "is not in the word.")
            wrong_guesses -= 1
            guessed_letters.append(guess)
        else:
            print("Good job,", guess, "is in the word!")
            guessed_letters.append(guess)
            word_as_list = list(full_word)
            print(word_as_list)
            letters = [i for i, letter in enumerate(word) if letter == guess]
            print(letters)
            for index in letters:
                word_as_list[index] = guess
            full_word = "".join(word_as_list)

            if "_" not in full_word:
                you_won = True

    else:
        print("Not a valid guess.")
    print(wrong_guesses, 'tries left')
