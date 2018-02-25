scores = [("Moe", 1000), ("Larry", 1500), ("Curly", 3000)]
print(scores[0][::-1])

name = input("What is the player's name?: ")
score = int(input("What score did the player get?: "))
entry = (name, score)
scores.append(entry)
print("Appending the entry: ", scores)
scores.insert(len(scores), entry)
print("Inserting the entry: ", scores)
scores.remove(entry)
print("Now Removing your entry: ", scores)
del scores[len(scores)-1]
print("Deleting the last element: ", scores)

#Time to make a dictionary
derp={"Derp":"Hurp", "Harmandeep":"Harmanderp", "Raymond":"Skiwee", 
      "Skiwee":"Ramon noodles", "Pikaderp":"Derpachu"}


print("""
                     This is the DerpDICTIONARY!
            Please use one of the keys to retrieve a value.
            Press the enter key when you are done with the dictionary.
""")
user=input("""Put in a term to get the value in the derpdictionary
the terms are: Derp, Harmandeep, Raymond, Skiwee, Pikaderp
Which do you want to see first: 
""")

for item in derp.items():
    derp[item[0]]+=":)"
    print("This key and value pair is:", derp[item[0]])

for key in derp.keys():
    derp[key]+=":)"
    print(key, "means", derp[key])

#while user:
#    print("all the terms and definitions in the derpdictionary are -", derp.items())
#    print(derp.keys(), "\n", derp.values())#these methods are for getting all keys or all values
    #x=derp.get(user, ["Sorry, that was not in the derpdictionary, try another word"]), to get a value without checking if it is there because of the default
    #if user in derp:
        #print("In the derpdictionary, the term", user, "means:", derp[user])
    #else:
        #print("Sorry, that was not in the derpdictionary, try another word")
#    user=input("Put in a term to get the value: ")
 

   
input("Press the ESC key to exit")
