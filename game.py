import mechanics
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')    # linux or windows



def playGame(n, arrAttempts, letterAttempts, guessWord):
    clear()
    mechanics.coursedle_mechanics()

    # function that prints yung mga nahulaan na
    # function that prints yung alphabet + color red yung ginamit na before // check if already in letter attempts
    
    # function that kukuha ng input
    # function that updates yung array of attempts and letters
    # function that checks yung mga tamang letters ng user
    # if tama, show win screen, then main menu
    # elif mali but n < 4, call another instance ng playgame with updated arrays
    # elif mali n == 4 na, show lose screen, then main menu
    print(guessWord)
    end = input("End")