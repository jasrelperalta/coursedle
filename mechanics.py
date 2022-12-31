from colorama import Fore, Back, init #for the colors
from termcolor import colored
import textwrap as tw
import codelist

def modePick(day):
    print('─' * 80)
    modeText = ("Random: Pick random course code from main list of all course codes\nPre-pick: Pick random course code from the list of the day\nLIST OF THE DAY: codes starting with " + str(day))
    return modeText

def mainMenu():

    init(autoreset=True)    

    print('─' * 80)

    # trial design with colorama
    print(' ' + Back.GREEN + ' C ' + Back.YELLOW + ' O ' + Back.GREEN + ' U '
          + Back.YELLOW + ' R ' + Back.GREEN + ' S ' + Back.YELLOW + ' E '
          + Back.GREEN + ' D ' + Back.YELLOW + ' L ' + Back.GREEN + ' E ')
    
    # trial design with termcolor
    print(' ' + colored(' C ', 'white', 'on_green' ) + colored(' O ', 'white', 'on_yellow' )
          + colored(' U ', 'white', 'on_green' ) + colored(' R ', 'white', 'on_yellow' ) 
          + colored(' S ', 'white', 'on_green' ) + colored(' E ', 'white', 'on_yellow' )
          + colored(' D ', 'white', 'on_green' ) + colored(' L ', 'white', 'on_yellow' )
          + colored(' E ', 'white', 'on_green' ))

    print('─' * 80)

    intro_text = "COURSEDLE is a Wordle-inspired game made by AMAT 152 students for their Final Project. " \
          "It follows Wordle's basic mechanics with an added UPLB twist. Test how familiar you are to " \
          "UPLB's programs by guessing the given word which will be chosen from the different "\
           "4-letter codes of courses offered by the University."
           
    intro = tw.wrap(intro_text, width = 80)

    print("\n".join(intro))
    
    print('─' * 80)
    
    #print mechanics / instructions
    
    print('─' * 80)
    
    # trial design with colorama
    print(Back.WHITE + Fore.BLACK +'  MAIN MENU  ')
    
    # trial design with termcolor
    menu = colored('  MAIN MENU  ', 'green', 'on_white')
    
    print(' (1) START')
    print(' (2) RESUME')
    print(' (3) QUIT ')
    
    option = int(input('\nReady? (Input number of option): '))
    
    return option


#this is displayed before every code guessing
def coursedle_mechanics():
    print('─' * 80)
    print("YOU HAVE 4 ATTEMPTS TO GUESS THE CODE")
    print()
    print(colored("YELLOW", "yellow" ), end=" : ")
    print("Letter is in the code but in a wrong position")
    print(colored("RED", "red" ), end="    : ")
    print("Letter is not in the code")
    print(colored("GREEN", "green" ), end="  : ")
    print("Letter is in the correct position")
    print("\nInput 'SAVE' to save progress and quit.")
    print('─' * 80)

def saveGame():
    print(colored("\nGame saved successfully. Goodbye!","green"))

def winScreen(guessWord):
    print(colored("\nCONGRATULATIONS! YOU WON!", "green"))
    print("─" * 80)
    for item in codelist.dict_A_Z:
        for code, desc in item.items(): 
            if code == guessWord:
                print(colored(code, "blue"), end=": ")
                print(desc[0])
                print("\n".join(tw.wrap(desc[1], width=80)))
                
    print("─" * 80)
    print()
    key_press()
            
                
def loseScreen(guessWord):
    print(colored("\nYOU LOSE. BETTER LUCK NEXT TIME!", "red"))
    print("─" * 80)
    for item in codelist.dict_A_Z:
        for code, desc in item.items(): 
            if code == guessWord:
                print(colored(code, "blue"), end=": ")
                print(desc[0])
                print("\n".join(tw.wrap(desc[1], width=80)))
                
    print("─" * 80) 
    key_press()
 
def key_press():
    num_press = int(input(colored("Press [1] to go back to Main Menu or [0] to exit game: ", "yellow")))
    if num_press == 1:
        pass
    elif num_press == 0:
        print(colored("GOODBYE!", "green"))
        quit()
    else:
        print("Invalid Key. Try Again")
        key_press()