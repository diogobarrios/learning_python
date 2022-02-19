import random

secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guesses in range(1, 7):
    print('Take a guess:')
    guess = int(input())

    if guess < secret_number:
        print('You are too low.')
    elif guess > secret_number:
        print('You are to high.')
    else:
        # breaks the loop if is reached the max guesses or we guessed it.
        break

if guess == secret_number:
    print('Good Job! You guessed my number in ' + str(guesses) + ' guesses.')
else:
    print('Nope. the number I was thinking of was ' + str(secret_number))
