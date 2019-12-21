# CLASS OBJECTS
import random

class Pokemon():
    def __init__(self, name="None", health=100, kind="None", attackOne="None", attackTwo="None", attackThree="None"):
        self.allPokemon = []
        self.name = name
        self.health = health
        self.kind = kind
        self.attackOne = attackOne
        self.attackTwo = attackTwo
        self.attackThree = attackThree

    def playerInfo(self):
        return '* Player Info *\nName: {}\nHealth: {}\nType: {}\nAttack 1: {}\nAttack 2: {}\nAttack 3: {}\n'.format(self.name,
                                                                                      self.health, self.kind,
                                                                                      self.attackOne, self.attackTwo,
                                                                                      self.attackThree)
# LIST OF POKEMON - instances
charmander = Pokemon("Charmander", 100, "Fire", "Flamethrower", "Fire Spin", "Cast Inferno")
bulbasaur = Pokemon("Bulbasaur", 100, "Grass", "Vine Whip", "Leech Seed", "Cast Razor Leaf")
squirtle = Pokemon("Squirtle", 100, "Water", "Rapid Spin", "Aqua Tail", "Cast Hydro Pump")

pokemons = [charmander, bulbasaur, squirtle]


class Player(Pokemon):
    def __init__(self, name="None", health=100, kind="None", attackOne="None", attackTwo="None", attackThree="None"):
        super().__init__(name, health, kind, attackOne, attackTwo, attackThree)

    def selectPokemon(self):
        checkPokemon = True

        for pokemonIndex in range(len(pokemons)):
            print(str(pokemonIndex + 1) + ": " + pokemons[pokemonIndex].name)

        while checkPokemon:
            try:
                pokemonChosen = int(input("Choose a pokemon: "))
                if pokemonChosen > 0 and pokemonChosen <= (len(pokemons)):
                    return pokemons[pokemonChosen - 1]  # print out pokemon at index of chosen pokemon (1,2,3)
                    checkPokemon = False
                else:
                    raise AssertionError

            except AssertionError:
                print("Incorrect input. Please enter the # for one of the pokemons above.")
                checkPokemon = True
            except ValueError:
                print("Incorrect value type. Please enter one of the numbers above.")

class Enemy(Pokemon):
    def __init__(self, name="", health=100, kind="", attackOne="", attackTwo="", attackThree=""):
        super().__init__(name, health, kind, attackOne, attackTwo, attackThree)

    # Enemy chooses pokemon at random
    def randomPokemonSelected(self):
        pokemonChosen = random.choice(pokemons)

        nameOfPokemon = pokemonChosen.name

        print("The random choice chosen is", nameOfPokemon)

        return pokemonChosen

def playerAttack(pChosenPokemon):
    checkAttack = True
    # playerPokemon - assigns parameter as chosen pokemon object
    # able to called repeatedly for player to attack during battle on turn
    attack1 = pChosenPokemon.attackOne
    attack2 = pChosenPokemon.attackTwo
    attack3 = pChosenPokemon.attackThree
    attackList = [attack1, attack2, attack3]

    #Display attacks for chosen Pokemon for current battle
    for attackIndex in range(len(attackList)):
        print(str(attackIndex + 1) + ":", attackList[attackIndex])

    #check for correct INPUT for attack:
    while checkAttack:
        try:
            attackChosen = int(input("Choose an attack: "))
            if attackChosen > 0 and attackChosen <= (len(attackList)):
                print("Attack chosen:", attackList[attackChosen - 1])
                checkAttack = False
                #return attackList[attackChosen - 1]  # print out pokemon at index of chosen pokemon (1,2,3)
            else:
                raise AssertionError

        except AssertionError:
            print("Incorrect input. Please enter one  of the attacks above.")
            checkAttack = True
        except ValueError:
            print("Incorrect value type. Please enter one of the #'s above.")

    # PROCESS behind attack effect on health and damage to other pokemon - (turn into sep. func)

    # Moderate Damage:
    if attackChosen == 1:
        attackDamage = random.randint(18, 25)
        newEnmyHealth = enemyPokemon.health - attackDamage # reduces enemy's health by amount
        enemyPokemon.health = newEnmyHealth
        if attackDamage >= 20:
            print("The attack is very effective!")
        # attack is 19 or below
        else:
            print("The attack is not very effective...")

        print("You have decreased the enemy's health by:", attackDamage, "to:", newEnmyHealth)

    # High Range Damage:
    elif attackChosen == 2:
        attackDamage = random.randint(10, 35)
        newEnmyHealth = enemyPokemon.health - attackDamage  # reduces enemy's health by amount
        enemyPokemon.health = newEnmyHealth

        if attackDamage >= 30:
            print("The attack is extremely effective!")
        elif attackDamage >= 20:
            print("The attack is very effective!")
        else:
            print("The attack is not very effective...")

        print("You have decreased the enemy's health by:", attackDamage, "to:", newEnmyHealth)

    '''
    #CAST - increase player's hp by moderate amount 
    elif attackChosen == 3:
        attackDamage = random.randint()
    '''










'''
#Either player or enemy's turn in the battle. (CURRENT ATTACK) 
#take's player's chosen pokemon and extracts attacks

Attack Chosen (attk):

DECISIONS:
•	IF chooses FIRST attack:
	Moderate DAMAGE randomly assigned (18-25 HP)
	Opponent's HP DECREASES by DAMAGE

IF chooses SECOND attack:
	High Range DAMAGE randomly chosen (10 - 35 ) to opponent's HP
	Opponent's HP DECREASES by DAMAGE

If chooses THIRD attack:
	PRINT cast has been called
	CAST randomly assigned moderate amount  (18-25 HP)
	Player's HP increases by CAST

IF DAMAGE is GREATER than 20:
	PRINT attack is effective
•	ELSE:
	PRINT attack not effective

PRINT player's HEALTH and opponent's HEALTH
RETURN Player's HEALTH and Opponent's HEALTH

'''








#MAIN PROGRAM
# ENEMY CHOOSES POKEMON: create instance of an enemy - takes new enemy, and prints out it's information
enemyPlayer = Enemy()
enemyPokemon = Enemy.randomPokemonSelected(enemyPlayer)
print(enemyPokemon.playerInfo())  # derives from Pokemon() object
print("\n")
# PLAYER CHOOSES POKEMON: create instance of an enemy - takes new enemy, and prints out it's information
humPlayer = Player()
playerPokemon = Player.selectPokemon(humPlayer)
print(playerPokemon.playerInfo())
print("\n")

playerAttack(playerPokemon)  # selected
playerAttack(playerPokemon)  # selected


print(enemyPokemon.playerInfo())
