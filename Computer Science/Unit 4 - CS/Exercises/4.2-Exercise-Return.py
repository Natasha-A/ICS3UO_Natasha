#4.2 - Exercise - Returning a Value
import math

#Exercise 1 - Area of a circle

def circleA(r):
    area = (math.pi) * (r ** 2)
    
    return area #computates area

area1 = circleA(1) #assigns area to each instance - 1, and 5
area2 = circleA(5)

print(round(area1,2), round(area2,2)) #prints out area rounded

#Exercise 2 - surface area of a cylinder

def cylinderSA(height, radius):
    #computate cylinder
    areaCircle = 2 * (math.pi * (radius ** 2))
    circum = math.pi * (2 * radius)
    sideArea = circum * height 
    surfaceArea = areaCircle + sideArea

    return surfaceArea 

#main program 
cyclSAOne = cylinderSA(4,10) #input different values 
cyclSATwo = cylinderSA(1,1)

print("Cylinder Surface Area One:", round(cyclSAOne, 2))
print("Cylinder Surface Area Two:", round(cyclSATwo,2))


#Exercise 3 - Volume of rectangular prism
def rectangleV(length, width, height):
    volume = length * width * height

    return volume

volumeOne = rectangleV(4,5,10)

print("The volume of the rectangular prism is", round(volumeOne,2))

#Exercise 4 - Time of object
def findTime(v,h): #y = ax2 + bx + c equation: -4.9^2 +vt +h = 0.
    xOne = 0
    xTwo = 0
    try:
        divideBy = 2 * (-1 * 4.9) #or can do -4.9
        squareRoot = math.sqrt((v**2) - (4 * (-1 * 4.9) * h))
        xOne = ((-1 * v) + squareRoot) / divideBy
        xTwo = ((-1 * v) - squareRoot) / divideBy
    except:
        print("The numbers are imaginary")

    # time = xTwo
    
    if xOne >= 0 or xTwo >= 0:
        if xOne >= xTwo:
            time = xOne
        elif xTwo >= xOne:
            time = xTwo
        elif xOne == xTwo:
            time = xOne
    else:
        print("The time is an imaginary number.")

    return time

timeInstance = findTime(10, 1)
print("The ball reaches the ground at", round(timeInstance,2), "seconds.")

