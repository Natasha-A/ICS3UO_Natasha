#4.4 - Lesson - Using Functions
#Reduce code reuse in our programs - use functions to develop a simple algorithm
import random
'''
#Writing Efficient Code - write code once, call it multiple times with different values

#Example 1 - Simple Game: Dice Roll

#Version #1 - NO FUNCTIONS
p1d1 = random.randint(1,6)
p1d2 = random.randint(1,6)
p1d3 = random.randint(1,6)
p1d4 = random.randint(1,6)

p2d1 = random.randint(1,6)
p2d2 = random.randint(1,6)
p2d3 = random.randint(1,6)
p2d4 = random.randint(1,6)

player1 = p1d1 + p1d2 + p1d3 + p1d4
player2 = p2d1 + p2d2 + p2d3 + p2d4

if player1 > player2:
    print("Player one wins")
elif player1 < player2:
    print("Player two wins")
else:
    print("tied")


#Version 2 - USE FUNCTIONS

def sumDice():
    for roll in range(4): #Takes 4 random rolls, adds to total
        total += random.randint(1,6)
        return total

#Main Program
player1 = sumDice() #called two instances of total for each player
player2 = sumDice()

if player1 > player2:
    print("Player 1 wins!")
elif player1 < player2:
    print("Player 2 wins!")
else:
    print("It's a tie")


#Using functions to help implement algorithms - problems solving is isolated into sections,
    #makes easier to disect instead of solving all at once

#***Example 3 - Calcuate the sum of the first n integers and odd integers***
'''

def getInt():
    while True:
        try:
            n = int(input("Enter a positive integer: ")) #Get integer - input, check for
            #correct data type

            if n >= 0:
                #print("*pos. int entered*") #confirm what time of integer is inputted
                break

            if n <= 0:
                #print("*neg. int entered*") #see that a negative int was inputted 
                x = 5/0 #forces except*** can use any incorrect operation that forces the program to crash when this negative constraint is met, so that it will go to except and force a
                #postive input instead each time.
                
        except:
            print("Incorrect Input. Please enter a positive integer below.")
        
    return n #returns value if computated


def sumFirstIntegers():
    amountOfNums = getInt() #uses getSum() function for data input 
    numSum = 0
    for num in range(1,(amountOfNums+1)):
        numSum += num

    total = print("The sum of these consecutive integers is", numSum)
    return total


def sumOddIntegers():
    amountOfNums = getInt()  #uses getSum() function for data input
    odd = 1
    oddSum = 0
    count = 0 
    while (odd % 2) != 0:
        oddSum = oddSum + odd
        odd = odd + 2
        count += 1

        if count >= amountOfNums:
            newOddSum = print("The odd sum is", oddSum)
            break


    return oddSum
    

#Main program
playAgain = ""

while playAgain != "no":
    sumFirstIntegers()
    sumOddIntegers()
    try:
        playAgain = input("Would you like to play again? (Enter Yes/No):").lower() #repeats program based on user input 
        if (playAgain == "yes") or (playAgain == "no"): #if either yes/no is met, able to continue with program conditions
            print("correct input")
        else:
            x = 5/0 #otherwise, forces except
            playAgain == "" #resets value of playAgain to evaluate in except 
    except:
        while (playAgain != "yes") and (playAgain != "no"): #checks to see if user input is NOT yes/no, which if true, the program will ask the user to input the correct response
            playAgain = input("Incorrect Input. Please enter again \nWould you like to play again? (Enter Yes/No):").lower()

           

    
            
            
        
        
        

