
'''
Name: Natasha Ahammed
Date: October 31, 2019
File Name: Natasha_Ahammed_A3.py
Description: Program which takes users inputs and based on input will determine if the number and present number of sixes/multiples of sixes and the largest/second largest number
Test Cases: Try and Except ensures that values are either numbers, or the values of 'r' or 'd', otherwise runs except, different data types tested
'''
import random

countSixes = 0
execute = True
userInput = 0
previous = 0

largeNum = int(0)
smallNum = int(0)
secondLarge = 2000

while execute == True:

    
    userInput = input("Enter an integer or 'r' for random or 'd; for done: ")
    if userInput != "r" or userInput != "d":
        print("you entered", userInput) #number entered 
        
    if userInput == "r": 
        userInput = random.randint(1,10) #random number assigned 
        print("new r:",userInput)

    if userInput == "d":
        print("Exit program")
        break #user wants to exit program to print results

    if (int(userInput) == 6) or ((int(userInput) % 6) == 0): #evaluate occurances of 6 
        countSixes += 1
        print(countSixes)

    #evaluate larger and second larger numbers 
    if (int(userInput)) > int(largeNum):
        largeNum = userInput
        print("greater than previous")
        #largest

    if int(userInput) < int(largeNum):
        #second largest
        secondLarge = userInput
        print("less than previous")

    if int(secondLarge) < int(userInput):
        #smaller number largest
        smaller = userInput
        ("less than previous")

   
print("no. of sixes =", countSixes)
print("Largest =", largeNum)
print("2nd largest =", secondLarge)

  
