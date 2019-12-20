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

#LIST OF POKEMON - instances
charmander = Pokemon("Charmander", 100,"Fire", "whip", "blaze", "shock")
bulbasaur = Pokemon("Bulbasaur",100, "Leaf", "vine", "levitate", "run away")
squirtle = Pokemon("Squirtle",100, "Water", "hydro pump", "final smash", "triple finish")

pokemons = [charmander, bulbasaur, squirtle]

class Player(Pokemon):
    def __init__(self, name="", health=100, kind="", attackOne="", attackTwo="", attackThree=""):
        super().__init__(name, health, kind, attackOne, attackTwo, attackThree)

    def selectPokemon(self):
        checkPokemon = True

        for pokemonIndex in range(len(pokemons)):
            print(str(pokemonIndex+1) + ": " + pokemons[pokemonIndex].name)

        while checkPokemon:
            pokemonChosen = int(input("Choose a pokemon: "))
            try:
                if pokemonChosen > 0 and pokemonChosen <= (len(pokemons)):
                    return pokemons[pokemonChosen - 1] #print out pokemon at index of chosen pokemon (1,2,3)
                    checkPokemon = False
                else:
                    raise AssertionError
            except AssertionError:
                print("Incorrect input. Please enter the # for one of the pokemons above.")
                checkPokemon = True


class Enemy(Pokemon):
    def __init__(self, name="", health=100, kind="", attackOne="", attackTwo="", attackThree=""):
        super().__init__(name, health, kind, attackOne, attackTwo, attackThree)

    #Enemy chooses pokemon at random
    def randomPokemonSelected(self):
        pokemonChosen = random.choice(pokemons)

        nameOfPokemon = pokemonChosen.name

        print("The random choice chosen is", nameOfPokemon)

        return pokemonChosen

#ENEMY CHOOSES POKEMON: create instance of an enemy - takes new enemy, and prints out it's information
enemyOne = Enemy()
enemyPokemon = Enemy.randomPokemonSelected(enemyOne)
print(enemyPokemon.playerInfo()) #derives from Pokemon() object

#PLAYER CHOOSES POKEMON: create instance of an enemy - takes new enemy, and prints out it's information
print("\n")
humPlayer = Player()
playerPokemon = Player.selectPokemon(humPlayer)
print(playerPokemon.playerInfo())

