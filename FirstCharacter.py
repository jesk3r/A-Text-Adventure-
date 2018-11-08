from Player import *
import time


class FirstCharacter:

    charactername = "Torque"

    def __init__(self,player):

        self.CharacterName = "Torqe"
        self.player = player
        self.playername = player.getname()

    def givecharactername(self):
        return self.characterName

    def introdialog(self):


        print("{0}: YOUR AWAKE!".format(self.CharacterName))
        time.sleep(1)
        print("{0}: NO WAY, YOUR AWAKE!".format(self.CharacterName))
        time.sleep(1)
        print("{0}: Every body {1} is a awake".format(self.CharacterName,self.playername))
        time.sleep(1)
        print("Docter: What,how is even possible \n")


        for i in reversed(range(0,6)):
            print(i)

        print("\nSystem reboot complete")

        print("...what will you do...")
        print("1) Listen")
        print("2) Access Memory")
        print("3) Get up")
        print("4) Say something")


        Ans1 = input("Enter action id: ")

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


    def optlisten(self):
        self.player.addgoodrep()

    def optaccessmemory(self):
        counter = 0
        counter2 = 10
        while True:
            dot = "."
            print(dot * counter)
            counter += 1
            if counter == 10:
                break


        while True:
            dot = "."
            print(dot * counter2)
            counter2 -= 1

            if counter2 == 0:
                break

        print("Memory search complete")
        print("ability gained: syphin")

        self.player.addabilities(Player.syphin())





