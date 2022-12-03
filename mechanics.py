#This is a function for mechanics
from termcolor import colored

#this is displayed before every code guessing
def coursedle_mechanics():
    print("YOU HAVE 4 ATTEMPTS TO GUESS THE CODE")
    print()
    print(colored("YELLOW", "yellow" ), end=" : ")
    print(" A letter is in the code but in a wrong position")
    print(colored("RED", "red" ), end="    : ")
    print(" A letter is not in the code")
    print(colored("GREEN", "green" ), end="  : ")
    print(" A letter is in the correct position")
    print(colored("BLUE", "blue" ), end="   : ")
    print(" Correct Answer")
    pass
    
    #Yellow: A letter is in the code but in a wrong position
    #Red: A letter is not in the word
    #Green: A letter is in the correct position
    #Blue: Correct Answer
    
#test/sample function call
# coursedle_mechanics()