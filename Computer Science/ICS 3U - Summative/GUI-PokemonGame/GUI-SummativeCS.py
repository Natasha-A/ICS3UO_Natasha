'''
Name: Natasha Ahammed
Date: January 9 2020
File Name: Natasha_Ahammed_SummativeCS.py
Description: Pokemon Game Based off of Turn-Based Battles. Player battles with Computer AI in a series of rounds \
where a pokemon is chosen and different attacks can be chosen yielding in different amounts of damage or healing \
health. Whoever is able to cause one the opponent's pokemon to faint first, wins the the battle.
Test Cases: Made use of exploratory testing to examine UI display and game play loop. Played using various \
combinations, testing all functions individually and collectively. Use of Try and Except to handle error handling
for user inputs, and Integration Testing to ensure that algorithms produced correct results and no logic errors. Made
use of PyCharm's Automated Testing in order to detect and replace unreachable code.

REVEALS ASPECTS
- First Attack: Yields in damage by 10 - 25 HP
- Second Attack: Yields in damage by 18 - 35 HP
- Third Attack: Yields in healing (to own pokemon) by 10 - 25 HP
'''

# Add enemy pokemon seperate list, using time.sleep in order make user display easier to read. Add counts for wins and loses for rounds.
# Add comments isolating areas of kinds of functions

import random
import time
import tkinter as tk
from tkinter import font

#Creating GUI
HEIGHT = 700
WIDTH = 800
#root window
root = tk.Tk()

# widgets - display canvas and frame sizing
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#CREATING BACKGROUND IMAGE
backgroundImage = tk.PhotoImage(file="battleGround.png")
backgroundLabel = tk.Label(root, image=backgroundImage)
backgroundLabel.place(relwidth=1, relheight=1)


# *********** CLASS OBJECTS ***********
class Pokemon():

    attackList = []

    def __init__(self, name="None1", health=100, healthBars="==========", kind="None", attackOne="None",
                 attackTwo="None",
                 attackThree="None"):
        self.allPokemon = []
        self.name = name
        self.health = health
        self.healthBars = healthBars
        self.kind = kind
        self.attackOne = attackOne
        self.attackTwo = attackTwo
        self.attackThree = attackThree

    # displays main stats during battle
    def playerInfo(self):
        return '-- Player Info --\nName: {}\nHealth: {}\nHP: \n'.format(
            self.name,
            self.health,
            self.healthBars)

    # Creates list of instances of attacks used by Enemy Chosen Pokemon
    @staticmethod
    def attackList(self,numberChosen):
        enemyAttackList = [self.attackOne, self.attackTwo,
                           self.attackThree]

        return enemyAttackList[numberChosen]

class Player(Pokemon):
    def __init__(self, name="None2", health=100, healthBars="==========", kind="None", attackOne="None",
                 attackTwo="None",
                 attackThree="None"):
        super().__init__(name, health, healthBars, kind, attackOne, attackTwo, attackThree)

    # create property for number of wins?

    @staticmethod
    def selectPokemon(self):
        checkPokemon = True
        pokemons = playerPokemonList()

        for pokemonIndex in range(len(pokemons)):
            print(str(pokemonIndex + 1) + ": " + pokemons[pokemonIndex].name)

        while checkPokemon:
            try:
                pokemonChosen = int(input("Choose a pokemon (#):"))
                if pokemonChosen > 0 and pokemonChosen <= (len(pokemons)):
                    print("\nGo!", str(pokemons[pokemonChosen - 1].name) + "!")
                    time.sleep(0.5)
                    return pokemons[pokemonChosen - 1]  # print out pokemon at index of chosen pokemon (1,2,3)
                else:
                    raise AssertionError

            except AssertionError:
                print("Incorrect input. Please enter the # for one of the pokemons above.")
                checkPokemon = True
            except ValueError:
                print("Incorrect value type. Please enter one of the numbers above.")


