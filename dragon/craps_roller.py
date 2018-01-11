# Craps Roller

import random

# generate random number from 1 to 6
dice1 = random.randint(1, 6)
dice2 = random.randrange(6) + 1

print("You rolled a ", dice1, " and a", dice2, "for a total of", dice1+dice2)

input("\n\nPress any key to exit")