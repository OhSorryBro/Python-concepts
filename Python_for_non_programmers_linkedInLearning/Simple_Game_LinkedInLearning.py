import random
import time
correct_number = random.randint(1,100)
print("Welcome to the guessing game, please guess number between 1 and 100")
time.sleep(1)
print("Picking a number...")
time.sleep(2)
guess = 0
guess_count = 0
while guess != correct_number:
    guess = input("What is your guess?: ")
    guess = int(guess) 
    guess_count += 1
    time.sleep(.5)
    if guess < correct_number:
        print("You have to guess higher")
    if guess > correct_number:
        print("You have to guess lower")
print(f"You got the right answer! Is was {correct_number}, it too you {guess_count} tries.")