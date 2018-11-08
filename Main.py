from Player import *
from Startingworld import *

import time
import sys


def main():

    #init all objects that we need
    player = Player()
    player.givename("XDeath")
    sw = Startingworld(player)

    #start of the game
    Delay_msg("Wellcome to the world of",.05)
    print("\n\n")
    print("\t Chrono Crisis")

    time.sleep(5)
    Delay_msg("You wake up\nEvery thing is a haze",0.25)

    Delay_msg("type to say something",0.25)



    input()

    sw.SFirstCharacter()








def Delay_msg(text,speed):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(speed)




if __name__ == '__main__':
    main()