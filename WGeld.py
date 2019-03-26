"""WGeld - A fun game to practice calculating change."""
__version__ = "0.0.3"
__author__ = "Fereon"

import random
import time
import math

min, max = 800, 5000
lines = range(10)

def game():
    """Run the game."""
    print("Round\tTo Pay\tAvailable\tChange")
    cor = 0
    fal = 0
    nulltime, ctime = time.time(), time.time()
    for line in lines:
        topay = int((max-min)*random.random() + min)
        available = math.ceil((random.random()*(max-topay) + topay)/100)*100
        change = available - topay
        if input("{0!s}\t{1!s}\t{2!s}\t\t".format(line, topay/100, available/100)) == str(change/100) :
            cor = cor + 1
            print("Correct!\tLap : {!s} s".format(round(time.time() - ctime, 2)))
        else :
            fal = fal +1
            print("False!\tCorrect: {0!s}\tLap : {1!s} s".format(change/100, round(time.time() - ctime, 2)))
        ctime = time.time()
    print("Correct : {0!s}\tFalse : {1!s}\tTime : {2!s} s".format(cor, fal, round(ctime - nulltime, 2)))
    startgame()

def startgame():
    """Asks user whether game should be started."""
    if input("Start Game? (Y/N): ") == 'Y': game()
    else : quit()

print(__doc__ + "\t" + __version__ + "\t" + __author__)
startgame()