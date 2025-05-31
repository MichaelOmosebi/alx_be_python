import random
# Guessing Game

secret_number = random.randint(1, 10)
# This code implements a simple guessing game where the user has to guess a randomly generated number between 1 and 10.

guess_count = 0
print("Welcome to the Guessing Game!")
print("I have selected a secret number between 1 and 10.")
guess = int(input("Guess a number between 1 and 10: "))

while guess != secret_number:
    guess_count += 1
    try:
        guess = int(input("Try again! Guess a number between 1 and 10: "))
        if guess < 1 or guess > 10:
            print("Please guess a number between 1 and 10.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("That's not a valid number. Please enter a number between 1 and 10.")
        continue

print(f"You guessed it in {guess_count} tries!")