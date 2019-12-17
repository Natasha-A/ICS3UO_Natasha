#3.4 Lesson - Random Module
import random
#contains functions tha generate random numbers, make random selections, shuffle lists

#1) Randint - generates random integer between two values
#random.randint(LOW,HIGH)

#Inclusive range - meaning the ranfom int will be between LOW and HIGH, or may be LOW or HIGH
spin = random.randint(1,10)
print(spin)

#2) Randrange - random int between LOW and HIGH

#The value of STEP acts as a "count by" value -- if STEP = 2 count by twos, HIGH is not included in range of values, but LOW is 
randomEven = random.randrange(0,11,2)
print(randomEven)

#3) Random - floating number between 0 and 1 inclusive

#generate a number between 0 and 1 inclusive
randomFloat = random.random()
print(randomFloat)

#generate a number between 0 and 20 inclusive
randomNum = 20*random.random()
print(randomNum)

#4) Choice - selects a random charater from a string

#random.choice(string)
vowel = random.choice("AEIOU")
print(vowel)

#You Try
#random.choice(string)
coinFlip = random.choice("HT")

if coinFlip.lower() == "h":
    print("Heads")
if coinFlip.lower() == "t":
    print("Tails")

#Day 2 - Random Module and Simulation

#Example - guessing game
numToGuess = random.randint(1,100)
numTries = 0
won = False 
while numTries < 5 and not(won):
    #Ask user the guess
    guess = int(input("Guess a number between 1 and 100: "))
    numTries += 1
    
    #check to see if the guess is correct. Output result
    if guess == numToGuess:
        won = True #Able to stop looping through game, since won already
        #can add "break" to break out of loop and go to true/false condition
    else:
        if guess < numToGuess:
            print("Your guess was too low!")
        else:
            print("Your guess was too high!")
        print("Try again")

if won:
    print("Yay! You won!")
else:
    print("You lost!")
    
    
