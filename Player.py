from Startingworld import *

class Player:

    Name = ""
    goodrep = []
    badrep = []
    abilities = {"syphin":""}
    level = 0

    def __init__(self):
        pass


    def location(self,curlocation):
        self.location = curlocation

    def givelocation(self):
        return self.location

    def givename(self, Name):
        self.Name = Name

    def getname(self):
        return self.Name

    def addgoodrep(self):
        self.goodrep.append(1)

    def addbadrep(self):
        self.badrep.append(-1)

    def addabilities(self,name,abbilityfuntion):
        self.abilities[name] = abbilityfuntion

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

    def addlevel(self):
        self.level += 1




