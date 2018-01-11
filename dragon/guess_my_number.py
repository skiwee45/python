# this is a guess number game, pick a numer from 1 to 100 and let use guess
import random

print("""
Welcome to the guess number game!
I am thinking of a number between 1 and 100.
Try to guess it in as few attempts as possible.
Good luck!
""")

# set initial value
r = random.randint(1,100)
guess = int(input("Take a guess:"))
tries = 1
while (guess != r):
    if guess > r: 
        print("too big")
    else:
        print("too small")
    guess = int(input("Take a guess:"))
    tries += 1

print("You got it right! After", tries, "tries!")
input("\n\nPress any key to exit")