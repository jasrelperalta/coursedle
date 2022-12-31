
#main menu
#can add design later for extra smth 

from colorama import Fore, Back, init #for the colors
import textwrap as tw #wrap text - can change width if needed
from termcolor import colored

def mainMenu():

#     init(autoreset=True)    

    print('─' * 50)

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

    print('─' * 50)

    intro_text = "COURSEDLE is a Wordle-inspired game made by AMAT 152 students for their Final Project. " \
          "It follows Wordle's basic mechanics with an added UPLB twist. Test how familiar you are to " \
          "UPLB's programs by guessing the given word which will be chosen from the different "\
           "4-letter codes of courses offered by the University."
           
    intro = tw.wrap(intro_text, width = 50)

    print("\n".join(intro))
    
    print('─' * 50)
    
    #print mechanics / instructions
    
    print('─' * 50)
    
    # trial design with colorama
    print(Back.WHITE + Fore.BLACK +'  MAIN MENU  ')
    
    # trial design with termcolor
    menu = colored('  MAIN MENU  ', 'green', 'on_white')
    
    print(' (1) START')
    print(' (2) RESUME')
    print(' (3) QUIT ')
    
    option = int(input('\nReady? (Input number of option): '))
    
    # if option == 1:
    #     #start 
    #     print('start')
    # elif option == 2:
    #     #resume
    #     print('resume')
    # elif option == 3:
    #     #exit
    #     print('exit')

    return option

# mainMenu()