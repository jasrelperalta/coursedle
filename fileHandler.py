import os

def loadFile():
    path = 'savefile.txt'

    if os.path.exists(path):
        f = open(path, 'r')
        numAttempts = int(f.readline().strip())
        attempts = f.readline().strip()
        guessWord = f.readline().strip()
        return numAttempts, attempts, guessWord

def saveFile(n, att, word):
    path = 'savefile.txt'

    f = open(path, 'w')

    tempStr = str(n) + '\n' + str(att) + '\n' + str(word)
    f.write(tempStr)
    f.close()

saveFile(2, ['CMSC', 'AMAT'], "THEA")

for i in loadFile():
    print(i)