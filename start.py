import codelist, fileHandler, game
from datetime import datetime


# newGame
# expected input:
#   game mode:
#       0 = resume
#       1 = random
#       2 = pre-pick
#   empty counter and list

# expected output:
#   function call to game mode with initialized values

def newGame(mode, n, arrAttempts):
    # resume game using save file
    if mode == 0:
        game.playGame(n, arrAttempts)        # to game.py

    # initialize new game
    elif mode == 1:
        randomGame()
    elif mode == 2:
        prepickGame()

# pickMode
# expected input:
#  user input
# expected output:
#  game mode
def pickMode():
    choice = int(input("\n[1] Random\n[2] Pre-pick\nPick a game mode: "))
    if choice == 1 or choice == 2:
        return choice
    else:
        print("Invalid game mode!")
        pickMode()

# resume
# expected input:
#   none
# expected output:
#   call to start
def resume():
    fileHandler.loadFile()
    # pass to game
    pass


# TODO - Change "TRYZ" "TRYX" to random key from list

def randomGame():
    game.playGame(0, [],"TRYZ")

def prepickGame():
    today = datetime.now().strftime('%A')       # returns weekday
    game.playGame(0, [],"TRYX")