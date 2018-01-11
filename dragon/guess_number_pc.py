#this program let player put in a number and let comput guess
#Computer need guess it smartly
import random

print("""
Welcome to upgraded version of guess my number!
In this game player will input a secret number btw 1 and 100.
Computer will try to guess it in as few attempts as possible
""")

secret=int(input("\nEnter your secret number: "))
range_min = 1
range_max = 100
guess = random.randint(range_min, range_max)
tries = 1
print("Guess:", guess, "attempt:", tries);
while secret != guess: 
    if guess > secret:
        range_max = guess
    else:
        range_min = guess
    guess = random.randint(range_min, range_max)
    tries += 1
    print("Guess:", guess, "attempt:", tries);
    
print("Congrats! Number is", secret, "after", tries, "!")