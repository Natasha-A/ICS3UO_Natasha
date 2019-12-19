
#standard structures - may need to include different kinds under super class
class Player():
    def __init__(self, name="", health=100, type="", attackOne="", attackTwo="", attackThree=""): #if necessary try to include
        # default vals and list type
        self.name = name
        self.health = health
        self.type = type
        self.attackOne = attackOne
        self.attackTwo = attackTwo
        self.attackThree = attackThree


    def playerInfo(self):
        return 'Name:{} Health:{} Type:{} Attack 1:{} Attack 2:{} Attack 3:{}'.format(self.name,
                                            self.health, self.type, self.attackOne, self.attackTwo, self.attackThree)

class Enemy(Player):#inherits from super class of Player() UNFINISHED 
    def __init__(self, name="", health=100, type="", attackOne="", attackTwo="", attackThree=""):  # if necessary try to include
        # default values (must include all attributes) and list type
        self.name = name
        self.health = health
        self.type = type
        self.attackOne = attackOne  # eventually condense into one list
        self.attackTwo = attackTwo
        self.attackThree = attackThree

    def playerInfo(self):
        return 'Name:{} Health:{} Type:{} Attack 1:{} Attack 2:{} Attack 3:{}'.format(self.name,
                                                                                      self.health, self.type,
                                                                                      self.attackOne, self.attackTwo,
                                                                                      self.attackThree
playerOne = Player("Charmander", "Fire","whip","blaze","shock")
print(playerOne.playerInfo())

enemy = Enemy("Bulbasaur","Leaf", "vine", "levitate", "run away")
print(enemy.playerInfo())






