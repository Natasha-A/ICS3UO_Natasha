
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

largeNum = 0
smallNum = 0
secondLarge = 0

while execute == True:
    try:
        userInput = input("Enter an integer or 'r' for random or 'd; for done: ")
        previous = int(userInput) 
        if userInput != "r" or userInput != "d":
            number = int(userInput)
            print("you entered", number)
            
        if userInput == "r":
            userInput = random.randint(1,10)
            print("new r:",userInput)

        if userInput == "d":
            print("Exit program")
            break

        if (int(userInput) == 6) or ((int(userInput) % 6) == 0):
            countSixes += 1
            print(countSixes)

        if int(userInput) > previous:
            largeNum = previous
            print("The largest number is:", largeNum)

        if int(userInput) < largeNum:
            secondLarge = previous
            print("A smaller number is:", secondLarge)

        if secondLarge < int(userInput):
            print("The second largest number is", secondLarge)

    except:
        print("This is not a valid entry... try again")



print("no. of sixes =", countSixes)
print("Largest =", largest)
print("2nd largest =", secondLarge)


