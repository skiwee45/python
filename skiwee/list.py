# create a list with some items and display with a for loop
inventory = ["sword", "armor", "shield", "healing potion"]
print("Your items:")
for item in inventory:
    print(item)
    
# display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])    

# concatenate two lists
chest = ["gold", "gems"]
print("You find a chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

# assign by index
print("You trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your inventory is now:")
print(inventory)

#inventory[6]="an epic derp", you can only change existing elements of the list, not add new ones

# assign by slice
print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print("Your inventory is now:")
print(inventory)

#sort
inventory.sort(reverse=True)
print("this is the inventory after sorting - ", inventory)

# delete a slice
print("Your crossbow and armor are stolen by thieves.")
#del inventory[:2]
inventory.remove("crossbow")
to_del = "armorrrr"
if to_del in inventory: inventory.remove(to_del)

print("Your inventory is now:")
print(inventory)

for item in inventory:
    print("each item", item)


#appending list method
for i in range(3):
    inventory.append("a really long and derpy lasar gun")
print("\n\n\n", inventory)

#reversing list method
inventory.reverse()
print("\n", inventory)

#count how much derpy guns i got
print("\n\n", inventory.count("a really long and derpy lasar gun"))

#pop method in listing
pop=inventory.pop(0)
print("\n\n", pop)

input("\nPress the enter key to continue.")