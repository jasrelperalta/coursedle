import os

def loadFile():
    path = 'savefile.txt'

    if os.path.exists(path):
        f = open(path, 'r')
        numAttempts = int(f.readline().strip())
        guessWord = f.readline().strip()
        return numAttempts, guessWord

def saveFile(n, word):
    path = 'savefile.txt'

    f = open(path, 'w')

    tempStr = str(n) + '\n' + str(word)
    f.write(tempStr)
    f.close()


for i in loadFile():
    print(i)