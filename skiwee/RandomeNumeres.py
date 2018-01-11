print("This is a number guessing game, the game will tell you if your guess is above or below the answer, you have unlimited tries!")
import random
def guessing_game():
    r=random.randint(1,100)
    while True:
        y=int(input("guess a number between 0 and 100 "))
        if y<r:
            print("Too Small")
            
        elif y>r:
            print("Too Big")
            
        else:
            print("Right On, You WWIIIINNN!!")
            break



    
while True:
    guessing_game()
    z=input("Wanna Play AGAIN!! Type Y or N ")
    if z=="Y" or z=="y":
        continue
    if z=="N" or z=="n":
        print("GAMEOVERERERERER!!!")
        break
