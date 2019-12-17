#REDONE - using Teacher Example - Assignment Three (Repeition)

import random

highest = -10000000000 #extremely small number in order to not be evaluated as highest first time looped
highest2nd = -100000 # extremely small number (greater than highest) so not second highest first time around (first number is second highest first)

entry = input("Enter an number or 'r' or 'd': ") #have to ask in begining too !

while entry != "d": #evaluates whether program will continue to run or not
    numberGood = False

    #Choose how 
    if entry == "r":
        num = random.randint(1,10) #creates a random number
        numberGood = True #While numberGood is true,
        print("random number generated:", num)
    else:
        try:
            num = int(entry) #convert to int to handle as number 
            numberGood = True
            print("You entered", num)
        except:
            print("Wrong entry please try again.")


    #Evaluate all the cases of the number to sort into category to display
    if numberGood == True:
        if num > highest: #if number is greater than highest..
            highest2nd = highest #highest is assigned as 2nd highest
            highest = num #number is the highest
        elif num < highest and num > highest2nd: #if the number is less than the highest,
            #while being greater than the second highest, evaluated as second highest...
            highest2nd = num #num evaluated as second highest

    entry = input("Enter an number or 'r' or 'd: ") #loops through asking user to enter input for rest of program 

print("Largest =", highest)
print("2nd largest =", highest2nd)

  


