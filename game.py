import mechanics
from colorama import Back, init


init(autoreset=True)

# save game progress
def saveFile(n, word):
    path = 'savefile.txt'

    f = open(path, 'w')

    tempStr = str(n) + '\n' + str(word)
    f.write(tempStr)
    f.close()

# prints user attempt
def printAttempt(n):
    if n == 0:
        tempStr = "\n" + str(n+1) + "st attempt:\n"
    elif n == 1:
        tempStr = "\n" + str(n+1) + "nd attempt:\n"
    elif n > 1:
        tempStr = "\n" + str(n+1) + "th attempt:\n"
    return tempStr

# called when resume or new game
def playGame(n, guessWord):
    mechanics.coursedle_mechanics()

    while n < 4:
        guess = str(input(printAttempt(n))).upper() # need 4 letters input
        if len(guess) == 4:
            if guess == 'SAVE':
                saveFile(n, guessWord)
                mechanics.saveGame()
                quit()
            if guess == guessWord:
                mechanics.winScreen(guessWord)
                break
            check(guess, guessWord)
            n += 1
        else:
            print("Invalid input!")
    if n == 4:
        mechanics.loseScreen(guessWord)
    
# checking logic of attempts
def check(code_guess,code_random):
    if code_guess == code_random:
        for i in range(4):
            print(Back.GREEN + ' ' + code_guess[i] + ' ' , end ='')
    else:
        for i in range(4):
            count = code_random.count(code_guess[i])
        
            if count > 0:
                if code_guess[i] == code_random[i]:
                    print(Back.GREEN + ' ' + code_guess[i] + ' ' , end ='')
                else:
                    print(Back.YELLOW + ' ' + code_guess[i] + ' ' , end ='')
            
            else:
                print(Back.RED + ' ' + code_guess[i] + ' ' , end='')
    