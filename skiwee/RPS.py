import random
#the constants
R="R"
P="P"
S="S"
CHOICES=[R, P, S]
TIE="TIE"
NUM_OF_GAMES=20
WIN={R:S, P:R, S:P}

def instructions():
    """Shows the user the instructions"""
    print("""This is a game of rock paper scissors (RPS)\n pick a choice and see if you can beat the computer in a game out of five""")

def winner_check(H, C):
    """Determines winner, or tie"""    
    if H == C != None:
        print("It is a tie, lets play again!")
        return TIE
    if C and WIN[C]==H:
        return C
    if H and WIN[H]==C:
        return H

def ask_RPS(question):
    """Asks a yes no question, recieves an answer"""
    answer = None
    while answer not in CHOICES:
        answer = input(question).upper()
    return answer

def human_move():
    """Gets the human move"""
    move=ask_RPS("Please put in rock paper or scissors(R, P, S): ")
    return move

def computer_move():
    """Random chooses the computer move out of R, P, and S"""
    move=random.choice(CHOICES)
    print("Computer move was", move)
    return move

def congrats(H, C, winner):
    """Congrats the Winner!"""
    if H==winner:
        print("Congratulations, you beat the computer! GG!")
    else:
        print("Take the L! YOU LOOOOOOOOOOOOOOOOOOST!! HAHAHAHA")

def onegame():
    """The function that pulls everything together for one game"""
    winner=None
    while winner==None or winner==TIE:
        H=human_move()
        C=computer_move()
        winner=winner_check(H, C)
    congrats(H, C, winner)
    if winner==H:
        return 1
    else:
        return 0

def main():
    """Pulls together a certain number of games"""
    instructions()
    score=0
    for count in range(NUM_OF_GAMES):
        score+=onegame()
        print("Your score so far is:", score, "out of", count+1)
    print("You won", score, "games out of", NUM_OF_GAMES)

#time to actually run the program
main()