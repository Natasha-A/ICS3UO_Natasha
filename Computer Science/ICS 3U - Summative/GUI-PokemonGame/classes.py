'''
Name: Natasha Ahammed
Date: January 16 2020
File Name: Natasha_Ahammed_SummativeCS.py
Description: Pokemon Game Based off of Turn-Based Battles. Player battles with Computer AI in a series of rounds \
where a pokemon is chosen and different attacks can be chosen yielding in different amounts of damage or healing \
health. Whoever is able to cause one the opponent's pokemon to faint first, wins the the battle.
Test Cases: Made use of exploratory testing to examine UI display and game play loop. Played using various \
combinations, testing all functions individually and collectively. Use of Try and Except to handle error handling
for user inputs, and Integration Testing to ensure that algorithms produced correct results and no logic errors. Made
use of PyCharm's Automated Testing in order to detect and replace unreachable code.

- GUI APPLICATION -
As a part of extended research and understanding of application development, I decided to create an intro GUI interface.
Working with Tkinter offers many benefits since it's framework is very expansive and flexible to work with. Coupled
trial/error and investigating through documentation I was able to create a interface despite my limited
experience with application life cycles. Please ignore the globals within the GUI classes. I had to do what I had to do.

You must click the respective button in order to continue. If the interface does not populate or crashes,
just exit the window and the text-program will continue to run.

- REVEALED ASPECTS -
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

# CONSTANTS
LARGE_FONT = ("Courier", 18)

# *********** CLASS OBJECTS ***********

class Pokemon():
    attackList = []

    def __init__(self, name="None", health=100, healthBars="==========", kind="None", attackOne="None",
                 attackTwo="None",
                 attackThree="None", image="No Image"):
        self.allPokemon = []
        self.name = name
        self.health = health
        self.healthBars = healthBars
        self.kind = kind
        self.attackOne = attackOne
        self.attackTwo = attackTwo
        self.attackThree = attackThree
        self.image = image

    # displays main stats during battle
    def playerInfo(self):
        return '-- Player Info --\nName: {}\nHealth: {}\nHP: \n'.format(
            self.name,
            self.health,
            self.healthBars)

    # Creates list of of attack attributes used by Enemy Chosen Pokemon
    @staticmethod
    def attackList(self, numberChosen):
        enemyAttackList = [self.attackOne, self.attackTwo,
                           self.attackThree]

        return enemyAttackList[numberChosen]


class Player(Pokemon):
    def __init__(self, name="None", health=100, healthBars="==========", kind="None", attackOne="None",
                 attackTwo="None",
                 attackThree="None", image="No Image"):
        super().__init__(name, health, healthBars, kind, attackOne, attackTwo, attackThree, image)

    @staticmethod

    # Allow player to select pokemon from list
    def selectPokemon(self, pokemonSelected):
        pokemons = playerPokemonList()

        return pokemons[int(pokemonSelected)-1]  # print out pokemon at index of chosen pokemon (1,2,3)
        # returns instance of pokemon -- eg, charmander, bulbasaur, squirtle


class Enemy(Pokemon):

    def __init__(self, name="None", health=100, healthBars="=====", kind="None", attackOne="None", attackTwo="None",
                 attackThree="None", image="No Image"):
        super().__init__(name, health, healthBars, kind, attackOne, attackTwo, attackThree, image)

    # Enemy chooses pokemon at random
    @staticmethod
    def randomPokemonSelected(self):
        pokemons = enemyPokemonList()
        pokemonChosen = random.choice(pokemons)

        return pokemonChosen

