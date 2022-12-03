import os.path

def loadFile():
    path = 'savefile.txt'

    if os.path.exists(path):
        f = open(path, 'r')
        mode = f.readline().strip()
        numAttempts = f.readline().strip()
        attempts = f.readline().strip()
        
        return mode, numAttempts, attempts

def saveFile(mode, n, att):
    path = 'savefile.txt'

    f = open(path, 'w')

    tempStr = str(mode) + '\n' + str(n) + '\n' + str(att)
    f.write(tempStr)
    f.close()

saveFile(1, 2, ['CMSC', 'AMAT'])