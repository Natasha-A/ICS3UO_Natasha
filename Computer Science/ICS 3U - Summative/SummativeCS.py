# CLASS OBJECTS
import random
import time


class Pokemon():
    def __init__(self, name="None", health=50, kind="None", attackOne="None", attackTwo="None", attackThree="None"):
        self.allPokemon = []
        self.name = name
        self.health = health
        self.kind = kind
        self.attackOne = attackOne
        self.attackTwo = attackTwo
        self.attackThree = attackThree

    def playerInfo(self):
        return '-- Player Info --\nName: {}\nHealth: {}\nType: {}\nAttack 1: {}\nAttack 2: {}\nAttack 3: {}\n'.format(
            self.name,
            self.health, self.kind,
            self.attackOne, self.attackTwo,
            self.attackThree)


# can turn into function (SUPER CLASS STATIC METHOD?)
# which returns list of pokemons to implement into player and enemy classes
# LIST OF POKEMON - instances

def pokemonList():
    #**stores all instances of existing pokemon - can create seperate functions for enemy pokemon and player pokemon
    charmander = Pokemon("Charmander", 50, "Fire", "Flamethrower", "Fire Spin", "Cast Inferno")
    bulbasaur = Pokemon("Bulbasaur", 50, "Grass", "Vine Whip", "Leech Seed", "Cast Razor Leaf")
    squirtle = Pokemon("Squirtle", 50, "Water", "Rapid Spin", "Aqua Tail", "Cast Hydro Pump")

    pokemons = [charmander, bulbasaur, squirtle]

    return pokemons


class Player(Pokemon):
    def __init__(self, name="None", health=50, kind="None", attackOne="None", attackTwo="None", attackThree="None"):
        super().__init__(name, health, kind, attackOne, attackTwo, attackThree)

    @staticmethod
    def selectPokemon(self):
        checkPokemon = True
        pokemons = pokemonList()

        for pokemonIndex in range(len(pokemons)):
            print(str(pokemonIndex + 1) + ": " + pokemons[pokemonIndex].name)

        while checkPokemon:
            try:
                pokemonChosen = int(input("Choose a pokemon: "))
                if pokemonChosen > 0 and pokemonChosen <= (len(pokemons)):
                    return pokemons[pokemonChosen - 1]  # print out pokemon at index of chosen pokemon (1,2,3)
                else:
                    raise AssertionError

            except AssertionError:
                print("Incorrect input. Please enter the # for one of the pokemons above.")
                checkPokemon = True
            except ValueError:
                print("Incorrect value type. Please enter one of the numbers above.")


class Enemy(Pokemon):
    def __init__(self, name="", health=50, kind="", attackOne="", attackTwo="", attackThree=""):
        super().__init__(name, health, kind, attackOne, attackTwo, attackThree)

    # Enemy chooses pokemon at random
    def randomPokemonSelected(self):
        pokemons = pokemonList()
        pokemonChosen = random.choice(pokemons)

        nameOfPokemon = pokemonChosen.name

        print("Enemy is choosing its pokemon...")
        print("The random choice chosen is", nameOfPokemon)

        return pokemonChosen


# PROCESS behind attack effect on health and damage to other pokemon
def attackOutcome(attackChoice, pokemonSIDED, pokemonOPPOSING):  # eg when Player's Turn: pPokemon = pokemonSIDED
    # ePokemon = pokemonOPPOSING
    attackChosen = attackChoice
    opposingPokemon = pokemonOPPOSING  # for player - opposingPokemon = 'enemy'... for enemny - opposingPokemon = 'player'
    pokemonOnSide = pokemonSIDED
    newPlayerHealth = pokemonSIDED.health  # i nitalize health of player
    newEnemyHealth = pokemonOPPOSING.health  # initalize health of enemy

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
            opposingPokemon.health = 100  # reduce to capped health if outcome is greater

        if opposingPokemon.health < 0:  # if health has been reduced negative, it will be capped to value of 0
            opposingPokemon.health = 0

        print("Health has been decreased by:", attackDamage, "to:", opposingPokemon.health)

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

        if opposingPokemon.health > 100:
            opposingPokemon.health = 100  # reduce to capped health

        if opposingPokemon.health < 0:  # if health has been reduced negative, it will be capped to value of 0
            opposingPokemon.health = 0

        print("Health has been decreased by:", attackDamage, "to:", opposingPokemon.health)

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
                pokemonOnSide.health = 100  # Capped health of 100, doesn't go beyond

            if newPlayerHealth < 0:  # if health has been reduced negative, it will be capped to value of 0
                pokemonOnSide.health = 0

            print("The cast has healed the health by:", cast, "to:", pokemonOnSide.health)

    return newPlayerHealth, newEnemyHealth  # now in 'Battle' can use attacks to check (**NOT USED?)
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
            attackChosen = int(input("Choose an attack!\n"))
            if attackChosen > 0 and attackChosen <= (len(attackList)):
                print("Attack chosen:", attackList[attackChosen - 1])
                checkAttack = False
            else:
                raise AssertionError

        except AssertionError:
            print("Incorrect input. Please enter one  of the attacks above.")
            checkAttack = True
        except ValueError:
            print("Incorrect value type. Please enter one of the #'s above.")
            checkAttack = True

    # call attackOutcome to determine results of attack by pokemon chosen
    attackOutcome(attackChosen, playerPokemon, enemyPokemon)


