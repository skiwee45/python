#backwards word code for practice
word=input("Type a random word that just popped into your mind: ")
backwardsword=""
print("the number of letter in your word is - ", len(word))
#print(word[0])
#print(word[6])
print("\t\t\t\t\tCount Backwards")
for i in range(len(word)-1,-1,-1):
     #print(word[i], end="")
     backwardsword+=word[i]

print(backwardsword)

print("v2: ", word[::-1])

print("v3", "".join(reversed(word)))