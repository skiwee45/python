def derp(thederp):
    print("And", thederp, "was the greatest derpiest, hurpiest derp of all derps!")
    print(thederp, ", he was so great, but so derpy!")
    print("We will remember him forever!")
    
def askayesno(question="Looks like the dude making dis program forgot to put in something, so I'll just derp around and wait."):
    response=None
    while response not in ("y", "n"):
        response=input(question).lower()
    return response

def main():
    derp("Raymonderp")
    answer=askayesno("Put in y for yes or n for no(This is a useless dumb question): ")
    print("That u for entering", answer, "and thank you for answering a useless question")

#now we show the program
main()