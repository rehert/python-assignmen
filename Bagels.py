import random

# Game settings
NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f""""Bagels - A deductive logic game.

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. 

Clues:
  Pico  = One digit correct but in the wrong position.
  Fermi = One digit correct and in the right position.
  Bagels= No digit is correct.
""")

    while True:
        secret_num = get_secret_num()
        print(f"I have thought up a number. You have {MAX_GUESSES} guesses.")

        for guess_num in range(1, MAX_GUESSES + 1):
            guess = get_guess(guess_num)
            clues = get_clues(guess, secret_num)
            print(clues)

            if guess == secret_num:
                break
        else:
            print(f"You ran out of guesses. The answer was {secret_num}.")

        if not input("Play again? (yes/no): ").lower().startswith('y'):
            print("Thanks for playing!")
            break


def get_secret_num():
    """Return a string of NUM_DIGITS unique random digits."""
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:NUM_DIGITS])


def get_guess(guess_num):
    """Ask the player for a valid guess and return it."""
    while True:
        guess = input(f"Guess #{guess_num}: ")
        if len(guess) == NUM_DIGITS and guess.isdecimal():
            return guess
        print(f"Enter a {NUM_DIGITS}-digit number.")


def get_clues(guess, secret_num):
    """Return Pico, Fermi, or Bagels clues based on the guess."""
    if guess == secret_num:
        return "You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")

    return " ".join(sorted(clues)) if clues else "Bagels"


if __name__ == "__main__":
    main()

