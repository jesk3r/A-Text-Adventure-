from Player import *
import time


class FirstCharacter:

    charactername = "Torque"

    def __init__(self,Name):

        self.CharacterName = "Torqe"
        self.playername = Name

    def givecharactername(self):
        return self.characterName

    def introdialog(self):


        print("{0}: YOUR AWAKE!".format(self.CharacterName))
        time.sleep(1)
        print("{0}: NO WAY, YOUR AWAKE!".format(self.CharacterName))
        time.sleep(1)
        print("{0}: Every body {1} is a awake".format(self.CharacterName,self.playername))
        time.sleep(1)
        print("Docter: How is even possible")

        print("Systems online")
        print("...what will you do...")
        print("1) Listen")
        print("2) Access Memory")
        print("3) Get up")
        print("4) Say something")


        Ans1 = input("Enter action id")

        if Ans1 == "1":
            pass
        elif Ans1 == "2":
            pass
        elif Ans1 == "3":
            pass
        elif Ans1 == "4":
            pass
        else:
            print("action id invalid")