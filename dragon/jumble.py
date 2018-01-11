# this is my jumble game
# computer pick a random word and jumble it
# player has to guess the original word
import random

#create a variabl to check if word is correct
correct = random.choice(("python", "jumble", "easy", "difficult", "answer", "xylophone"))

def jumble(word):
    result = ""
    while word:
        position = random.randrange(len(word))
        result += word[position]
        word = word[:position] + word[position+1:]
    return result

# start the game
print("""
               Welcome to the word jumble!
               
               Unscramble the letters to make a word
""");
print("The jumble is:", jumble(correct))
guess = input("\nYour guess: ")
while guess != correct and guess !="":
    print("Sorry, not correct.")
    guess = input("\nYour guess: ")
    
if guess == correct:
    print("That's it! Congrats!!!\n")
    
input("Press any key to exit")