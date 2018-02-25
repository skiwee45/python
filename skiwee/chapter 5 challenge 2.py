attributes={"strength":4, "health":5, "wisdom":8, "derpiness":15}
money=30
items=[]
print("""
                    Welcome to the Hero Creater Studios
            Please pick whether you want to buy(choice 0) or sell(choice 1) an attribute.
            The attributes are listed below
            strength-$4
            health-$5
            wisdom-$8
            derpiness-$15
            The game is over once you have used all your money or you have overspent.
            Press the enter key to quit.
""")
choice=None
while choice!="":
    print("\n\nYou have:", money, "dollars")
    print("You have:", items, "as your attributes")
    print("All available items and their matching prices are:", attributes, "\n\n")
    choice=input("Put in 0 for buying or 1 for selling: ")
    
    if choice=="0":
        x=None
        while x not in attributes:
            x=input("Which attribute do you want to buy: ")
            x=x.lower()
            
        if(money - attributes[x] < 0) :
            print("sorry - not enough fund to buy", x)
            continue
            
        money-=attributes[x]
        items.append(x)
        print("Transaction done, you spent", attributes[x], "dollars on", x)
        
    elif choice=="1":
        if not items:
            print("Sorry, you are itemless, you got nutting to sell!")
            continue
        
        y=None
        while y not in items:
            y=input("Which attribute do you want to sell: ")
            y=y.lower()
        money+=attributes[y]
        items.remove(y)
        print("\nTransaction done, you got", attributes[y], "dollars by selling", y)
    else:
        print("Unknown choice, choose again.")
    
if money<=0:
    print("Ahh, it looks like you have ran out of money")
    print("You ended up with", items)
    
else:
    print("Oohoho, it looks like somebody quit, remember, quiters never win\n and winners never quit!")
    print("Anyway, you ended up with these items:", items, "You also ended up with", money, "dollars")


input("Press the ESC key to exit")