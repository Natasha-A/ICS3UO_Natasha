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



#PRACTICE TWOOO
#4.4 - Exercise - Using Functions
import math

#a) circumference function

#overall input statement to reuse
def getRadiusInt():
    while True:
        try:
            n = int(input("Enter the radius: ")) #Get integer - input, check for
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
        
    return n #returns value if computated (and breaks)

radiusInput = getRadiusInt() #instance of radius input

def circumference(r):

    equation = math.pi * (r * 2)

    circum = print("The circumference is", round(equation,2))

    return circum

#b) Area of a circle

def area(r):
    equation = math.pi * (r ** 2)

    area = print("The area of the circle is", round(equation,2))

    return area

#c) radius - with error checks - for floating number

def getFloatRadius():
    while True:
        try:
            n = float(input("Enter a floating number for the radius: "))

            if n >= 0:
                break

            if n <= 0:
                x = 5/0

        except:
            print("Incorrect input. Please enter a positive integer below. ")

    return n
        
def getRadius():
    radius = getFloatRadius()

    radiusOutput = print("The radius is", round(radius,2))

    return radiusOutput

circumference(radiusInput)
area(radiusInput)
getRadius()
    

#d) VERSION 3: compile together radius, circumference, and print results

runProgram = "yes"

def totalCircleInfo():
    radius = getFloatRadius()

    areaCir = area(radius)
    circum = circumference(radius)

    return areaCir
    return circum

#****how to check for if user enters yes/no and correct input
while runProgram == "yes":
    print("Total Circle Info: ")
    totalCircleInfo()
    try:
        runProgram = input("Would you like to run the program again? ").lower() #if yes, program runs again

        if runProgram == "no":
            break
        elif runProgram != "yes" and runProgram != "no":
            x = 5/0 #Forces except to be run, since value is not either yes/no
    except:
        while (runProgram != "yes") and (runProgram != "no"): #checks to see if user input is NOT yes/no, which if true, the program will ask the user to input the correct response
            runProgram = input("Incorrect Input. Please enter again \nWould you like to run again? (Enter Yes/No):").lower()

#EXAMPLE 3 - FACTORIALSS

#2) Factorials - product of all postive integers down to 1
'''
#1. Get input of number, handle error cases from input.
def getInput():
    while True:
        try:
            n = int(input("Enter a number to determine its factorial: ")) #Get integer - input, check for
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
        
    return n #returns value if computated (and breaks)

def factorial():
    num = getInput()
    previous = 1
    totalProduct = 0
    digit = 1
    
    for digit in range(1, (num+1)):
        productOfDigits = previous * digit
        print(digit, "x", (previous), "=", productOfDigits)

        #previous assigned at end of program
        previous = productOfDigits #***to multiple all together, have determine first result\
        #eg) 3 * 2 = 6, ask the first product. then can assign as previous, now multiply 6 * 4 = 24... 24 (previous) * 5 = 120

    total = print("The total product of the factorial of", num, "is", productOfDigits) #after displaying computation, shows the total amount for the factoral

    return total

factorial()

        

#****Version 3 - Using Functions to create a calculator****

def getOption():
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

choice = ""

while choice != 5:
    print("")
    print("Welcome to the Calculator Program")
    choice = getOption() #prints out all the options, then computates choice

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


print("Thank you for using our calculator ")


#3***Even Numbers and Prime Numbers***
import random

            
def getTestInput():
    while True:
        try:
            n = int(input("Enter the number of #'s you want to test as even/odd: ")) #Get integer - input, check for
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
        
    return n #returns value if computated (and breaks)

def isEven():
    amountNum = getTestInput()
    numOfEvens = 0
    numOfOdds = 0

    for number in range(0,amountNum):
        
        randomNumber = random.randint(1,50)
            
        if randomNumber % 2 == 0 or randomNumber == 9:
            numOfEvens += 1
        
        else:
            numOfOdds += 1

    evens = print("The number of even numbers generated are:", numOfEvens)
    odds = print("The nuber of odd numbers generated are:", numOfOdds)

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

            
#Main Program
while checkRunProgram(): #while this is true... (continues looping until "no"
    isEven() #displays program 







    


    
            
            
        
        
        

