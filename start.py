import codelist, fileHandler
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

def newGame(mode, n, arr):
    if mode == 0:
        pass        # to game.py
    elif mode == 1:
        randomGame(n, codelist.code_random)
    elif mode == 2:
        today = datetime.now().strftime('%A')       # returns weekday
        prepickGame(n, today)

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


def randomGame(n, arr):
    # pass to game
    pass

def prepickGame(n, day):
    # pass to game
    pass