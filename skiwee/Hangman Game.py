HANGMAN = (
"""
------
|   |
|
|
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
|
|
|
|
|
|
----------
""",
"""
------
|  |
|  O
| -+-
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|   |
|
|
|
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|   |
|   |
|  |
|  |
|
----------
""",
"""
------
|   |
|   O
| /-+-/
|   |
|   |
|  | |
|  | |
|
----------
""")
maxwrong=len(HANGMAN)-1
f = open('raymond-words.txt', 'r')
words = f.readlines()
#choosing a random word out of the initial words
import random
word=random.choice(words).strip().lower()
#for item in word:
    #print("word: ", item)

sofar="-" * len(word)
wrong=0
used=[]
print("""
                       Welcome to the Hangman Game!
                    Type a letter that you think is in the word.
""")
while wrong<maxwrong and sofar!=word:
    print(HANGMAN[wrong])
    print("You have used these letter so far:\t", used)
    print("So far the word is:\t", sofar)
    print("The word is: ", len(word), "letters long")
    
    guess=input("\nGuess a letter: ")
    guess=guess.lower()
    
    
    while guess in used:
        print("\nYou have already guessed this letter")
        guess=input("\nGuess another letter: ")
        guess=guess.lower()
        
    used.append(guess)
    
    if guess in word:
        print("\nYay, you guessed a letter thats in the word!")
        new=""
        
        for i in range(len(word)):
            if guess==word[i]:
                new+=guess
            else:
                new+=sofar[i]
        sofar=new
        
    else:
        print("\nSorry, your guess wasn't in the word")
        wrong+=1
        
if wrong==maxwrong:
    print(HANGMAN[wrong])
    print("\nYou just got hanged, GAME OVER!")

else:
    print("\n\nYaya! You won! You succesfully guess the word: ", word, "with: ", wrong, "wrongs!")
    
print("\nThe word was: ", word)

input("\n\nPress the ESC key to exit")