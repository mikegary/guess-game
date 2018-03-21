#This a number guessing game
import random

print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number betwwen 1 and 20.')

# Ask the player to guess 6 times
for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + ' ! You guessed my number in ' + str(guessTaken) + ' guesses!')
else: print('Nope. The number I was thinking of was ' + str(secretNumber))
