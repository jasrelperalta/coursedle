import game
from termcolor import colored
import codelist
import menu


def winScreen(guessWord):
    print(colored("CONGRATULATIONS! YOU WON!", "green"))
    print("-" * 100)
    for item in codelist.dict_A_Z:
        for code, desc in item.items(): 
            if code == guessWord:
                print(colored(code, "blue"), end=": ")
                print(desc[0])
                print(desc[1])
                
    print("-" * 100)
    print()
    key_press()
            
                
def loseScreen(guessWord):
    print(colored("YOU LOSE. BETTER LUCK NEXT TIME!", "red"))
    print("-" * 100)
    for item in codelist.dict_A_Z:
        for code, desc in item.items(): 
            if code == guessWord:
                print(colored(code, "blue"), end=": ")
                print(desc[0])
                print(desc[1])
                
    print("-" * 100) 
    key_press()
 
def key_press():
    num_press = int(input(colored("Press [1] to go back to Main Menu or [0] to exit game: ", "yellow")))
    if num_press == 1:
        menu.mainMenu()  
    elif num_press == 0:
        print(colored("GOODBYE!", "green"))
        print()
    else:
        print("Invalid Key. Try Again")
        key_press()
        
#sample printing   
loseScreen("AMAT")


#problem: the info prints twice. idk why lol (fixed na)
