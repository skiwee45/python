#show a slice with the word pizza
print("""
                       I Will Now Let U Slice A Pizza!
""")
word="pizza"
start = int(input("\nEnter a number to begin the slice: "))
finish = int(input("\nEnter another number to end the slice: "))
print("\npizza slice-", start, ":", finish, "is", end="  ")
print(word[start:finish])

input("\n\n\nPress the ESC key to exit")