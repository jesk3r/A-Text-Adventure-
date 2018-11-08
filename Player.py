from Startingworld import *

class Player:

    Name = ""
    goodrep = []
    badrep = []

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





