#4.2 - Lesson - Returning a Value
#"fruitful functions"
import random
'''
#these are void functions - can have parameters, but do not pass info back to main program 
def happy():
    print("Happy birthday to you!")

def sing(name):
    happy()
    happy()
    print("Happy birtday dear", name + "!")
    happy()

#Example 1

num = random.randint(1,10) #We can catch the value and assign it to the variable called num, example of a f
#fruitful function, randint
print(num)

#Example 2 - returns a value back to the main program

Basic Syntax

def nameOfFunction (parameters):
    body of function

    return value1, value2
'''
print("\n")

#***NOTE: Does return do the same thing as printing?***
def difference(a,b):
    answer = a - b
    print(answer) 
    return answer #Printing doesnt mean it will be evaluated, but return will evaluate. If commented
    #out, then function has no information called, 

#Main program - evalue differences 
n = difference(5,3) #with return, answer can be held 
print("outside of the function, n =", n) #

print("\n")

#Example - Return Difference of Two numbers
def findDifference(num1, num2): #Code will run with num1 = 7, and num2 = 2, the difference is found
    #and returned to the main 
    difference = num1 - num2 

    return difference

#Main Program
d = findDifference(7,2) #The value returned is now saved in the variable called d. That is, d has been
#assigned the return value of seven and two
print(d) #Arguments, num1 and num2 are passed in with the values 7 and 2 respectively

print("\n")

#Example 3 - Even or Odd - determines if number is even or odd

def isEven(num):
    if num % 2 == 0:
        return True #can have multiple returns 
    else:
        return False

#Main Program
result = isEven(13) #now have two different ways of printing values returned from a function 
print(result)
print(isEven(22))

#Example 4 - NOTE: Placement of return keyword
#when called, the function returns to the point where it was called immediately, Any code after the
#return statement will not be executed

#Instance, nothing is ever printed to the screen, because print statement follows return
def addNum(num1, num2):
    sum = num1 + num2

    return sum
    print("The sum is", sum)

#Main Program
s = add_sum(3,5) #this code prints NO output, Need to move print statement above return 




