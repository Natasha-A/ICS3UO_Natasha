
#4.1-Day 2 - Lesson: Parameters
import random
'''
#Parameters - allows the main program to pass in info to the function

def printHello(): #no parameters passed into func, body will simply run 
    print("Hello")

def printWelcome(name): #parameter called "name", when func is called, value passed in\
    #will be stored and used in "name" within body of the function when run 
    print("Welcome", name)

#Main program
printHello()
printWelcome("Fred")
printHello()
printWelcome("Barney")

#Example 1: Using for and random - no parameters

def sumDice():
    sum = 0 #local var
    for roll in range(4):
        sum += random.randint(1,6) #sum of 4 random dice
    print("The sum is", sum)

#Main program
sumDice()

#Example 1: Using for and random - WITH parameters

def newSumDice(n):
    sum = 0
    for roll in range(n): #new value of n assigned when func is called 
        sum += random.randint(1,6)
        print(sum)
    print("1: The sum is", sum)

print("Five numbers:")
#vale of n inside function will be assigned the value of the parameter
#when the function is called:
newSumDice(5) 
print("Two numbers:")
newSumDice(2)
print("Ten numbers:")
newSumDice(10)

#Example 2: print the number of diagonals in a polygon using formula 
def numDiag(edge):
    d = edge * (edge - 3) / 2
    print("The number of diagonals are", d)

#main Program
numDiag(8)
numDiag(12)
'''

#Functions with MULTIPLE Parameters

#Example 1
def printTwoThings(x,y):
    print("x is", x)
    print("y is", y)

printTwoThings("Hello", "world!")

#YOU TRY

#1)
def printMin(x,y):
    if x < y: #calulates between values provided 
        print(x, "is the lowest")
    if y < x:
        print(y, "is the lowest")

printMin(-5,6) #provides values for x and y to calculate
printMin(5,0)

#2)
def printArea(l,w):
    area = l * w #calculates area
    print(area)

printArea(5,6)
printArea(8.9,5.5)

