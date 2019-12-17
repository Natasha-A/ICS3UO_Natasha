#***4.5 - Menu Driven Program: Using Functions to create a calculator***

def getOption():
    print(" ")
    print("Your options are:")
    print(" ")
    print("1) Addition", "2) Subtraction", "3) Multiplication", "4) Division", "5) Quit Calculator", sep="\n")

    while True:
        try:
            print("")
            choice = int(input("Choose your option: "))

            if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
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


#Revision 1 - removed need to display each evaluation, program computates itself using eval() function
def printComputation(n1, n2, choice):
    print("function called")
    
    operators = ["invalid", "+", "-", "*", "/"] # 1 - "+", 2 - "-", 3 - "*", 4 - "/"

    calculation = 'str(n1) + str(operators[choice]) + str(n2)'
    strResult = eval(calculation) #evaluate as string concecated
    numResult = eval(strResult) #evalute as integers
          
    print("The answer is:", n1, operators[choice], n2, "=",  numResult)


def calculateNums():
    print("")
    print("- Welcome to the Calculator Program -")
    choice = getOption() #prints out all the options, then computates choice 

    num1,num2 = getInput() #prints out inputs, them computates numbers 
    
    while choice != 5:
        printComputation(num1,num2,choice)
        print("")

        #Reask for next instance
        choice = getOption() 
        num1,num2 = getInput() 

    print("Thank you for using our calculator ")


#Main program
calculateNums()