class Enemy(Pokemon):

    def __init__(self, name="None3", health=100, healthBars="=====", kind="None", attackOne="None", attackTwo="None",
                 attackThree="None"):
        super().__init__(name, health, healthBars, kind, attackOne, attackTwo, attackThree)

    # Enemy chooses pokemon at random
    @staticmethod
    def randomPokemonSelected(self):
        pokemons = enemyPokemonList()
        pokemonChosen = random.choice(pokemons)

        nameOfPokemon = pokemonChosen.name

        print("Pokemon Trainer RED sent out", str(nameOfPokemon) + "!\n")
        time.sleep(0.7)

        return pokemonChosen



# *********** INSTANCE Functions - Pokemon Lists ***********
def playerPokemonList():
    # *stores all instances of existing pokemon - can create seperate functions for enemy pokemon and player pokemon
    charmander = Pokemon("CHARMANDER", 100, "==========", "FIRE", "FLAMETHROWER", "FIRE SPIN", "CAST")
    bulbasaur = Pokemon("BULBASAUR", 100, "==========", "GRASS", "VINE WHIP", "LEECH SEED", "CAST")
    squirtle = Pokemon("SQUIRTLE", 100, "==========", "WATER", "RAPID SPIN", "AQUA TAIL", "CAST")
    pokemons = [charmander, bulbasaur, squirtle]

    return pokemons


def enemyPokemonList():
    # *stores all instances of existing pokemon - can create seperate functions for enemy pokemon and player pokemon
    pidgey = Pokemon("PIDGEY", 100, "==========", "NORMAL", "GUST", "WHIRLWIND", "CAST")
    pikachu = Pokemon("PIKACHU", 100, "==========", "ELECTRIC", "THUNDER SHOCK", "THUNDERBOLT", "CAST")
    mankey = Pokemon("MANKEY", 100, "==========", "FIGHTING", "KARATE CHOP", "CROSS CHOP", "CAST")
    pokemons = [pidgey, pikachu, mankey]

    return pokemons


# *********** GAME FUNCTIONS - Behaviours and displays of Main Game and Battles ***********

# visual bar display of level of health in reference to player's HP health
def barHealth(health):
    roundedHealth = health // 10  # splits health into bars
    if health >= 10:
        barAmount = "=" * roundedHealth
    elif health < 10 and health > 0:
        barAmount = "="
    else:  # health has reached zero
        barAmount = ""

    print("HP:", barAmount)
    time.sleep(0.7)

    return barAmount


