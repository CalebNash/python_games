num = int(input("Enter a number between 1 and 100: "))

counter = 0

low = 1
high = 100
guess = 50

while guess != num:
    counter += 1

    guess = (low + high)//2
    print( guess)

    if guess > num:
        high = guess
    elif guess < num:
        low = guess + 1

print('The computer guessed in', counter, 'tries.')
