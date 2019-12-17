#4.2 - Day 2 - Lesson: Returning Multiple Values
import math

#Example 1
#A function can return more than one value by listening them after the return statement
def sumProduct(numOne, numTwo):
    sum = numOne + numTwo
    product = numOne * numTwo
    return sum, product #returns two values back to the main program

#Main program
s, p = sumProduct(3,5) #Need to make sure that you use the same number of variables to store
#the results
print(s, p)

#Example 2 - Midpoint - returns the midpoint of the line segment

def midpoint(x1, y1, x2, y2):
    midx = (x1 + x2) / 2
    midy = (y1 + y2) / 2

    return midx, midy

#Main program
x,y = midpoint(9,4,-3,-4) #midx = x (stored in each variable), midy = y
print("The midpoint is, (" + str(x) + "," + str(y) + ").")

#LOCAL VARIABLES
#Variables INSIDE the functions are not accessible OUTSIDE the function

'''
def catTwice(part1,part2):
    cat = part1 + part2
    print(cat)

catTwice("Foo", "bar")
print(cat) #When catTwice terminates, the variable cat is destroyed, causing an error


#GLOBAL VARIABLES
def catTwice(part1, part2):
    cat = part1 + part2 + part3
    print_Twice(cat)

part3 = "hello" #Created outside the function, so belongs to the special frame main(), these are
#global because they can be accessed from any function. They do not disappear when the
#function ends - global values persist from one function to the next

catTwice("So", "what")

#Example 3 - Difference Between Global and Local

def ex1():
    local_var = 'bar'
    print(global_var)
    print(local_var)

global_var = 'foo'
ex() #This executes the code inside the func and prints both global_var and local_var
print(global_var) #prints value of global_var
print(local_var) #produces error, since local var is only available inside func
'''
#Example 4 - Functions Inside Functions - Calculating SA and V of a Cylinder

#Three typical functions to deal with the basic calculations required:
def areaRectangle(length, width):
    return length * width

def areaCircle(radius):
    return math.pi * radius**2

def circumference(radius):
    return 2 * math.pi * radius

#This function calls the other three functions since they are used in the calculation of SA
def surfaceAreaCylinder(radius, height):
    return 2 * areaCircle(radius) * areaRectangle(circumference(radius), height)

#Program starts here
radius = int(input("Radius: ")) #applied in all the functions 
height = int(input("Height: "))
SA = surfaceAreaCylinder(radius, height) #surface area compiles all the values into one func 

print("The surface area of the cylinder is", round(SA,2))
