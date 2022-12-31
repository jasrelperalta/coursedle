import lose_win_Screen as lws
import mechanics
import fileHandler
from colorama import Back, init


init(autoreset=True)   

# n = number of attempts
# guessWord = word na huhulaan
def playGame(n, guessWord):
    mechanics.coursedle_mechanics()

    while n < 4:
        end = input("\n") # need 4 letters input
        if len(end) == 4:
            if end == 'SAVE':
                fileHandler.saveFile(n, guessWord)
                quit()
            if end == guessWord:
                lws.winScreen(guessWord)
                break
            check(end, guessWord)
            n += 1
        else:
            print("Invalid input!")
    if n == 4:
        lws.loseScreen(guessWord)

    
        
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
    