# ATTACK OUTCOME - Process behind attack effect on health and damage to other pokemon
# (Parameter Input Depends on Turn of Player)
def attackOutcome(attackChoice, pokemonSidedObject, pokemonOpposedObject):  # eg when CPU's Turn: "enemyObject" = pokemonSIDED, \
    # when User Player's Turn: "playerObject" = pokemonSIDED
    attackChosen = attackChoice
    opposingPokemon = pokemonOpposedObject  # for player - opposingPokemon = 'enemy'. For enemy - opposingPokemon = 'player'
    newEnemyHealth = pokemonOpposedObject.health  # initalize health of enemy

    pokemonOnSide = pokemonSidedObject
    newPlayerHealth = pokemonSidedObject.health  # initalize health of player

    # Moderate Damage:
    if attackChosen == 1:
        attackDamage = random.randint(18, 25)
        newEnemyHealth = opposingPokemon.health - attackDamage  # reduces enemy's health by amount
        opposingPokemon.health = newEnemyHealth
        opposingPokemon.healthBars = barHealth(newEnemyHealth)

        if attackDamage >= 20:
            print("The attack is very effective!\n")
        # attack is 19 or below
        else:
            print("The attack is not very effective...\n")
            time.sleep(1)

        if newEnemyHealth > 100:
            opposingPokemon.health = 100  # reduce to capped health if outcome is greater

        if opposingPokemon.health < 0:  # if health has been reduced negative, it will be capped to value of 0
            opposingPokemon.health = 0
            print(opposingPokemon.name, "has fainted!\n") # HP has reached 0

        # $$$$$$$$$
        print(opposingPokemon.name, "health has been decreased by:", attackDamage, "HP to:", opposingPokemon.health, "HP.")
        time.sleep(1)

    # High Range Damage:
    elif attackChosen == 2:
        attackDamage = random.randint(10, 35)
        newEnemyHealth = opposingPokemon.health - attackDamage  # reduces enemy's health by amount
        opposingPokemon.health = newEnemyHealth
        opposingPokemon.healthBars = barHealth(newEnemyHealth)

        if attackDamage >= 30:
            print("The attack is extremely effective!\n")
        elif attackDamage >= 20:
            print("The attack is super effective!\n")
        else:
            print("The attack is not very effective...\n")
        time.sleep(1)

        if opposingPokemon.health > 100:
            opposingPokemon.health = 100  # reduce to capped health

        if opposingPokemon.health < 0:  # if health has been reduced negative, it will be capped to value of 0
            opposingPokemon.health = 0
            print(opposingPokemon.name, "has fainted!\n")

        print(opposingPokemon.name, "health has been decreased by:", attackDamage, "HP to:", opposingPokemon.health, "HP.")
        time.sleep(1)


    # CAST - increase own player's HP by moderate amount:
    elif attackChosen == 3:
        if pokemonOnSide.health >= 100:
            print("Cast is not effective. Pokemon is already at the max health.\n")
        else:
            cast = random.randint(18, 25)
            newPlayerHealth = pokemonOnSide.health + cast
            pokemonOnSide.health = newPlayerHealth
            pokemonOnSide.healthBars = barHealth(newEnemyHealth)

            if cast >= 20:
                print("The cast was very effective!\n")
            else:
                print("The cast was not very effective...\n")
            time.sleep(1)


            if newPlayerHealth > 100:
                pokemonOnSide.health = 100  # Capped health of 100, doesn't go beyond

            if newPlayerHealth < 0:  # if health has been reduced negative, it will be capped to value of 0
                pokemonOnSide.health = 0
                print(opposingPokemon.name, "has fainted!\n")

            print(pokemonOnSide.name, "has been healed by:", cast, "HP to:", pokemonOnSide.health, "HP.\n")
            time.sleep(1)

    return newPlayerHealth, newEnemyHealth


# User Player's Turn in Battle Round
def playerAttack(playerObject, enemyObject):

    playerTurn = playerObject
    enemyTurn = enemyObject
    checkAttack = True
    # playerPokemon - assigns parameter as chosen pokemon object
    # able to called repeatedly for player to attack during battle on turn
    attack1 = playerObject.attackOne
    attack2 = playerObject.attackTwo
    attack3 = playerObject.attackThree
    attackList = [attack1, attack2, attack3]  # list of attacks corresponding to chosen pokemon

    # Display attacks for chosen Pokemon for current battle
    time.sleep(0.6)
    print("\n")
    for attackIndex in range(len(attackList)):
        print(str(attackIndex + 1) + ":", attackList[attackIndex])
    print("\n")
    time.sleep(0.6)

    # check for correct INPUT for attack:
    while checkAttack:
        try:
            attackChosen = int(input("Choose an attack (#): "))
            print("\n")
            time.sleep(0.6)

            if attackChosen > 0 and attackChosen <= (len(attackList)):
                print(playerObject.name, "used", str(attackList[attackChosen - 1]) + "!")
                time.sleep(0.6)
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
    attackOutcome(attackChosen, playerTurn, enemyTurn)


# CPU Player's Turn in Battle Round
def enemyAttack(enemyObject, playerObject):
    # only need to index attacks in order to choose option
    enemyPokemon = enemyObject
    playerPokemon = playerObject

    if enemyPokemon.health <= 30:
        enemyAttackList = [1, 2, 3, 3, 3]  # Increase chances of enemy choosing cast when HP is at a low level:
    else:
        enemyAttackList = [1, 2, 3]

    enemyAttackChosen = random.choice(enemyAttackList)

    # Address change in turn in battle, index attack randomly selected
    print("\nEnemy", enemyPokemon.name, "used", str(enemyPokemon.attackList(enemyPokemon, (enemyAttackChosen-1))) + "!")

    attackOutcome(enemyAttackChosen, enemyPokemon, playerPokemon)


