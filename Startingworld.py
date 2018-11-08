from FirstCharacter import *

class Startingworld:

    location = "Starting World"

    def __init__(self,player):

        self.playerinworld = player.getname()
        self.FirstCharacter = FirstCharacter(self.playerinworld)

    def loction(self):
        return location

    def SFirstCharacter(self):
        self.FirstCharacter.introdialog()



