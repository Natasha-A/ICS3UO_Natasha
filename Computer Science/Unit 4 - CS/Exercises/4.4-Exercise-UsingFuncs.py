#4.4 - Exercise - Using Functions
import math, random

'''
#a) ****circumference function****PP

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
'''
        

#2) ****Factorials - product of all postive integers down to 1****PP

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


runProgram = "yes"

while runProgram == "yes":
    factorial()
    try:
        runProgram = input("Would you like to run the program again? ").lower() #if yes, program runs again

        if runProgram == "no":
            break
        elif runProgram != "yes" and runProgram != "no":
            x = 5/0 #Forces except to be run, since value is not either yes/no
    except:
        while (runProgram != "yes") and (runProgram != "no"): #checks to see if user input is NOT yes/no, which if true, the program will ask the user to input the correct response
            runProgram = input("Incorrect Input. Please enter again \nWould you like to run again? (Enter Yes/No):").lower()



#3***Even Numbers and Prime Numbers***

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

runProgram = "yes"


while runProgram == "yes":
    isEven()
    print("")
    try:
        runProgram = input("Would you like to run the program again? ").lower() #if yes, program runs again

        if runProgram == "no":
            break
        elif runProgram != "yes" and runProgram != "no":
            x = 5/0 #Forces except to be run, since value is not either yes/no
    except:
        while (runProgram != "yes") and (runProgram != "no"): #checks to see if user input is NOT yes/no, which if true, the program will ask the user to input the correct response
            runProgram = input("Incorrect Input. Please enter again \nWould you like to run again? (Enter Yes/No):").lower()

    print("")


#4 - ***Prime Numbers***

#validate user input
def getPrimeInput():
    while True:
        try:
            n = int(input("Enter a number to display the number of prime numbers between it: ")) #Get integer - input, check for
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

#determine if number inputted is prime
def isPrime():
    amountNums = getPrimeInput()

    for num in range(1, (amountNums + 1)):
        if (num % 2) != 0 and (num != 9):
            print("num", num, "is prime")

#loop program - MAIN PROGRAM

runProgram = "yes"

while runProgram == "yes":
    isPrime()
    print("")
    try:
        runProgram = input("Would you like to run the program again? ").lower() #if yes, program runs again

        if runProgram == "no":
            break
        elif runProgram != "yes" and runProgram != "no":
            x = 5/0 #Forces except to be run, since value is not either yes/no
            
    except:
        while (runProgram != "yes") and (runProgram != "no"): #checks to see if user input is NOT yes/no, which if true, the program will ask the user to input the correct response
            runProgram = input("Incorrect Input. Please enter again \nWould you like to run again? (Enter Yes/No):").lower()

    print("")


