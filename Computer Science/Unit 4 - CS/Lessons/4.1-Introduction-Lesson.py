#Introduction - 4.1 - Lesson

#Built In Functions

#***ALL FUNCTIONS SHOULD BE AT TOP*** then include main code

#Always available - type(), print(), input()

#Built in Modules - eg) math and random module -- functions - math.sqrt(), math.sin(), random.randint

#Methods - just like functions - but defined in class, for example string.lower()

#User Defined Functions - something for program to do that doesn't exist in program

def happy():
    print("Happy birthday to you!") #not run until happy() is called

#less code duplication
#Example One
happy()
happy()
print("Happy birthday, dear Fred")
happy()


#Revised Example

def happy():
    print("Happy birthday to you!")

#You can call functions inside of other functions 
def sing():
    happy()
    happy()
    print("Happpy birthdy, dear Fred!")
    happy()

#Main Program
sing()


#Revised Example 2
#Use can pass information into function called parameter 
def happy():
    print("Happy birthday to you!")

#You can call functions inside of other functions 
def sing(name): #accepts a parameter, to be given a value 
    happy()
    happy()
    print("Happpy birthdy, dear", name + "!")
    happy()

sing("Chris") #Now the value for name is defined and can be run as name = Chris

#RETURN--will do whatever was in the function 
'''
The Structure

def nameofFunction(parameters): #HEADING - defining - variable list as parameters to be passed in function

    do something #Executed each tume function is called 
    do something else #BODY 
    blah

nameOfFunction("datatype instance")

1) Program execution is suspended at the point of call
2) parameters get assigned the values supplied by the arguments in call
3) The body of the function is executed
4) Returns to the point just after where the function 
'''

#4.1-In Class Lesson Practice

#1) login info

def login():
    try:
        username = str(input("Enter the user name: "))
        password = str(input("Enter the password: "))
        print(username)
        print(password)
    except:
        print("Incorrect info")

login() #able to create new instances of username and password

#2) Average marks


def average():
    #***Have to assign variables locally, within function 
    total = 0
    average = 0 
    marks = 0 

    
    for marks in range(0,5):
        marks += 1 
        mark = int(input("Enter a mark: "))
        total = total + mark
    average = round((total / marks), 2)
    print("The average is,",average)

average()

'''
Cannot use argument labels
def printHello(to name: "You!"): dont have to explicity declare type
    print("Hello ", name)

printHello(to: "Chris")
printHello(to: Johnny)
'''    



