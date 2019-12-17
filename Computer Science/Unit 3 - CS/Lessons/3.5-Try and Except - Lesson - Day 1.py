#3.5 - Repetition - Try and Except - Lesson - day 1
#Input checking and error prevention - revisted with loops and try/except
import math

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

*************************
try:
    <code to run>
except:
 #it will always run - as long as program crashes, except will be executed
    <code to run if exception was raised>
*******************************
'''
quotient = 1

#Example 1
try:
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    quotient = num1 / num2 #error met, does not present quotient, instead will print except
    print("the quotient is: ", quotient) 

except:
    print("You need to enter a number!")



#Example 2 - practice with try wiht class
import math

numberOne = float(input("Enter first number: "))
numberTwo = float(input("Enter second number: "))
try:
    squareRootFirstNumber = math.sqrt(numberOne)
    print("The first number", numberOne, "CAN be square rooted.")
except:
    print("The first number", numberOne, "CANNOT be square rooted.")

try:
    squareRootSecondNumber = math.sqrt(numberTwo)
    print("The second number",numberTwo, "CAN be square rooted.")
except:
    print("The second number",numberTwo, "CANNOT be square rooted.")
'''
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
#Try and Except - With Looping *** BASIC STRUCTURE going forward - infinite loop ***
#User is stuck in the loop until they enter only two good numbers, until that happens the rest of the code will not be executed using the numbers 
while True:
    try:
        num1 = float(input("#Enter number 1: "))
        num2 = float(input("#Enter number 2: "))
        print("The numbers are: ", num1, "and", num2)
        break #if you get the two numbers, breaks from the loop, and continues on with code
    except:
        print("You need to enter a number!") #this is an infinite loop

#Working with Try and Except - Additional Checks
#Checking that the second number is not 0

#Checking as long as the second number is not 0, and there are proper integers, then it will print quoitent, if the second number is not zero, and the first number is not an integer, then the execpt will be run 
num_2 = 0
num_1 = 0
 
while num_2 == 0: #Loop will continue checking for new numbers if the second one remains as 0
    try:
        num_1 = float(input("A:Enter number 1: "))
        num_2 = float(input("A:Enter number 2: ")) #once condition are met, the quotient is created 
    except:
        print("You need to enter two numbers and the second number can't be 0!")

quotient = num_1/num_2
print("The quotient is: {:.2f}".format(quotient)) #{:.2f} rounds the quotient to 2 decimal places

#You try - ensure dataType of the inputted data is correct AND also perform any additional checks as required by the program 
#Read a number from the user and output its square root:
newNum = -1

while newNum < 0: #continues looping to enter a number that is not less than zero 
    try:
        newNum = float(input("Enter a number: "))
    except: #if a character other than a number is inputted
        print("You need to enter a positive number!") #continues repeating, since newNum is still less than 0

square_root = newNum**0.5 #Same as performing square root operartion

print("The square root is: {:.2f}".format(square_root))


