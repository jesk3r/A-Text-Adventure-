from FirstCharacter import *

class Startingworld:

    location = "Starting World" # Data type:Sring

    #init all the variables
    def __init__(self,player):
        self.playerinworld = player
        self.FirstCharacter = FirstCharacter(self.playerinworld)

    #retuns the name of the location
    def loction(self):
        return self.location

    #Starts talking with one of the characters in the world
    def SFirstCharacter(self):
        self.FirstCharacter.introdialog()



