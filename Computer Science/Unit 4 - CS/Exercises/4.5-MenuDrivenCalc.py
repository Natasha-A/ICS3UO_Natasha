#4.5 - Menu Driven Programs - Calcuator Program

'''
Program - Version #1 - Algorithm
- Print opening message

- Print the options (Add, Subtract, Multiply, Divide, and Quit)

- Get the menu option

While the user doesn't want to quit:
    - Get and error check two numbers
    - If the option is 1, add
    - If the option is 2, subtract
    - If the option is 4, divide
    - Print the options (Add, Subtract, Multiply, Divide, and Quit)
    - Get the next menu option

- Print goodbye message
'''

'''
Program - Version #2 - Python Code
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

choice = int(input("Choose your option: "))

while choice != 5:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("The answer is:", num1 + num2)

    elif choice == 2:
        print("The answer is:", num1 * num2)

    elif choice == 4:
        print("The answe is:", num1 / num2)

    print(" ")
    print("Your options are:")
    print(" ")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit Calculator")
    print(" ")

    choice = int(input("Choose your option: "))

 print("Thank you for using our calculator ")
'''

#Version 3 - Using Functions to create a calculator 

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





            
            

    

    
    
    
    
