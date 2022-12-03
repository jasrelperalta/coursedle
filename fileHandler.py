import os

def loadFile():
    path = 'savefile.txt'

    if os.path.exists(path):
        f = open(path, 'r')
        mode = f.readline().strip()
        numAttempts = f.readline().strip()
        attempts = f.readline().strip()
        letterAttempts = f.readline().strip()
        return mode, numAttempts, attempts, letterAttempts

def saveFile(mode, n, att, lett):
    path = 'savefile.txt'

    f = open(path, 'w')

    tempStr = str(mode) + '\n' + str(n) + '\n' + str(att) + '\n' + str(lett)
    f.write(tempStr)
    f.close()

# saveFile(1, 2, ['CMSC', 'AMAT'], ['C', 'M', 'S', 'A', 'T'])

# for i in loadFile():
#     print(i)