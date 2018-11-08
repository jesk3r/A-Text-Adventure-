from FirstCharacter import *

class Startingworld:

    location = "Starting World"

    def __init__(self,player):
        self.playerinworld = player
        self.FirstCharacter = FirstCharacter(self.playerinworld)

    def loction(self):
        return self.location

    def SFirstCharacter(self):
        self.FirstCharacter.introdialog()



