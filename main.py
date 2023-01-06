from codelist import dict_A_Z, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
from datetime import date
import mechanics, game, codelist
import os, calendar, random

# clears terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# determine if resume, random, prepick game mode
def newGame(mode, n, arrAttempts):
    if mode == 0:
        game.playGame(n, arrAttempts)
    elif mode == 1:
        randomGame()
    elif mode == 2:
        prepickGame()

# prints mechanics and today's list and picks game mode
def pickMode():
    choice = 0
    while choice != 1 or choice != 2:
        print(mechanics.modePick(codelist.listToday()))
        choice = input("\n[1] Random\n[2] Pre-pick\n\nPick a game mode: ")

        if len(choice) < 1 or not choice.isdigit():
            print("Invalid choice!\n")
            continue   

        choice = int(choice)
        if choice == 1 or choice == 2:
            choice = int(choice)
            break
        else:
            print("Invalid choice!\n")
    return choice

# loads existing saved game
def loadFile():
    path = 'savefile.txt'

    if os.path.exists(path):
        f = open(path, 'r')
        numAttempts = int(f.readline().strip())
        guessWord = f.readline().strip()
        return numAttempts, guessWord

# called in menu if player will resume
def resume():
    numAttempts, guessWord = loadFile()
    game.playGame(numAttempts, guessWord)


# pick random course code from main list of all course codes 
def randomGame():
    letter = random.choice(list(dict_A_Z))                                                       
    word = random.choice(list(letter.keys()))

    #sample outputs     
    # print("Sample chosen word:", word)
    # print("Sample info: ", letter[word])

    game.playGame(0, word)

# pick random course code from today's list
def prepickGame():
    today = date.today()
    day = str(calendar.day_name[today.weekday()])
    dayList = random.choice(list(globals()[day]))
    word = random.choice(list(dayList))

    game.playGame(0, word)


# user pick choice
while True:
    clear()
    choice = mechanics.mainMenu()
    while len(choice) < 1 or not choice.isdigit() or int(choice) > 3 or int(choice) == 0:
        print("Invalid choice!")
        choice = input('\nReady? (Input number of option): ')
    
    choice = int(choice)


    if choice == 1:
        mode = pickMode()
        newGame(mode, 0, [])
    elif choice == 2:
        resume()
    elif choice == 1:
        break
    else:
        print("Invalid choice!")
