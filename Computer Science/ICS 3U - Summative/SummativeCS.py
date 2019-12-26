# CLASS OBJECTS
import random, time

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
        return '* Player Info *\nName: {}\nHealth: {}\nType: {}\nAttack 1: {}\nAttack 2: {}\nAttack 3: {}\n'.format(
            self.name,
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

# PROCESS behind attack effect on health and damage to other pokemon - (turn into sep. func)
def attackOutcome(attackChoice, pokemonSIDED, pokemonOPPOSING):
    attackChosen = attackChoice
    opposingPokemon = pokemonOPPOSING # for player - opposingPokemon = 'enemy'... for enemny - opposingPokemon = 'player'
    pokemonOnSide = pokemonSIDED
    newPlayerHealth = pokemonSIDED.health # i nitalize health of player
    newEnemyHealth = pokemonOPPOSING.health # initalize health of enemy

    # Moderate Damage:
    if attackChosen == 1:
        attackDamage = random.randint(18, 25)
        newEnemyHealth = opposingPokemon.health - attackDamage  # reduces enemy's health by amount
        opposingPokemon.health = newEnemyHealth
        if attackDamage >= 20:
            print("The attack is very effective!")
        # attack is 19 or below
        else:
            print("The attack is not very effective...")

        if newEnemyHealth > 100:
            newEnemyHealth = 100 # reduce to capped health if outcome is greater

        print("Health has been decreased by:", attackDamage, "to:", newEnemyHealth)

    # High Range Damage:
    elif attackChosen == 2:
        attackDamage = random.randint(10, 35)
        newEnemyHealth = opposingPokemon.health - attackDamage  # reduces enemy's health by amount
        opposingPokemon.health = newEnemyHealth

        if attackDamage >= 30:
            print("The attack is extremely effective!")
        elif attackDamage >= 20:
            print("The attack is very effective!")
        else:
            print("The attack is not very effective...")

        if newEnemyHealth > 100:
            newEnemyHealth = 100 # reduce to capped health

        print("Health has been decreased by:", attackDamage, "to:", newEnemyHealth)

    # CAST - increase player's hp by moderate amount
    elif attackChosen == 3:
        if pokemonOnSide.health >= 100:
            print("Cast is not effective. You are already at the max health.")
        else:
            cast = random.randint(18, 25)
            newPlayerHealth = pokemonOnSide.health + cast
            pokemonOnSide.health = newPlayerHealth

            if cast >= 20:
                print("The cast was very effective!")
            else:
                print("The cast was not very effective...")

            if newPlayerHealth > 100:
                pokemonOnSide.health = 100 #Capped health of 100, doesn't go beyond

            print("The cast has healed the health by:", cast, "to:", newPlayerHealth)

    return newPlayerHealth, newEnemyHealth # now in 'Battle' can use attacks to check (**NOT USED?)
    # if either health has reached zero yet in order to choose winner

def playerAttack(pChosenPokemon):
    checkAttack = True
    # playerPokemon - assigns parameter as chosen pokemon object
    # able to called repeatedly for player to attack during battle on turn
    attack1 = pChosenPokemon.attackOne
    attack2 = pChosenPokemon.attackTwo
    attack3 = pChosenPokemon.attackThree
    attackList = [attack1, attack2, attack3]

    # Display attacks for chosen Pokemon for current battle
    for attackIndex in range(len(attackList)):
        print(str(attackIndex + 1) + ":", attackList[attackIndex])

    # check for correct INPUT for attack:
    while checkAttack:
        try:
            attackChosen = int(input("Choose an attack: "))
            if attackChosen > 0 and attackChosen <= (len(attackList)):
                print("Attack chosen:", attackList[attackChosen - 1])
                checkAttack = False
                # return attackList[attackChosen - 1]  # print out pokemon at index of chosen pokemon (1,2,3)
            else:
                raise AssertionError

        except AssertionError:
            print("Incorrect input. Please enter one  of the attacks above.")
            checkAttack = True
        except ValueError:
            print("Incorrect value type. Please enter one of the #'s above.")

    #call attackOutcome to determine results of attack by pokemon chosen
    attackOutcome(attackChosen, playerPokemon, enemyPokemon)


def enemyAttack(eChosenPokemon):
    # only need to index attacks in order to choose option

    if eChosenPokemon.health <= 30:
        enemyAttackList = [1,2,3,3,3] #Increase chances of enemy choosing cast when HP is at a low level:

    else:
        enemyAttackList = [1, 2, 3]

    enemyAttackChosen = random.choice(enemyAttackList)
    print("Attack chosen:", enemyAttackChosen)

    attackOutcome(enemyAttackChosen, enemyPokemon, playerPokemon)

def checkHealth(playerHealth, enemyHealth):
    # one of the players have reached a health of 0 (TURN INTO FUNCTION****)
    if playerHealth <= 0 or enemyHealth <= 0:
        if playerHealth > enemyHealth:  # player has won
            return winner = "Player"
            break

        else:  # enemy has won
            print("The winner of the battle is:", enemyTurn.name, "!")
            return winner = "Enemy"
            break
    else:
        print("**Battle Continues**")




def battle(PlayerPokemon, EnemyPokemon):
    runBattle = True
    playerTurn = PlayerPokemon
    enemyTurn = EnemyPokemon

    while runBattle:
        #create new instance of playerTurn and EnemyTurn for each round

        #round 1 - player goes first
        print("PLAYER'S TURN \n")
        playerAttack(playerTurn)

        # one of the players have reached a health of 0 (TURN INTO FUNCTION****)
        if playerTurn.health <= 0 or enemyTurn.health <= 0:
            if playerTurn.health > enemyTurn.health:  # player has won
                print("The winner of the battle is:", playerTurn.name, "!")
                break

            else:  # enemy has won
                print("The winner of the battle is:", enemyTurn.name, "!")
                break
        else:
            print("**Battle Continues**")

        time.sleep(2) #delay for user to view results

        print("ENEMY'S TURN")
        #round 1 - enemy goes second
        enemyAttack(enemyTurn)

        # one of the players have reached a health of 0
        if playerTurn.health <= 0 or enemyTurn.health <= 0:
            if playerTurn.health > enemyTurn.health:  # player has won
                print("The winner of the battle is:", playerTurn.name, "!")
                break

            else:  # enemy has won
                print("The winner of the battle is:", enemyTurn.name, "!")
                break
        else:
            runBattle = True
            print("**Battle Continues**")

            #At the end of each of the player's and enemy's attack display total information
            print(playerPokemon.playerInfo())
            print(enemyPokemon.playerInfo())

'''
RUN BATTLE (Player, Enemy):
#Continuous Loop that alternates between user player and AI player
REPETITION:
While TRUE:
ASSIGN pHlth and oHlth to  Player'sTurn():
	If pHlth less than 0 or eHlth less than 0:
•	RUN FALSE (battle ends)

ASSIGN pHlth and oHlth = EnemysTurn():
	If pHlth less than 0 or eHth less than 0:
•	RUN FALSE (battle ends)

Else:
Run TRUE
'''


# MAIN PROGRAM
# ENEMY CHOOSES POKEMON: create instance of an enemy - takes new enemy, and prints out it's information
enemyPlayer = Enemy() #****GETS CHOSEN IN PLAY GAME FUNCTION ******
enemyPokemon = Enemy.randomPokemonSelected(enemyPlayer)
'''
print(enemyPokemon.playerInfo())  # derives from Pokemon() object
print("\n")
'''

# PLAYER CHOOSES POKEMON: create instance of an enemy - takes new enemy, and prints out it's information
humPlayer = Player()
playerPokemon = Player.selectPokemon(humPlayer) #done in playGame()

'''
print(playerPokemon.playerInfo())
print("\n")
'''

battle(playerPokemon, enemyPokemon) #repeats until health of a player is zero

'''
#BATTLE BEGINS
print("PLAYER'S TURN \n")
playerAttack(playerPokemon)  # selected
time.sleep(2)
print("ENEMY'S TURN")
enemyAttack(enemyPokemon)
'''

'''
#FIRST ROUND INFO:
print(enemyPokemon.playerInfo())
print(playerPokemon.playerInfo())
'''
