#3.4 Exercise - Random Module - Day 2
import random

#Day 2 - Random Module and Simulation

#Example - guessing game
numTries = 0
numToGuess = random.randint(1,100)
won = False
guess = 0 

unlimitedTries = True

print("If you wish to exit the name, enter -1")
while unlimitedTries == True and not(won):
    if guess != -1:
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
    else:
        break

if won:
    print("Yay! You won!")
else:
    print("You lost!")
    

#Rock Paper Scissors
won = False 
computerChoice = ""

while not(won):
        userChoice = input("Play against the computer! Rock! Paper! Scissors! (R/P/S): ")
        computerChoice = random.choice("RPS")
        if computerChoice == "S" and userChoice == "R":
            print("Computer Choice: S, User: R")
            won = True
        if computerChoice == "R" and userChoice == "P":
            print("Computer Choice: R, User: P")
            won = True
        if computerChoice == "P" and userChoice == "S":
            print("Computer Choice: P, User: S")
            won = True
        elif computerChoice == userChoice:
            print("You have entered the same choice as the computer, try again.")
        elif userChoice == "R" or userChoice == "S" or userChoice == "P":
            print("You lost, try again.")
        else:
            print("You have entered the incorrect choice type, try again.")

if won:
    print("You have won!")

        
