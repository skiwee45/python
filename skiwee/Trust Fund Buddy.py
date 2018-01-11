print("""


                Trust Fund Buddy Trial Program
                
A trial to see if I can use the techniques shown in the book

I will use fruits instead of rich people items.

Please state in dollar amounts how much you usually spend on the following items in a average shopping trip. Press enter to see the next fruit.

""")
apple=int(input("Apples-"))
banana=int(input("Bananas-"))
orange=int(input("Oranges-"))
pear=int(input("Pears-"))
grape=int(input("Grapes-"))
peach=int(input("Peaches-"))
total=apple+banana+orange+pear+grape+peach
print("\n\nTotal Cost Of Fruits Per Week-", total)
print("Total Cost Of Fruits Per Year-", total*52)
input("\n\n\nPress The Escape Key To Exit")