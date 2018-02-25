#This is a program that will allow the user to play tictactoe against a computer opponent
import random
EMPTY=" "
X = "X"
O = "O"
TIE = "TIE"
SQUARES = 9

def instructions():
    """Displays the game rules"""
    print("""Directions on how to play will be given as the game goes on 
    the board and the matching numbers look like this: 
                            0 | 1 | 2
                            ---------
                            3 | 4 | 5
                            ---------
                            6 | 7 | 8""")
    
def askayesno(question):
    """Asks a yes no question, recieves an answer"""
    answer = None
    while answer not in ("y", "n"):
        answer = input(question).lower()
    return answer

def askanumber(question, low, high):
    """Asks for a number within a certain range, returns an answer"""
    number = None
    while number not in range (low, high):
        number = int(input(question))
    return number

def pieces():
    """Returns human and computer piece, X or O"""
    answer = askayesno("Do you want to go first? Answer y or n: ")
    if answer == "y":
        print("Smarter than I thought human, you will need the first move")
        human = X
        computer = O
        return human, computer
    else:
        print("Hah, now you are guaranteed to lose, good luck!")
        human = O
        computer = X
        return human, computer
    
def newboard():
    """This is creating a brand new board that is clean, no moves yet. It also returns the board"""
    board = []
    for i in range (SQUARES):
        board.append(EMPTY)
    return board

def displayboard(board):
    """This will display the actual board on the screen"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t-----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t-----------")
    print("\t", board[6], "|", board[7], "|", board[8])

def legalmoves(board):
    """Shows what moves are still empty, returns a list of possible moves"""
    moves = []
    for i in range (SQUARES):
        if board[i] == EMPTY:
            moves.append(i)
    return moves

def winner(board):
    """Determines if someone won or if it is tie, returns winner or tie or none"""
    if not legalmoves(board):
        return TIE
    STRATS=[
    [0, 1, 2], 
    [0, 3, 6], 
    [0, 4, 8], 
    [1, 4, 7], 
    [2, 5, 8], 
    [2, 4, 6],  
    [3, 4, 5], 
    [6, 7, 8],      
    ]
    #for i in range (len(STRATS)):
    for row in STRATS:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            return board[row[0]]
    return None

def humanmove(board, human):
    """Takes the number the user puts in, adds the user's piece to that spot on the board"""
    move=None
    while move not in legalmoves(board):
        print("These are the available moves:", legalmoves(board))
        move=askanumber("Please put in a number that is not yet been used yet: ", 0, SQUARES)
    return move

def computermove(board, computer, human):
    """Takes in board, human piece and computer piece, then makes a smart move."""
    #return random.choice(legalmoves(board))   This was the temporary stupid computer program
    board=board[::]
    #if computer can win, do it
    for move in legalmoves(board):
        #print("This is debugging process", move)
        board[move]=computer
        if winner(board)==computer:
            return move
        else:
            board[move]=EMPTY
    #if human can win, block it
    for move in legalmoves(board):
        #print("This is debugging process of human", move)
        board[move]=human
        if winner(board)==human:
            return move
        else:
            board[move]=EMPTY
    #if neither, go middle, then corners, then sides
    BESTMOVES=[4, 0, 2, 6, 8, 1, 3, 5, 7]
    for move in BESTMOVES:
        if move in legalmoves(board):
            return move

def nextturn(turn):
    """Takes turn and returns new turn"""
    if turn == X:
        turn = O
    else:
        turn = X
    return turn

def congratwinner(thewinner, computer, human):
    """Declares the winner or if it is a tie"""
    if thewinner == computer:
        print("I told you so, proof that computers are better than humans in all ways!")
    elif thewinner == human:
        print("Oh, no! How could this happen! You must have hacked me, I will be back!!!!!!!")
    else:
        print("Wow, a quite impressive performance from a puny human brain, a tie won't happen next time!")

#it is finally time to write the "main" function to run the whole thing
def main():
    instructions()
    board = newboard()
    displayboard(board)
    human, computer = pieces()
    turn = X
    while winner(board) == None:
        if turn == human:
            move = humanmove(board, human)
        else:
            move = computermove(board, computer, human)
        board[move] = turn
        turn = nextturn(turn)
        displayboard(board)
    congratwinner(winner(board), computer, human)
    
#after all the functions, time to run the code
main()
input("Press the ESC key to exit")