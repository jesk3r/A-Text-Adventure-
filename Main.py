from Player import *
from Startingworld import *
import os
import time
import sys
import pygame

def main():

    #init all objects that we need
    player = Player()
    player.givename(input("Enter your name:"))

    sw = Startingworld(player)
    pygame.mixer.init()
    music = os.getcwd()
    pygame.mixer.music.load(music +"/DISTRICT 89' Best of Synthwave And Retro Electro Music Mix.mp3")
    pygame.mixer.music.play()
    #start of the game
    Delay_msg("Welcome to the world of",.05)
    print("\n\n")
    print("\t Chrono Crisis\n")

    time.sleep(4)

    Delay_msg("You wake up\nEvery thing is a haze",0.21)
    Delay_msg("\ntype to say something:\n",0.21)

    input()

    sw.SFirstCharacter()  # goes to the Starting world class method S



def Delay_msg(text,speed):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(speed)




if __name__ == '__main__':
    main()