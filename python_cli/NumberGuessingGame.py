import random
import math as m

print('Welcome to the integer guess game.')
print('   1. You\'ll set the range of the guess by setting the lower end then the higher end')
print('   2. You\'ll be prompted by the available number of guessses and the start score')
print('   3. Then, the game will start')
print('   4. Every wrong guess will reduce your score by 10 points')
print('Let\'s start')

userName = input('Please, enter your name: ')

lowerLimit = int(input(f'Hello {userName}\n. Please, enter the lower limit of guess range: '))
upperLimit = int(input('Please, enter the higher limit of guess range: '))

Target = random.randint(lowerLimit, upperLimit)
guessingsLimit = m.ceil(m.log2(upperLimit - lowerLimit + 1))
score = guessingsLimit * 10

print(f'OK {userName}, you have {guessingsLimit} guesses and your start score is {score}')

availableGuessings = guessingsLimit
guessings = 0

while guessings <= guessingsLimit:
    guessings += 1
    score -= 10
    availableGuessings -= 1
    guess = int(input('Enter your guess: '))

    if guess == Target:
        print(f'Bingo! You found the right number it is {guess}')
        print(f'You have used {guessings} guesses and the remaining guesses are {availableGuessings}')
        print(f'Your score is {score}')
        break
    
    elif guessings > guessingsLimit and guess != Target:
        print(f'Oops! You have consumed all your guesses without reaching the target. Your target was {Target}')
        print(f'Your score is {score}')
        break

    elif guess > Target:
        print(f'Your guess {guess} is higher than target')
        print(f'You have used {guessings} guesses and your available guesses are {availableGuessings}')
        print(f'Your current score is {score}')

    elif guess < Target:
        print(f'Your guess {guess} is lower than target')
        print(f'You have used {guessings} guesses and your available guesses are {availableGuessings}')
        print(f'Your current score is {score}')
