inventory=("derp", "hurp", "derpahurp", "pikaderp")

#now I will print the tuple inventory
print("\n\nThe tuple inventory is- ", inventory)

#now I will print the tuple inventory element by element
print("\n\nEach Item Is- ")
for item in inventory: 
    print(item)
    

epicallysuperdupermagicalchest=("1 trillion $$$$", "5 megatons of diamonds", "a derp")
print(epicallysuperdupermagicalchest)

print("Now I will add all of that stuff to my inventory")

inventory+= epicallysuperdupermagicalchest

#inventory[0]="derpahurpaderpahurpaderp", this doesn't work with tuples, it can't be changed

#del inventory[2], you can't delete elements in tuples

print("My new inventory is- ", inventory)

input("\n\n\t\t\tPress ESC key to exit")