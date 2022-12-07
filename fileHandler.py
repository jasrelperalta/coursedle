import os

def loadFile():
    path = 'savefile.txt'

    if os.path.exists(path):
        f = open(path, 'r')
        numAttempts = f.readline().strip()
        attempts = f.readline().strip()
        letterAttempts = f.readline().strip()
        guessWord = f.readline().strip()
        return numAttempts, attempts, letterAttempts, guessWord

def saveFile(n, att, lett, word):
    path = 'savefile.txt'

    f = open(path, 'w')

    tempStr = str(n) + '\n' + str(att) + '\n' + str(lett) + '\n' + str(word)
    f.write(tempStr)
    f.close()

saveFile(2, ['CMSC', 'AMAT'], ['C', 'M', 'S', 'A', 'T'], "THEA")

for i in loadFile():
    print(i)