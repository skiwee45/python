#chapter 3 challenge 4
print("\t\t\tThis is a program that lets you pick the number from 1-100, the computer will guess it.")
number=int(input("Put in a number you think is hard to guess: "))
x=1
y=100
import random
guess=random.randint(x,y)
tries=1
while guess !=number:
    print(guess)
    
    if guess>number:
        print("Smaller")
        y=guess-1
        
    else:
        print("Bigger")
        x=guess+1
        
    tries+=1
    guess=random.randint(x,y)

        
print("Yay, the computer guessed the secret number", number, "in", tries, "tries")