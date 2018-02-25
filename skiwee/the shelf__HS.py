import shelve
def user():
    name=input("Put in your name: ")
    try:
        score=int(input("Put in your score: "))
    except:
        print("Sorry, you did not put in a whole number. Pls put in a whole number.")
    else:
        return name, score

def update(name, score):
    hs=shelve.open("HSHS.dat")
    hs[name]=str(score)
    hs.close()
    
def display():
    hs=shelve.open("HSHS.dat")
    print("The scoreboard is shown below:")
    for key in hs:
        print(key, ":", hs[key])
        
def main():
    name=None
    score=None
    while not name or not score:
        name, score=user()
    update(name, score)
    display()
    
main()