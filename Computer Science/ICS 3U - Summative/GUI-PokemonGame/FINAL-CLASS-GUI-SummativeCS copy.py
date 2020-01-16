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

REVEALED ASPECTS

Attack Damage Outcomes
- First Attack: Yields in damage by 10 - 25 HP
- Second Attack: Yields in damage by 18 - 35 HP
- Third Attack: Yields in healing (to own pokemon) by 10 - 25 HP

Type Advantages: Stronger Pokemon - increase attack damage by half... Weaker Pokemon - decreases attack by half
- FIRE pokemon is STRONGER against GRASS pokemon
- FIRE pokemon is WEAKER against WATER pokemon

- WATER pokemon is STRONGER against FIRE pokemon
- WATER pokemon is WEAKER against GRASS pokemon

- GRASS pokemon is STRONGER against WATER pokemon
- GRASS pokemon is WEAKER against FIRE pokemon
'''
import random, time
import tkinter as tk
from tkinter import font, ttk

# CONSTANTS (HENCE ALL CAPS)
LARGE_FONT = ("Verdana", 30)

# have to set up globals -- which are called throughout classes 

# *********** CLASS OBJECTS ***********

class Pokemon():
    attackList = []

    def __init__(self, name="None", health=100, healthBars="==========", kind="None", attackOne="None",
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
    def attackList(self, numberChosen):
        enemyAttackList = [self.attackOne, self.attackTwo,
                           self.attackThree]

        return enemyAttackList[numberChosen]


class Player(Pokemon):
    def __init__(self, name="None", health=100, healthBars="==========", kind="None", attackOne="None",
                 attackTwo="None",
                 attackThree="None"):
        super().__init__(name, health, healthBars, kind, attackOne, attackTwo, attackThree)

    # create property for number of wins?

    @staticmethod
    def selectPokemon(self, pokemonSelected):
        print("pokemonSelected Value:", pokemonSelected)
        checkPokemon = True
        pokemons = playerPokemonList()
        dash = "-" * 30
        print(dash)
        print('{:>20}'.format("POKEMON INDEX"))
        print(dash)

        for pokemonIndex in range(len(pokemons)):
            print(str(pokemonIndex + 1) + ": " + pokemons[pokemonIndex].name, "- TYPE:", pokemons[pokemonIndex].kind)

        while checkPokemon:
            try:
                if int(pokemonSelected) > 0 and int(pokemonSelected) <= (len(pokemons)):
                    print("Selected Pokemon:", pokemons[int(pokemonSelected)-1].name)
                    return pokemons[int(pokemonSelected)-1]  # print out pokemon at index of chosen pokemon (1,2,3)
                     # returns instance of pokemon -- eg, charmander, bulbasaur, squirtle

                else:
                    raise AssertionError

            except AssertionError:
                print("Incorrect input. Please enter the # for one of the pokemons above.")
                checkPokemon = True
            except ValueError:
                print("Incorrect value type. Please enter one of the numbers above.")


class Enemy(Pokemon):

    def __init__(self, name="None", health=100, healthBars="=====", kind="None", attackOne="None", attackTwo="None",
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



# *********** GUI CLASS OBJECTS ***********
class PokemonGUIApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        # CONFIG PROPERTIES - for container/frames
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # runs through pages - saving the frames added, and bringing to the front
        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            #allows to remove add as go along
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # takes frame from parent
        self.parent = parent

        backgroundImage = tk.PhotoImage(file="battleGround.png")  # update values
        backgroundLabel = tk.Label(self, image=backgroundImage)
        backgroundLabel.photo = backgroundImage
        backgroundLabel.place(relwidth=1, relheight=1)


        label = tk.Label(self, text="Welcome to Python Pokemon!", font=LARGE_FONT)

        # Potential UI configs
        #label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)
        #label.pack(side="bottom", fill="x")
        #label.place(relx=0.3, rely=0.4, relwidth=0.45, relheight=0.25)
        label.pack(side="bottom", fill="x")

        # goes to page one
        button = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame(PageOne))  # goes to page one
        button.pack(side="right")


# Page One
class PageOne(tk.Frame):

    # always creating under init, since always working into each 'sel' call of object
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pokemon Trainer RED wants to battle!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # goes to page two
        button2 = tk.Button(self, text="Next",
                            command=lambda: controller.show_frame(PageTwo))  # goes back to start page
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # ENEMY OBJECT INSTANTIATED
        # needs to be global in order to be accessed throughout GUI and non-gui classes and functions
        global enemyPokemonChosen
        enemyPokemonChosen = Enemy.randomPokemonSelected(ENEMY)  # Enemy randomly chooses pokemon

        textEnemy = "Pokemon Trainer RED sent out " + str(enemyPokemonChosen.name) + "!"

        label2 = tk.Label(self, text=textEnemy, font=LARGE_FONT)
        label2.pack()

        # always creating under init, since always working into each 'sel' call of object
        def getChosenPokemon(entry):
            # PLAYER OBJECT INSTANTIATED
            global playerPokemonChosen
            playerPokemonChosen = Player.selectPokemon(PLAYER, entry)  # Human chooses pokemon from list
            chosenPk = "You chose:" + str(playerPokemonChosen.name)

            chosenPokemon = tk.Label(self, text=chosenPk, font=LARGE_FONT)
            chosenPokemon.pack()


        label = tk.Label(self, text="Which Pokemon will you choose?", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="Next",
                            command=lambda: controller.show_frame(PageThree))  # goes back to start page
        button2.pack()


        pokemon1 = tk.Label(self, text="Charmander", font=LARGE_FONT)
        pokemon2 = tk.Label(self, text="Bulbasaur", font=LARGE_FONT)
        pokemon3 = tk.Label(self, text="Squirtle", font=LARGE_FONT)

        entry = tk.Entry(self, font=("Courier", 18), bg="green")
        entry.pack()
        entryButton = tk.Button(self, text="Get Chosen Pokemon", font=("Courier", 16),bg="green",
                           command=lambda: getChosenPokemon(entry.get()))  # DISPLAYS ENTRY text

        entryButton.pack(pady=10, padx=10)

        pokemon1.pack(pady=10, padx=10)
        pokemon2.pack(pady=10, padx=10)
        pokemon3.pack(pady=10, padx=10)


# Battle begin - create images of selected pokemon, and continue game in text format... CONTINUE THE GAME - EXIT BUTTON
class PageThree(PageTwo,tk.Frame):
    # always creating under init, since always working into each 'sel' call of object
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def closeWindow():
            controller.destroy()

        label = tk.Label(self, text="Battle Begins!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # button to say exit out of main loop!
        #button = tk.Label(self, text="Quit", command=lambda: closeWindow())
        button = tk.Button(self, text="Quit", command=controller.quit)

        button.pack(pady=20, padx=20)


# when adding new information - create lamda functions which will call game functions in order to run forward


# *********** INSTANCE Functions - Pokemon Lists ***********
def playerPokemonList():
    # *stores all instances of existing pokemon - can create seperate functions for enemy pokemon and player pokemon
    charmander = Pokemon("CHARMANDER", 100, "==========", "FIRE", "FLAMETHROWER", "FIRE SPIN", "CAST")
    bulbasaur = Pokemon("BULBASAUR", 100, "==========", "GRASS", "VINE WHIP", "LEECH SEED", "CAST")
    squirtle = Pokemon("SQUIRTLE", 100, "==========", "WATER", "WATER SPLASH", "AQUA TAIL", "CAST")
    pokemons = [charmander, bulbasaur, squirtle]

    return pokemons


def enemyPokemonList():
    # *stores all instances of existing pokemon - can create seperate functions for enemy pokemon and player pokemon
    flareon = Pokemon("FLAREON", 100, "==========", "FIRE", "FIRE SLASH", "BLAZE BALL", "CAST")
    breloom = Pokemon("BRELOOM", 100, "==========", "GRASS", "RAZOR LEAF", "SPIT POISON", "CAST")
    magikarp = Pokemon("MAGIKARP", 100, "==========", "WATER", "KARATE CHOP", "SUBMERGE", "CAST")
    pokemons = [flareon, breloom, magikarp]

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


# Consider type/kind advantages - Based on the kind of pokemon, the inflicted damage varies against opponents
# pokemon kind
def typeAdvantage(sidedObjectKind, opposingObjectKind, damageAmount):
    playerKind = sidedObjectKind
    enemyKind = opposingObjectKind

    # player is a FIRE type
    if playerKind == "FIRE":
        if enemyKind == "WATER":  # FIRE is weak against WATER
            damageAmount /= 2  # reduce damage by half
        elif enemyKind == "GRASS":  # FIRE is strong against GRASS
            damageAmount *= 1.5  # increase damage by half
        else:  # otherwise, enemyKind is same kind (i.e. FIRE)
            damageAmount = damageAmount  # damage remains the same

    # player is a WATER type
    elif playerKind == "WATER":
        if enemyKind == "GRASS":  # WATER is weak against GRASS
            damageAmount /= 2
        elif enemyKind == "FIRE":  # WATER is strong against FIRE
            damageAmount *= 1.5
        else:
            damageAmount = damageAmount


    # player is a GRASS type
    elif playerKind == "GRASS":
        if enemyKind == "FIRE":  # GRASS is weak against FIRE
            damageAmount /= 2
        elif enemyKind == "WATER":  # GRASS is strong against WATER
            damageAmount *= 1.5
        else:
            damageAmount = damageAmount

    return damageAmount


# ATTACK OUTCOME - Process behind attack effect on health and damage to other pokemon
# (Parameter Input Depends on Turn of Player)
def attackOutcome(attackChoice, pokemonSidedObject, pokemonOpposedObject):  # eg when CPU's Turn: "enemyObject" = \
    # pokemonSidedObject, when User Player's Turn: "playerObject" = pokemonSidedObject
    attackChosen = attackChoice
    opposingPokemon = pokemonOpposedObject  # for player - opposingPokemon = 'enemy'. For enemy - opposingPokemon = \
    # 'player'
    newEnemyHealth = pokemonOpposedObject.health  # initalize health of enemy

    pokemonOnSide = pokemonSidedObject
    newPlayerHealth = pokemonSidedObject.health  # initalize health of player

    # Moderate Damage:
    if attackChosen == 1:
        attackDamage = random.randint(18, 25)
        attackDamage = typeAdvantage(pokemonOnSide, opposingPokemon, attackDamage)  # change damage amount!!!

        newEnemyHealth = opposingPokemon.health - attackDamage  # reduces enemy's health by amount
        opposingPokemon.health = newEnemyHealth
        opposingPokemon.healthBars = barHealth(newEnemyHealth)

        if attackDamage >= 20:
            print("It's super effective!\n")
        # attack is 19 or below
        else:
            print("It's not very effective...\n")
            time.sleep(1)

        if newEnemyHealth > 100:
            opposingPokemon.health = 100  # reduce to capped health if outcome is greater

        elif opposingPokemon.health < 0:  # if health has been reduced negative, it will be capped to value of 0
            opposingPokemon.health = 0
            print(opposingPokemon.name, "has fainted!\n")  # HP has reached 0

        print(opposingPokemon.name, "health has been decreased by", attackDamage, "HP and is now at", \
              opposingPokemon.health, "HP.")
        time.sleep(1)

    # High Range Damage:
    elif attackChosen == 2:
        attackDamage = random.randint(10, 35)
        attackDamage = typeAdvantage(pokemonOnSide, opposingPokemon, attackDamage)  # change damage amount!!!

        newEnemyHealth = opposingPokemon.health - attackDamage  # reduces enemy's health by amount
        opposingPokemon.health = newEnemyHealth
        opposingPokemon.healthBars = barHealth(newEnemyHealth)

        if attackDamage >= 30:
            print("It's extremely effective!\n")
        elif attackDamage >= 20:
            print("It's super effective!\n")
        else:
            print("It's not very effective...\n")
        time.sleep(1)

        if opposingPokemon.health > 100:
            opposingPokemon.health = 100  # reduce to capped health

        elif opposingPokemon.health < 0:  # if health has been reduced negative, it will be capped to value of 0
            opposingPokemon.health = 0
            print(opposingPokemon.name, "has fainted!\n")

        print(opposingPokemon.name, "health has been decreased by", attackDamage, "HP and is now at", \
              opposingPokemon.health, "HP.")
        time.sleep(1)


    # CAST - increase own player's HP by moderate amount:
    elif attackChosen == 3:
        if pokemonOnSide.health >= 100:
            print("Cast is not effective. Pokemon is already at the max health.\n")
        else:
            cast = random.randint(18, 25)
            newPlayerHealth = pokemonOnSide.health + cast  # increases owns health by amount
            pokemonOnSide.health = newPlayerHealth
            pokemonOnSide.healthBars = barHealth(newEnemyHealth)

            if cast >= 20:
                print("The cast was very effective!\n")
            else:
                print("The cast was not very effective...\n")
            time.sleep(1)

            if newPlayerHealth > 100:
                pokemonOnSide.health = 100  # Capped health of 100, doesn't go beyond

            elif newPlayerHealth < 0:  # if health has been reduced negative, it will be capped to value of 0
                pokemonOnSide.health = 0
                print(opposingPokemon.name, "has fainted!\n")

            print(pokemonOnSide.name, "has been healed by", cast, "HP and is now at", \
                  pokemonOnSide.health, "HP.")
            time.sleep(1)

    return newPlayerHealth, newEnemyHealth


# User Player's Turn in Battle Round
def playerAttack(playerObject, enemyObject):
    playerTurn = playerObject
    enemyTurn = enemyObject
    checkAttack = True
    dash = "-" * 30

    # playerPokemon - assigns parameter as chosen pokemon object
    # able to called repeatedly for player to attack during battle on turn
    attack1 = playerObject.attackOne
    attack2 = playerObject.attackTwo
    attack3 = playerObject.attackThree
    attackList = [attack1, attack2, attack3]  # list of attacks corresponding to chosen pokemon

    # Display attacks for chosen Pokemon for current battle
    time.sleep(0.6)
    print("\n")

    print(dash)
    print('{:>24}'.format(str(playerObject.name) + "'S MOVES"))
    print(dash)

    for attackIndex in range(len(attackList)):
        print(str(attackIndex + 1) + ":", attackList[attackIndex])
    print("\n")
    time.sleep(0.6)

    # check for correct INPUT for attack:
    while checkAttack:
        try:
            attackChosen = int(input("What move would you like to use? (#): "))
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

    # Address change in turn in battle, index attack randomly selected for ENEMY
    print("\nEnemy", enemyPokemon.name, "used",
          str(enemyPokemon.attackList(enemyPokemon, (enemyAttackChosen - 1))) + "!")

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
        # single round begins - Player attacks first
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

        # single round continues - Enemy CPU goes second
        enemyAttack(enemyTurn, playerTurn)
        # check for winner
        winner = checkHealth(playerTurn.health, enemyTurn.health, Player(), Enemy())

        if winner == "player":  # fake 'enum' type usage in order assert winner of round
            print("\nYou have won the battle!\n")
            break
        elif winner == "enemy":
            print("\nPokemon Trainer RED won the battle!\n")
            break

        print("\n")

        # ATTACK ROUND STATS - At the end of each of the player's and enemy's attack display total information
        dash = '-' * 30
        print(dash)
        print('{:>4s}{:>18}'.format("PLAYER", "ENEMY"))
        print(dash)
        print('{:>2s}{:>13s}'.format(playerTurn.name, enemyTurn.name))
        print('{:>2s}{:>16s}'.format(playerTurn.kind, enemyTurn.kind))
        print('{:>2s}{:>16s}'.format(str(playerTurn.health), str(enemyTurn.health)))
        print('HP: {:>2s}    HP: {:>4s}'.format(str(playerTurn.healthBars), str(enemyTurn.healthBars)))


# Encompasses all aspects of the game - choosing pokemons, battle rounds, wins/loses, restarting game
def playGame(playerObject, enemyObject):

    # Global Objects Created to be used between GUI classes and text-based game classes
    global PLAYER
    PLAYER = playerObject
    global ENEMY
    ENEMY = enemyObject

    newRound = True

    # Run GUI application main loop before proceeding with text-based game.
    app = PokemonGUIApp()
    app.mainloop()

    while newRound:
        continueCheckingForInput = True

        # assign global enemyPokemonChosen and playerPokemonChosen created in GUI class PageTwo() as variables for \
        # battle round
        global playerPokemonChosen
        global enemyPokemonChosen


        enemyPokemon = enemyPokemonChosen
        playerPokemon = playerPokemonChosen

        print("\nGO!", playerPokemonChosen.name + "!")

        # Battle round begins
        battle(playerPokemon, enemyPokemon)  # repeats until health of a player is zero

        # SINGLE BATTLE ROUND FINISHED
        while continueCheckingForInput:
            try:
                runProgram = input("Would you like to battle again? ").lower()
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
