import random


num = random.randint(1, 100)

count = 0

while count < 8:
    count += 1

    guess = int(input("Guess a number between 1 and 100: "))

    if num == guess:
       print("Congratulations you guessed right!")
       break
    elif num > guess:
       print("Too low!")
    elif num < guess:
       print("Too high!")

    if count == 8:
        print("You lost! The correct number was ", num)
