import random

guessNumber = random.randint(1,20)
guessCount = 0

print('Hello! What is your name?')
Player = input()
print('Well, ' + Player + ', I am thinking of a number between 1 and 20.')      

for guessCount in range(6):
    print('Take a guess')
    guess = input()
    guess = int(guess)

    if guess > 20:
        print('Your guess is higher than 20.')
        print('Guess between 1 and 20.')
    elif guess > guessNumber:
        print('Your guess is too high.')
    
    if guess < 1:
        print('your guess is lower than 1.')
        print('Guess between 1 and 20.')
    elif guess < guessNumber:
        print('Your guess is too low.')

    if guess == guessNumber:
        print('Good job,' + Player + '! You guessed my number in ' + str(guessCount +1) + ' guesses!')
        break

if guess != guessNumber:
    print('Nope! The number I was thinking of was ' + str(guessNumber) + '.') 