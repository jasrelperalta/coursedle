#randomization

import random 
import calendar
from datetime import date
from codelist import dict_A_Z
from termcolor import colored
from colorama import Fore, Back, init


# initialize attempts and attempt array
n = 0
arr = []

init(autoreset=True)   

def main():
    mode = int(input("Choose game mode: "))
    start(mode, n, arr)

#start function from jas.py 
def start(mode, n, arr):

    if mode == 0:
        randomGame(n, arr)
    elif mode == 1:
        prepickGame(n, arr)
        
def check(n,arr,word,code_guess,code_random):
    for i in range(4):
            
            count = code_random.count(code_guess[i])
            
            if count > 0:
                #check if letter is in code word & right location              
                if code_guess[i] == code_random[i]:
                    print(Back.GREEN + ' ' + code_guess[i] + ' ' , end ='')
                else:
                    print(Back.YELLOW + ' ' + code_guess[i] + ' ' , end ='')
            else:
                #letter not in code word
                print(Back.RED + ' ' + code_guess[i] + ' ' , end='')
        
        
def randomGame(n, arr):
    
    #pick random course code from main list of all course codes
    
    letter = random.choice(list(dict_A_Z))                                                       
    word = random.choice(list(letter.keys()))

    #sample outputs     
    print("Sample chosen word:", word)
    print("Sample info: ", letter[word])
    
    while n<4:
        code_random = list(word)
        guess = str(input("\nEnter code: ")).upper()
        code_guess = list(guess)
        
        print(code_random, code_guess)
        letters = len(guess)
        
        n = n+1
        print(n)
        
        if code_guess == code_random:
            for i in range(4):
                print(Back.GREEN + ' ' + code_guess[i] + ' ' , end ='')
            print("\n call WIN")
            break
        else:
            while letters == 4:
                check(n,arr,word,code_guess,code_random)
                break
            else:
                print("Please enter 4 letter courses only.")
        
    else:
        print("\n call LOSE")
            
    
    end = int(input("\nEnd game mode: "))
    

def prepickGame(n, arr):
    
    today = date.today()
    day = str(calendar.day_name[today.weekday()])
    
    word = random.choice(list(globals()[day]))
    
    #sample outputs
    print("Sample chosen word:", word)
    print("Sample info: ", globals() [day] [word])
    
    while n<4:
        code_random = list(word)
        guess = str(input("\nEnter code: ")).upper()
        code_guess = list(guess)
        
        print(code_random, code_guess)
        letters = len(guess)
        
        n = n+1
        print(n)
        
        if code_guess == code_random:
            for i in range(4):
                print(Back.GREEN + ' ' + code_guess[i] + ' ' , end ='')
            print("\n call WIN")
            break
        else:
            while letters == 4:
                check(n,arr,word,code_guess,code_random)
                break
            else:
                print("Please enter 4 letter courses only.")
        
    else:
        print("\n call LOSE")
    
    
    end = int(input("\nEnd game mode: "))
    
    
    
main()
