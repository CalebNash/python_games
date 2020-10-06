import random

num = int(input("Enter a number between 1 and 100: "))

counter = 0

guess = 0

while guess != num:
    guess = random.randint(1, 100)
    counter +=1

print('The computer guessed in', counter, 'tries.')
