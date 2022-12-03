import fileHandler, game, random, calendar
from codelist import dict_A_Z, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
from datetime import date


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


def randomGame():
# from randomization.py (GAGI DI KO PALA NAKITA SORRY MY BAD)
    # pick random course code from main list of all course codes 
    letter = random.choice(list(dict_A_Z))                                                       
    word = random.choice(list(letter.keys()))

    #sample outputs     
    # print("Sample chosen word:", word)
    # print("Sample info: ", letter[word])

    game.playGame(0, [], [], word)

def prepickGame():
    today = date.today()
    day = str(calendar.day_name[today.weekday()])
    
    word = random.choice(list(globals()[day]))
    game.playGame(0, [], [], word)