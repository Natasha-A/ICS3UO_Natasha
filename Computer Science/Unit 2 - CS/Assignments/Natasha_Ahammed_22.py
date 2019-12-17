'''
Name: Natasha Ahammed
Date: October 7, 2019
File Name: Natasha_Ahammed_22.py
Description: Program which takes change in pennies and determines the least amount of coins to add up to its sum and presents concisely using plural/singular keyworks and error handling for negative values
Test Cases: Positive/negative integers, coin amounts inputted that would result in a value greater than 1, equal to 1, or equal to 0 tp check for proper outputs based on cases. 
'''

#User enters change in cents 
coins = int(input("Enter the amount of change you require in cents (between 1-499): "))

#Calculate coin types needed based on amount
toonies = coins // 200
remainingChange = coins % 200
loonies = remainingChange // 100
remainingChange = remainingChange % 100
quarters = remainingChange // 25 
remainingChange = remainingChange % 25
dimes = remainingChange // 10 
newRemainingChange = remainingChange % 10
nickels = newRemainingChange // 5
newRemainingChange = remainingChange % 5
pennies = newRemainingChange

if coins >= 0: #If coins are greater than zero, program continues
    #Check how many toonies: If there is more one than one, present as plural. If only one, present as singular. If there are zero, do not present and set to false
    if toonies > 1:
        valueToon = str(toonies) + " toonies"
    elif toonies == 1:
        valueToon = str(toonies) + " toonie"
    elif toonies == 0:
        valueToon = False

    #Repeat with Loonies
    if loonies > 1:
        valueLoon = str(str(loonies) + "loonies")
    elif loonies == 1:
        valueLoon = str(str(loonies) + " loonie")
    elif loonies == 0:
        valueLoon = False

    #Repeat with Quarters
    if quarters > 1:
        valueQuart = str(str(quarters) + " quarters")
    elif quarters == 1:
        valueQuart = str(str(quarters) + " quarter")
    elif quarters == 0:
        valueQuart = False

    #Repeat with Dimes
    if dimes > 1:
        valueDime = str(str(dimes) + " dimes")
    elif dimes == 1:
        valueDime = str(str(dimes) + " dime")
    elif dimes == 0:
        valueDime = False

    #Repeat with Nickels
    if nickels > 1:
        valueNickel = str(str(nickels) + " nickels")
    elif nickels == 1:
        valueNickel = str(str(nickels) + " nickel")
    elif nickels == 0:
        valueNickel = False

    #Repeat with Pennies
    if pennies > 1:
        valuePen = str(str(pennies) + " pennies")
    elif pennies == 1:
        valuePen = str(str(pennies) + " penny")
    elif pennies == 0:
        valuePen = False
        
    #Print out least amount of coins based on determined amount caluated above
    print("The least number of coins is: ")
    if valueToon != False:
        print(valueToon)
    if valueLoon != False:
        print(valueLoon)
    if valueQuart != False:
        print(valueQuart)
    if valueDime != False:
        print(valueDime)
    if valueNickel != False:
        print(valueNickel)
    if valuePen != False:
        print(valuePen) 
else:
    print("Sorry you need to enter a positive integer to use this program.") #If coins were less than zero, (neg. value) error message printed
    
