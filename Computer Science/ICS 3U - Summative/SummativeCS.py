# standard structures - may need to include different kinds under super class
class pokemonMaster():
    def __init__(self, name="", health=100, kind="", attackOne="", attackTwo="", attackThree=""):
        # if necessary try to include
        # default vals and list type
        self.name = name
        self.health = health
        self.kind = kind
        self.attackOne = attackOne
        self.attackTwo = attackTwo
        self.attackThree = attackThree

    def playerInfo(self):
        return 'Name:{} Health:{} Type:{} Attack 1:{} Attack 2:{} Attack 3:{}'.format(self.name,
                                                                                      self.health, self.kind,
                                                                                      self.attackOne, self.attackTwo,
                                                                                      self.attackThree)


class Player(pokemonMaster):
    def __init__(self, name, health, kind, attackOne, attackTwo, attackThree):
        # if necessary try to include
        # default values (must include all attributes) and list type
        super().__init__(name, health, kind, attackOne, attackTwo, attackThree)

        '''
        self.name = name
        self.health = health
        self.type = type
        self.attackOne = attackOne  # eventually condense into one list
        self.attackTwo = attackTwo
        self.attackThree = attackThree
        '''


'''
class Enemy(pokemonMaster)
    def __init__(self, name, health, type, attackOne, attackTwo, attackThree):
        # if necessary try to include
        # default values (must include all attributes) and list type
        super().__init__(self,name,health,type
                       ,attackOne,attackTwo,attackThree)
'''
playerOne = Player("Charmander",100, "Fire", "whip", "blaze", "shock")
print(playerOne.playerInfo())

# enemy = Enemy("Bulbasaur","Leaf", "vine", "levitate", "run away")
# print(enemy.playerInfo())
