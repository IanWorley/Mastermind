# Ian Worley /1/16/2021 4.6 Exercise B
import sys
import random
import termcolor
code = []
user_attempted = []
res = []
trys_took = 0 

termcolor.cprint("Welcome to game of mastermind")

def make_code(length_code=4):
    for i in range(length_code):
        num = random.randint(1, 9)
        code.append(num)


make_code()


def compare():
    """
Compare
This compares the code with what the user typed in.Tells if user got a number in the wrong place or right place.
    """
    if user_attempted == code:
        termcolor.cprint("You Win", "green")
        termcolor.cprint(F"It took you {trys_took} to guess the code.")
        sys.exit(0)
    else:
        for l, number in enumerate(user_attempted):
            if number == code[l]:
                termcolor.cprint(F"OK! {number}", "green")
                user_attempted[l] = 0
            elif number in code:
                termcolor.cprint(F"Not in right place: {number}", "cyan")
                user_attempted[l] = 0
            else:
                print(F"not found: {number}")

    # resets the list
    user_attempted.clear()


def guess(**kwargs):
    """ guess 
    Give the user chance to make a guess.
    """
    for i in range((kwargs["guesses"])):
        for j in range((kwargs["length"])):
            num = int(input("Put a number in here 1-9: "))
            user_attempted.append(num)
        global trys_took 
        trys_took += 1 
        compare()
        
    termcolor.cprint(F"You lose it took you {trys_took} trys. ", "red")


guess(guesses=3, length=4)
