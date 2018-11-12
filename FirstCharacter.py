from Player import *
import time


class FirstCharacter:

    charactername = "Torque"

    #init the varables
    def __init__(self,player):

        self.CharacterName = "Torqe"
        self.player = player
        self.playername = player.getname()

    #returns the characets name
    def givecharactername(self):
        return self.characterName

    #The starting dialog for the character
    def introdialog(self):


        print("{0}: YOUR AWAKE!".format(self.CharacterName))
        time.sleep(1)
        print("{0}: NO WAY, HOW ARE YOU AWAKE!".format(self.CharacterName))
        time.sleep(1)
        print("{0}: Every body {1} is a awake".format(self.CharacterName,self.player.getname()))
        time.sleep(1)
        print("Docter: What,how is this even possible \n")
        time.sleep(1)

        #counts back wards from 5
        for i in reversed(range(0,6)):
            print(i,flush=True)
            time.sleep(1)

        print("\nSystem reboot complete")
        time.sleep(1)
        print("...what will you do...")
        print("1) Listen")
        print("2) Access Memory")
        print("3) Get up")
        print("4) Say something")


        Ans1 = input("Enter action id: ")

        #cheaks the if the ans matches
        while True or False:
            if Ans1 == "1":
                print("you decided to listen")
                self.optlisten()
                break
            elif Ans1 == "2":
                print("your have accessed your memory")
                self.optaccessmemory()
                break
            elif Ans1 == "3":
                print("Servo failure")
                print("Magnetic interference")
                time.sleep(2)
                self.optlisten()
            elif Ans1 == "4":
                print("Firmware failure")
                print("Magnetic interference")
                time.sleep(2)
                self.optlisten()
            else:
                print("action id invalid")

    #the option to listen
    def optlisten(self):
        self.player.addgoodrep()
        print("you got good rep")

        print("{0}: We don't know if you remember this but, your a time traveller cyborg sent to fight in the chrono war.".format(self.CharacterName))
        time.sleep(1)
        print("{0}: The war has been going on forever, its a fixed point in time.It cant be changed, well, that's what we though.".format(self.CharacterName))
        time.sleep(1)
        print("{0}: The timeline has changed, its collapsing.".format(self.CharacterName))
        time.sleep(1)
        print("{0}: Your the only one who has come back from the time wars.".format(self.CharacterName))
        time.sleep(1)
        print("{0}: You need to stop the collapsing,".format(self.CharacterName))
        time.sleep(1)
        print("{0}: if we don't stop the time lines form collapsing, I'm afraid to say that we will all be dead".format(self.CharacterName))

        print("{0}: Will you do this for us\n".format(self.CharacterName))

        print("Action request")
        print("1) Yes i will")
        print("2) No ")

        #Ask again if the input is in valid
        while True and True:
            Ans1 = input("Enter action id: ")

            if Ans1 == "1" and True == True:
                print("Thank you for playing my demo")
                break
            elif Ans1 == "2":
                print("Thank you for playing my demo")
                break
            else:
                print("action id invalid")

    #the option for using syphin
    def optusesyphin(self):
        print("charging syphin")
        time.sleep(1)
        self.player.syphin()# does the animation for abillity
        time.sleep(1)
        print("\nyou used syphin")
        print("you gained bad rep")
        self.player.addbadrep()#add bad rep

        print("Computer Voice: There's a blinding flash of light,as you look around the room you see what you actions have done")
        time.sleep(3)
        print("Computer Voice: Every one was dead lying on the floor")
        time.sleep(1)
        print("you feel the power growing")
        time.sleep(1)
        print("You subsystems come online")
        time.sleep(1)
        print("Thank you for playing my demo")


    def optaccessmemory(self):
        counter = 0
        counter2 = 10

        #does an animation
        while True:
            dot = "."
            print(dot * counter)
            counter += 1
            if counter == 10:
                break

        #does another animation
        while True or False:
            dot = "."
            print(dot * counter2)
            counter2 -= 1

            if counter2 == 0:
                break

        print("Memory search complete")
        time.sleep(1)
        print("ability gained: syphin")
        time.sleep(1)
        self.player.addabilities("syphin",self.player.syphin)
        self.player.addlevel()
        time.sleep(1)

        print("Action request \nPlease enter action id: ")
        print("1) Listen")
        print("2) Use syphin")
        print("3) Get up")
        print("4) Say something")

        #Ensures that the users acctions doesn't stop the program
        while True:
            Ans1 = input("Enter action id: ")

            if Ans1 == "1":
                self.optlisten()
                break
            elif Ans1 == "2":
                self.optusesyphin()
                break
            elif Ans1 == "3":
                print("Servo failure")
                print("Magnetic interference")
                time.sleep(2)
                self.optlisten()
                break
            elif Ans1 == "4":
                print("Firmware failure")
                print("Magnetic interference")
                time.sleep(2)
                self.optlisten()
                break
            else:
                print("action id invalid")
                continue