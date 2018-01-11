# mood computer
import random

print("I sense your energy. Your true emputins are coming across my screen.")
print("You are ...")

mood = random.randint(1,3)

if mood == 1:
    # happy
    print("""
    -----------
    |         |
    |  O   O  |
    |    <    |
    |         |
    | .     . |
    |  `...`  |
    -----------
    """)
elif mood == 2:
    # neutral
    print("""
    -----------
    |         |
    |  O   O  |
    |    <    |
    |         |
    | ....... |
    |         |
    -----------
    """)
elif mood == 3:
    # sad
    print("""
    -----------
    |         |
    |  O   O  |
    |    <    |
    |         |
    |   ...   |
    | .`   `. |
    -----------
    """)    
else:
    print("illegal mode")
    
input("\n\nPress any key to exit.")