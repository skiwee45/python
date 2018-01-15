import random

WORDS=("derp", "hurp", "derpahurp", "pikaderp", "derpachu", "harmandeep",
       "dankmeme", "supercalifragilisticexpialidocious", "hurpaderp", "raymonderp", "harmanderp", "chelseaherp")
#make a word jumble
word=random.choice(WORDS)
#now i picked a random word from the tuple
correct=word
#now i am creating an empty jumble of the word
jumble=""
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]
    
#that was just making the random word, now the game will start
print("""

                  Welcome to Word Scramble!
            
            Unscramble the letters to make the word.
            
    If you give up and wanna quit press enter when you are asked for your guess.
""")
print("\n\n\t\t\t\tThe word scramble is: ", jumble)

guess=input("Enter your guess: ")
while guess!=correct and guess!="":
    print("\nThats not correct! Guess again!\n\n")
    guess=input("Enter your guess: ")  

if guess==correct: 
    print("\n\n\nYay, you guess the word!\n\n\n")
        
print("Thanks for playing my word jumble game by Raymond Lin")
input("\n\n\n\t\t\tPress the ESC key to exit")