import lose_win_Screen as lws
import mechanics
import fileHandler
from colorama import Back, init


init(autoreset=True)   

# n = number of attempts
# arrAttempts = previous words na ininput
# letterAttempts = list of letters na ginamit before
# guessWord = word na huhulaan
def playGame(n, guessWord):
    # coursedle banner with colors
    mechanics.coursedle_mechanics()

    # print prev attempts if resume
        # padaanin sa check function

    while n < 4:
        # print # of attempts
        # get input // get upper
        # check
        # update array of attempts and n
        end = input("\n") # need 4 letters input
        if end == 'SAVE':
            fileHandler.saveFile(n, guessWord)
            quit()
        if end == guessWord:
            lws.winScreen(guessWord)
        check(end, guessWord)
        n += 1
    lws.loseScreen(guessWord)

'''#function moved to another file
def winScreen():
    print("u win lol")
    end = input("Press ENTER to continue")

def loseScreen():
    print("lose")
    end = input("Press ENTER to continue")
'''
    
        
def check(code_guess,code_random):
    if code_guess == code_random:
        for i in range(4):
            print(Back.GREEN + ' ' + code_guess[i] + ' ' , end ='')
    else:
        for i in range(4):
        
            # print(code_guess[i])
            count = code_random.count(code_guess[i])
            # print(count)
        
            if count > 0:
                #print(code_guess[i], 'exist')
                
                if code_guess[i] == code_random[i]:
                    print(Back.GREEN + ' ' + code_guess[i] + ' ' , end ='')
                else:
                    print(Back.YELLOW + ' ' + code_guess[i] + ' ' , end ='')
            
            else:
                #print(code_guess[i], 'does not exist')
                print(Back.RED + ' ' + code_guess[i] + ' ' , end='')
    