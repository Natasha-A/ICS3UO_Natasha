# CLASS OBJECTS
import random

class Pokemon():
    def __init__(self, name="", health=100, kind="", attackOne="", attackTwo="", attackThree=""):
        self.allPokemon = []
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

class Player(Pokemon):
    def __init__(self, name="", health=100, kind="", attackOne="", attackTwo="", attackThree=""):
        super().__init__(name, health, kind, attackOne, attackTwo, attackThree)


class Enemy(Pokemon):
    def __init__(self, name="", health=100, kind="", attackOne="", attackTwo="", attackThree=""):
        super().__init__(name, health, kind, attackOne, attackTwo, attackThree)

    #Enemy chooses pokemon at random
    def choosePokemon(self):
        pokemonChosen = random.choice(pokemons)

        nameOfPokemon = pokemonChosen.name

        print("The random choice chosen is", nameOfPokemon)

        return pokemonChosen

#LIST OF POKEMON - instances
charmander = Pokemon("Charmander", 100,"Fire", "whip", "blaze", "shock")
bulbasaur = Pokemon("Bulbasaur",100, "Leaf", "vine", "levitate", "run away")
squirtle = Pokemon("Squirtle",100, "hydro pump", "final smash", "triple finish")

pokemons = [charmander, bulbasaur, squirtle]

'''
1)	AI GENEREATES random Pokemon ():
•	CHOOSES from Pokemon Instances LIST (RANDOM)
•	PRINT AI's Pokemon chosen (indexed)
•	RETURN Pokemon chosen (INSTANCE)
'''

#create instance of an enemy - takes new enemy, and prints out it's information
enemyOne = Enemy()

enemyPokemon = Enemy.choosePokemon(enemyOne)

print(enemyPokemon.playerInfo()) #derives from Pokemon() object




