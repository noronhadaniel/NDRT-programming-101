# Challenge 3 - Guessing Game (09/16/2021)

import random
import sys

num = random.randint(1,100)
print("\nRANDOM NUMBER GUESSING GAME")
# GAME LOOP
while True:
    try:
        guess = int(input("\nGuess an integer between 1 and 100: "))
    except:
        print("Sorry, you did not enter an integer. Please try again")
        continue
    if guess not in range(1,101):
        print("Integer not in range [1,100]. Please Try Again.")
        continue
    elif guess > num:
        print("Too High!")
    elif guess < num:
        print("Too Low!")
    else:
        print(f"Spot On! You won the game. The number was {num}.\n")
        break
    a = input("Would you like to try again?[y/n]: ")
    if a == "y" or a == "Y" or a == "yes" or a == "Yes":
        continue
    else:
        print(f"The answer was {num}. Better luck next time!\n")
        break

