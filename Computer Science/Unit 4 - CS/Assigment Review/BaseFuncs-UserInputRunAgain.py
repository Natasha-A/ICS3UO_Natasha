#Base Functions - To use for try and except and checking user input to continue
#running program
import random

# (1) Getting correct user input(based on if integer/post or neg...)
def getInput():
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

# (2) Generic user computation with user input....
def isEven():
    amountNum = getInput()
    numOfEvens = 0
    numOfOdds = 0

    for number in range(0,amountNum):
        
        randomNumber = random.randint(1,50)
            
        if randomNumber % 2 == 0 or randomNumber == 9 or randomNumber == 2:
            numOfEvens += 1
        
        else:
            numOfOdds += 1

    evens = print("The number of even numbers generated are:", numOfEvens)
    odds = print("The nuber of odd numbers generated are:", numOfOdds)


# (3) check with user in need to run program again...
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

            
#Main Program - check to run program continously
isEven()
while checkRunProgram(): #while this is true... (continues looping until "no"
    isEven() #displays program chosen



#Using Assertions - instead of forcing except using x = 5/0:

#EXAMPLE: 4.4 - Computate circumference, area, run program again
#using assert - runs as a condition to test the user input -- if it does not pass the condition, the value will be tested as false, and the AssertionError is run. 


def getRadius():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            
            assert radius > 0 # statement to test if it is true,(see if radius is pos/neg)
            break

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
                
            #ASSERTION
            assert runProgram == "yes" or runProgram == "no" #test input value

        except AssertionError:
            print("Incorrect input. Please enter 'yes' or 'no'.")

#Main program
circleInfo()
while runProgramAgain():
    circleInfo()
