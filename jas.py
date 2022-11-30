
# start
# expected input:
#   game mode:
#       0 = random
#       1 = pre-pick
#   empty counter and list

# expected output:
#   function call to game mode with initialized values

import os.path

# initialize attempts and attempt array
n = 0
arr = []

def start(mode, n, arr):

    if mode == 0:
        randomGame(n, arr)
    elif mode == 1:
        prepickGame(n, arr)



# resume
# expected input:
#   none
# expected output:
#   call to start




def resume():
    path = 'savefile.txt'

    if os.path.exists(path):
        f = open(path, 'r')
        mode = f.readline().strip()
        numAttempts = f.readline().strip()
        attempts = f.readline().strip()
        # start(mode, numAttempts, attempts)

        print(mode, numAttempts, attempts)

def randomGame(n, arr):
    pass

def prepickGame(n, arr):
    pass

resume()