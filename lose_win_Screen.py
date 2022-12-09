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
    menu.mainMenu()          
                
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
    menu.mainMenu() 
 
#sample printing   
loseScreen("AMAT")


#problem: the info prints twice. idk why lol (fixed na)
