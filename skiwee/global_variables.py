def change_global():
    global value, v2
    value = v2 = -10
    print ("local value", value, v2)
    
value = 10
v2 = 1

change_global()
print("The global value now changes to -10:", value, v2)

input("Press the ESC key to exit")