# Throughout battle, check healths of both players. Once of the player's health reaches zero, assert the winner of the\
# round
def checkHealth(playerHealth, enemyHealth, playerObject, enemyObject):
    enemyPlayer = playerObject
    humPlayer = enemyObject
    while True:
        if playerHealth <= 0 or enemyHealth <= 0:  # one of the players have reached a health of 0 ...

            if playerHealth > enemyHealth:  # User Player has won
                winner = "player"
                enemyPlayer.health = 0
                break
                # multiple situations where breaking out of the while loop in necessary. Thus in order to avoid
                # overwriting the boolean state further in function, break used to dismiss loop on command instead.

            else:  # Enemy CPU has won
                winner = "enemy"
                humPlayer.health = 0
                break
        else:
            winner = "none"
            break

    return winner


# Individual Complete Battle Round
def battle(playerObject, enemyObject):
    runBattle = True
    playerTurn = playerObject  # Assign objects
    enemyTurn = enemyObject

    while runBattle:
        # single round begins -Player attacks first
        playerAttack(playerTurn, enemyObject)

        winner = checkHealth(playerTurn.health, enemyTurn.health, Player(), Enemy())  # check for state of health
        # throughout battle

        if winner == "player":  # fake 'enum' type usage in order assert winner of round
            print("\nYou have won the battle!\n")
            break
        elif winner == "enemy":
            print("\nPokemon Trainer RED won the battle!\n")
            break

        time.sleep(2)  # delay for user to view results

        # single round continues - enemy goes second
        enemyAttack(enemyTurn, playerTurn)
        winner = checkHealth(playerTurn.health, enemyTurn.health, Player(), Enemy())

        print("\n")

        # ATTACK ROUND STATS - At the end of each of the player's and enemy's attack display total information
        dash = '-' * 30
        print(dash)
        print('{:>4s}{:>18}'.format("PLAYER", "ENEMY"))
        print(dash)
        print('{:>2s}{:>12s}'.format(playerTurn.name, enemyTurn.name))
        print('{:>2s}{:>16s}'.format(str(playerTurn.health), str(enemyTurn.health)))
        print('HP: {:>2s}    HP: {:>4s}'.format(str(playerTurn.healthBars), str(enemyTurn.healthBars)))




# Encompasses all aspects of the game - choosing pokemons, battle rounds, wins/loses, restarting game
def playGame(playerObject, enemyObject):
    root.mainloop()

    newRound = True
    continueCheckingForInput = True

    # INITIAL TITLE
    print("\nWelcome to Python Pokemon!\n")
    time.sleep(1.5)
    print("Pokemon Trainer RED wants to battle!\n")
    time.sleep(1)

    while newRound:
        # CREATE PLAYER OBJECTS - USER and CPU
        humPlayer = playerObject  # Human (User) Object Created
        playerPokemon = Player.selectPokemon(humPlayer) # User chooses pokemon

        enemyPlayer = enemyObject  # Enemy Player Object Created
        enemyPokemon = Enemy.randomPokemonSelected(enemyPlayer) # Enemy randomly chooses pokemon
        # BATTLE ROUND PLAYED
        battle(playerPokemon, enemyPokemon)  # repeats until health of a player is zero -- then moves onto next line:
        while continueCheckingForInput:
            try:
                runProgram = input("Battle again? ").lower()
                print("\n")

                if runProgram == "yes":
                    newRound = True
                    continueCheckingForInput = False

                elif runProgram == "no":
                    print("Python Pokemon battle ended!")
                    newRound = False  # BREAKS FROM LOOP
                    continueCheckingForInput = False

                # ASSERTION - "else" statement - creates an exception to check for correct value
                assert runProgram == "yes" or runProgram == "no"  # test input value

            except AssertionError:
                print("Incorrect input. Please enter 'yes' or 'no'.")
                continueCheckingForInput = True


# MAIN PROGRAM
playGame(Player(), Enemy())