def enemyAttack(eChosenPokemon):
    # only need to index attacks in order to choose option

    if eChosenPokemon.health <= 30:
        enemyAttackList = [1, 2, 3, 3, 3]  # Increase chances of enemy choosing cast when HP is at a low level:

    else:
        enemyAttackList = [1, 2, 3]

    enemyAttackChosen = random.choice(enemyAttackList)
    print("Attack chosen:", enemyAttackChosen)

    attackOutcome(enemyAttackChosen, enemyPokemon, playerPokemon)


def checkHealth(playerHealth, enemyHealth):
    # one of the players have reached a health of 0 ...
    while True:  # not needed? always breaking***
        if playerHealth <= 0 or enemyHealth <= 0:
            if playerHealth > enemyHealth:  # player has won
                winner = "player"  # turn into enums?*****
                enemyPlayer.health = 0
                break
                # multiple situations where breaking out of the while loop in necessary. Thus in order to avoid
                # overwriting the boolean state further in function, break used to dismiss loop on command.

            else:  # enemy has won
                winner = "enemy"
                humPlayer.health = 0

                break
        else:
            winner = "none"
            break

    return winner


def battle(PlayerPokemon, EnemyPokemon):
    runBattle = True
    playerTurn = PlayerPokemon
    enemyTurn = EnemyPokemon
    # continueBattle = True
    # create new instance of playerTurn and EnemyTurn for each round
    # round 1 - player goes first

    print("\nPython Pokemon Battle Begins!\n")

    while runBattle:
        print("PLAYER'S TURN \n")
        playerAttack(playerTurn)
        winner = checkHealth(playerTurn.health, enemyTurn.health)

        if winner == "player":
            print("YOU HAVE WON!")
            break
        elif winner == "enemy":
            print("THE COMPUTER HAS WON!")
            break

        time.sleep(2)  # delay for user to view results

        print("\nENEMY'S TURN")
        # round 1 - enemy goes second
        enemyAttack(enemyTurn)
        winner = checkHealth(playerTurn.health, enemyTurn.health)

        print("\n")
        # At the end of each of the player's and enemy's attack display total information
        print("PLAYER:\n" + str(playerTurn.playerInfo()), sep="\n")
        print("ENEMY:\n" + str(enemyTurn.playerInfo()), sep="\n")

        if winner == "player":
            print("YOU HAVE WON!")
            break
        elif winner == "enemy":
            print("THE COMPUTER HAS WON!")
            break
        #otherwise the game continues to be played...


def playGame():
    print("\nWelcome to Python Pokemon!\n")
    newRound = True
    continueCheckingForInput = True

    while newRound:

        # need to access objects as global variables in order to be modified by other functions such as during
        # battles and attacks
        global enemyPlayer
        enemyPlayer = Enemy()
        global enemyPokemon
        enemyPokemon = Enemy.randomPokemonSelected(enemyPlayer)
        # PLAYER CHOOSES POKEMON: create instance of an enemy - takes new enemy, and prints out it's information
        global humPlayer
        humPlayer = Player()
        global playerPokemon
        playerPokemon = Player.selectPokemon(humPlayer)  # done in playGame()

        # BATTLE ROUND
        battle(playerPokemon, enemyPokemon)  # repeats until health of a player is zero

        while continueCheckingForInput:  # convert to yes or no buttons.
            try:
                runProgram = input("Would you like to run the program again? ").lower()

                if runProgram == "yes":
                    newRound = True
                    continueCheckingForInput = False

                elif runProgram == "no":
                    print("Python Pokemon Battle Has Ended!")
                    newRound = False  # BREAKS FROM LOOP
                    continueCheckingForInput = False

                # ASSERTION - "else" statement - creates an exception to check for correct value
                assert runProgram == "yes" or runProgram == "no"  # test input value

            except AssertionError:
                print("Incorrect input. Please enter 'yes' or 'no'.")
                continueCheckingForInput = True

#MAIN PROGRAM
playGame()
