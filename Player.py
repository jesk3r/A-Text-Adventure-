from Startingworld import *

class Player:

    Name = ""
    goodrep = []
    badrep = []
    abilities = {"syphin":""}
    level = 0

    def __init__(self):
        pass

    #sets location of player
    def location(self,curlocation):
        self.location = curlocation

    #returns location of player
    def givelocation(self):
        return self.location

    #sets the players name
    def givename(self, Name):
        self.Name = Name

    #returns the players name
    def getname(self):
        return self.Name

    #adds good rep
    def addgoodrep(self):
        self.goodrep.append(1)

    #adds bad rep
    def addbadrep(self):
        self.badrep.append(-1)

    #adds to the ability list
    def addabilities(self,name,abbilityfuntion):
        self.abilities[name] = abbilityfuntion

    #An animation for syphin
    def syphin(self):
        print("             *               *   ")
        print("              *               *   ")
        print("              *               *   ")
        print("             *               *   ")
        print("              *               *   ")
        print("              *               *   ")
        print("             *               *   ")
        print("              *               *   ")
        print("              *               *   ")

        print("you have syphined")

    #adds levels
    def addlevel(self):
        self.level += 1




