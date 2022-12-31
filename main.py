from codelist import dict_A_Z, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
from datetime import date
import mechanics, game, codelist
import os, calendar, random
import textwrap as tw

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')    # linux or windows

def newGame(mode, n, arrAttempts):
    # resume game using save file
    if mode == 0:
        game.playGame(n, arrAttempts)

    # initialize new game
    elif mode == 1:
        randomGame()
    elif mode == 2:
        prepickGame()


def pickMode():
    choice = 0
    while choice != 1 or choice != 2:
        print(mechanics.modePick(codelist.listToday()))
        choice = int(input("\n[1] Random\n[2] Pre-pick\n\nPick a game mode: "))
        if choice == 1 or choice == 2:
            break
    return choice

def loadFile():
    path = 'savefile.txt'

    if os.path.exists(path):
        f = open(path, 'r')
        numAttempts = int(f.readline().strip())
        guessWord = f.readline().strip()
        return numAttempts, guessWord


def resume():
    numAttempts, guessWord = loadFile()
    game.playGame(numAttempts, guessWord)


def randomGame():
    # pick random course code from main list of all course codes 
    letter = random.choice(list(dict_A_Z))                                                       
    word = random.choice(list(letter.keys()))

    #sample outputs     
    # print("Sample chosen word:", word)
    # print("Sample info: ", letter[word])

    game.playGame(0, word)

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

    if choice == 1:
        mode = pickMode()
        newGame(mode, 0, [])
    elif choice == 2:
        resume()
    elif choice == 3:
        break
    else:
        print("Invalid choice!")
