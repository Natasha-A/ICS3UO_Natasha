#Unit 4 - Assigment Review
import math, random

# (1) 4.4 Lesson - Example 3 - calculate sum of n integers and odd integers

'''6
def getInput():
    while True: 
        try:
            userInput = int(input("Enter the num of integers to calcuate from: "))

            if userInput >= 0:  #postive value inputted 
                break

            if userInput <= 0:
                x = 5/0 #forces except

        except: #for negative integers and non-int values
            print("Incorrect input. Please enter a positive integer below.")

    return userInput

def sumFirstInts():
    amountNum = getInput()
    totalSum = 0

    for num in range(1, (amountNum + 1)):
        totalSum += num

    #create instance of total to return and print 
    total = print("The sum of the consecutive integers is", totalSum)

    return total

def sumOddInts():
    amountNum = getInput()
    totalOddSum = 0
    odd = 1

    for num in range(1, (amountNum + 1)):
        if (num % 2) != 0:
            totalOddSum += num

    totalOddSum = print("The sum of the consecutive odd integers is", totalOddSum)

    return totalOddSum


#check to run program

def checkRunProgram():
    runProgram = "yes"

    while True:
        try:
            runProgram = input("Would you like to run the program again? ").lower() #if "yes", program runs again
            #print("printed as:", newProgram)

            if runProgram == "yes":
                return True #if yes, continues running 

            if runProgram == "no":
                return False #no longer runs 
            
            else:
                x = 5/0 #Forces except to be run, since value is not either yes/no - until true will keep running 
        except:
            print("incorrect input") #runs, and then escapes back to while statement 



#main program

while checkRunProgram(): #check state of continueRunProgram 
    sumFirstInts()
    sumOddInts()

print("Program ended")

# (2) 4.4 - Exercise 2 - factorials 

def factorial():
    numAmount = getInput()
    productOfDigits = 1
    previous = 1 

    for digit in range(1, (numAmount + 1)):        
        productOfDigits = previous * digit 
        print(digit, "x", (previous), "=", productOfDigits)

        previous = productOfDigits 


    total = print("The total product of the factorial of", numAmount, "is", productOfDigits) #after displaying computation, shows the total amount for the factoral

    return total

#MAIN PROGRAM
factorial()

while checkRunProgram():
    factorial()


#***4.5 - Menu Driven Program: Using Functions to create a calculator***

def getOption():
    print(" ")
    print("Your options are:")
    print(" ")
    print("1) Addition", "2) Subtraction", "3) Multiplication", "4) Division", "5) Quit Calculator", sep="\n")

    while True:
        try:
            choice = int(input("Choose your option: "))

            if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
                #print("correct input")
                break
            else:
                x = 5 / 0 #force crash to evaluate except

        except:
            print("Incorrect input - enter a number between 1-5")


    return choice #returns either 1,2,3,4,5


def getInput():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
            
        except:
            print("Please enter a number below.")

    return num1, num2

def printComputation(n1, n2):
    choice = getOption()
    
    #1 - "+", 2 - "-", 3 - "*", 4 - "/"

    operators = ["invalid", "+", "-", "*", "/"]

    print(answerStatement = print("The answer is:", n1, operators[choice], n2, "=", end=" "))


def calculateNums():
    print("")
    print("Welcome to the Calculator Program")
    choice = getOption() #prints out all the options, then computates choice 

    num1,num2 = getInput() #prints out inputs, them computates numbers 
    
    while choice != 5:
        if choice == 1:
            printComputation(num1,num2)
            print(round(num1 + num2,2))

        elif choice == 2:
            printComputation(num1,num2)
            print(round(num1 - num2,2))

        elif choice == 3:
            printComputation(num1,num2)
            print(round(num1 * num2,2))

        elif choice == 4:
            try:
                printComputation(num1,num2)
                print(round(num1 / num2,2)) #if the second number is zero, answer is undefined, thus goes to except
            except:
                print("The second number cannot be zero.")



    print("Thank you for using our calculator ")

#Main program
calculateNums()


########VERSION 2 - without extra printComputation() function#######

def getOption():
    print("Welcome to the Calculator Program")

    print(" ")
    print("Your options are:")
    print(" ")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit Calculator")
    print(" ")

    while True:
        try:
            choice = int(input("Choose your option: "))

            if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
                #print("correct input")
                break
            else:
                x = 5 / 0 #force crash to evaluate except

        except:
            print("Incorrect input - enter a number between 1-5")
        

    return choice #returns either 1,2,3,4,5

def getInput():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            break
            
        except:
            print("Please enter a number below.")

    return num1, num2


#Main program 

def calculateNums():
    choice = getOption() #prints out all the options, then computates choice 


    while choice != 5:
        print("")

        num1,num2 = getInput() #prints out inputs, the computates numbers 
        
        if choice == 1:
            print("The answer is:", num1 + num2)

        elif choice == 2:
            print("The answer is:", num1 - num2)

        elif choice == 3:
            print("The answer is:", num1 * num2)

        elif choice == 4:
            try:
                print("The answer is:", round(num1 / num2,2)) #if the second number is zero, answer is undefined, thus goes to except
            except:
                print("The second number cannot be zero.")

        choice = getOption() #prints out all the options, then computates choice 



    print("Thank you for using our calculator ")


calculateNums()


#4.4 - Exercise - Using Functions
#1) - a to d

def getRadius():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            break

            assert radius > 0 # statement to test if it is true,(see if radius is pos/neg)

        except AssertionError: #when tested assertion as false 
          print("The value must be positive.")

        except ValueError: #tests against type
            print("The value must be an integer.")


    return radius 


def circumference(r):
    circum = math.pi * (r*2)

    return circum

def area(r):
    area = math.pi * (r**2)

    return area


#total outputs
def circleInfo():
    radius = getRadius()
    areaTotal = area(radius)
    circumfer = circumference(radius)

    printArea = print("The area of the circle is:", round(areaTotal,2), "units squared.")

    printCircum = print("The circumference of the circle is:", round(circumfer,2), "units.")

    return printArea, printCircum


def runProgramAgain():
    runProgram = ""

    while True:
        try:
            runProgram = input("Would you like to run the program again? ").lower()

            if runProgram == "yes":
                return True

            if runProgram == "no":
                return False

            assert runProgram == "yes" or runProgram == "no" #test input value

        except AssertionError:
            print("Incorrect input. Please enter 'yes' or 'no'.")

#Main program
circleInfo()       
while runProgramAgain():
    circleInfo()

'''
def getInput():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

    except ValueError:
        print("Please enter an integer")

    return num1, num2
        

