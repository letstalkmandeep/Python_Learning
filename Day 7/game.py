"""
### Mini Project

Project: Number Guessing Game

Project Description:

The program will randomly select a number between 1 and 20. The player will have a limited number 
of chances (let’s say 5) to guess the number. After each guess, the program will tell the player 
whether their guess is too high or too low. If the player guesses correctly within the allowed 
number of attempts, they win. Otherwise, the game ends and the player loses.
"""


import random
rand = random.randint(1,20)

attempt = 5



while attempt > 0 :
    number = int(input("Write your number - "))
    if number == rand :
        print(f"Wow you won $1000 number was {rand}")
        break
    elif number < rand :
        print(f"Your number was a bit lower\nTotal Attempts left {attempt}")
    else :
        print(f"Your number was a bit Higher\nTotal Attempts left {attempt}")

    attempt -= 1

    if attempt == 0:
        print(f"YOU LOSE number was {rand}")



