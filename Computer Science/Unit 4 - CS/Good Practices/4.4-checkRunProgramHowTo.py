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
            
        if randomNumber % 2 == 0 or randomNumber == 9 or randomNumber == 2:
            numOfEvens += 1
        
        else:
            numOfOdds += 1

    evens = print("The number of even numbers generated are:", numOfEvens)
    odds = print("The nuber of odd numbers generated are:", numOfOdds)


#EXTENSION - check to run program 
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
while checkRunProgram(): #while this is true... (continues looping until "no")
    isEven() #displays program

print("Program ended")