def quotRem():
    num1, num2 = getInput()

    quot = num1 // num2

    remain = num1 - (num2 * quot)

    quotAns = print("The quotient is", quot)
    remainAns = print("The remainder is", remain)

    return quotAns, remainAns

quotRem()

'''
def runProgramAgain():
    while True:
        try:
            runProgram = input("Would you like to run the program again? ").lower()

            if runProgram == "yes":
                return True

            if runProgram == "no":
                return False

            assert runProgram == "yes" or runProgram == "no" #test input value

        except AssertionError:
            print("Incorrect input. Please enter 'yes' or 'no'.")

#Main program
circleInfo()
while runProgramAgain():
    circleInfo()

'''

#4.2 - returning a value: Calculating SA and V of a cylinder
#2)

def dimensionsInput():
    while True:
        try: 
            height = int(input("Enter the height of the cylinder: "))
            radius = int(input("Enter the radius of the cylinder: "))
            break

        except ValueError:
            print("Please enter a integer.")

    return height, radius


#make simple calculations seperate functions 
def areaCircle(radius):
    return 2 * math.pi * radius

def areaRectangle(length, width):
    return length * width

def circumference(radius):
    return (2 * radius) * math.pi
    
def cylinderSA():
    height, radius = dimensionsInput() #assign height and radius at end 

    SA = 2 * areaCircle(radius) + areaRectangle(circumference(radius),height)

    print("The surface area of the cylinder is,", SA)


cylinderSA() 



    
    
    
        




