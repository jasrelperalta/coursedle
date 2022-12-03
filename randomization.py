#randomization

import random 
import calendar
from datetime import date
from codelist import dict_A_Z, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
from termcolor import colored


# initialize attempts and attempt array
n = 0
arr = []

def main():
    mode = int(input("Choose game mode: "))
    start(mode, n, arr)

#start function from jas.py for trial run
def start(mode, n, arr):

    if mode == 0:
        randomGame(n, arr)
    elif mode == 1:
        prepickGame(n, arr)
        
def randomGame(n, arr):
    
    #pick random course code from main list of all course codes
    
    letter = random.choice(list(dict_A_Z))                                                       
    word = random.choice(list(letter.keys()))

    #sample outputs     
    print("Sample chosen word:", word)
    print("Sample info: ", letter[word])

    end = int(input("End game mode: "))

def prepickGame(n, arr):
    
    today = date.today()
    day = str(calendar.day_name[today.weekday()])
    
    word = random.choice(list(globals()[day]))
    
    #sample outputs
    print("Sample chosen word:", word)
    print("Sample info: ", globals() [day] [word])
    
    end = int(input("End game mode: "))
    
    
main()
