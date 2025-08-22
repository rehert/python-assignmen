import random
from string import digits

print("WELCOME TO GUESS THE NUMBER GAME")
print("I am thinking of a number between 1 and 100 can you guess it?")
guess_number= random.randint(1,100)

for guess_left in range(10,0, -1):
    print("You have ",guess_left,'guesses remaining')
    guess = input('Enter your Guess number: ')
    if not guess.isdigit():
        print("enter A valid number between 1 and 100")
        continue
    guess = int(guess)
    if guess > guess_number:
        print("Guess is too high")
    elif guess < guess_number:
        print('Guess is too low')
    else:
        print('Gongrats you have guessed the correct number')
        break
else:
    print("Sorry friend you lost, the guess number was ",guess_number)












