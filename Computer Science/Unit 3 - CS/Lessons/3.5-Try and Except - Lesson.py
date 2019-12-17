#3.5 - Repetition - Try and Except - Lesson
#Input checking and error prevention - revisted with loops and try/except
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Error checking - using if statements 
#You can check for negatives, but cant handle cases such as letter inputs (data types)
#Only gives user one 
if num2 != 0:
    quotient = num1 / num2
    print("The quotient is: ", quotient)
else:
    print("The second integer is 0.")
    print("Please try again.")

#unlike if, will always run, no condition

#**Use try and except only for part that is pertinant to handling a specific error - minimize amount of lines in try**

try:
    <code to run>
except:
 #it will always run - as long as program crashes, except will be executed
    <code to run if exception was raised>


#Example 1
try:
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    quotient = num1 / num2 #error met, does not present quotient, instead will print except
    print("The quotient is: ", quotient) 
except:
    print("You need to enter a number!")


#Example 2 - practice with try wiht class
import math

try:
    numberOne = float(input("Enter first number: "))
    numberTwo = float(input("Enter second number: "))
    squareRootFirstNumber = math.sqrt(numberOne)
    print("The first number", numberOne, "CAN be square rooted.")
except:
    print("The first number", numberOne, "CANNOT be square rooted.")

try:
    squareRootSecondNumber = math.sqrt(numberTwo)
    print("The second number",numberTwo, "CAN be square rooted.")
except:
    print("The second number",numberTwo, "CANNOT be square rooted.")

#Boolean Datatype
x = 1
while x > 0:
    print("Repeat!") 


run_forever = True
while run_forever:
    print("This will run forever!")

while True:
    print("")
'''

'''
#Try and Except - With Looping *** BASIC STRUCTURE going forward - infinite loop ***
#User is stuck in the loop until they enter only two good numbers, until that happens the rest of the code will not be executed using the numbers 
while True:
    try:
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        break #if you get the two numbers, breaks from the loop, and continues on with code
    except:
        print("You need to enter a number!") #this is an infinite loop
        quotient = num_1/num_2

#Working with Try and Except - Additional Checks
#Checking that the second number is not 0
'''
num_2 = 0

while num_2 == 0:
    try:
        num_1 = float(input("Enter number 1: "))
        num_2 = float(input("Enter number 2: "))
    except:
        print("You need to enter two numbers and \
        the second number can't be 0!")

quotient = num_1/num_2
print("The quotient is: {:.2f}".format(quotient))
