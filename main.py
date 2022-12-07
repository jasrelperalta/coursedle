from termcolor import colored #example: print(colored("Hello". "yellow"))
import codelist, mechanics, menu, start
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')    # linux or windows

# user pick choice
while True:
    clear()
    choice = menu.mainMenu()

    if choice == 1:
        mode = start.pickMode()
        start.newGame(mode, 0, [])
    elif choice == 2:
        start.resume()
    elif choice == 3:
        break
    else:
        print("Invalid choice!")