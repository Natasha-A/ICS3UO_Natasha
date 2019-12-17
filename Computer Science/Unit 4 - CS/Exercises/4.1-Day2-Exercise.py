#4.1 - Day 2 - Introduction
import math
#Exercise 1 - Days of the Week

def dayWeek(num):
    if num >= 1 and num <= 7:
        if num == 1:
            print("Monday")
        elif num == 2:
            print("Tuesday")
        elif num == 3:
            print("Wednesday")
        elif num == 4:
            print("Thursday")
        elif num == 5:
            print("Friday")
        elif num == 6:
            print("Saturday")
        elif num == 7:
            print("Sunday")
    else:
        print("Error - Enter an integer between 1 and 7")

#main program - *try to always use comment for main program at end 
dayWeek(1)
dayWeek(7)
dayWeek(3)
dayWeek(10)
dayWeek(0)
dayWeek(-1)

#Exercise 2 - Calculate sum of first integers

def sumFirst(n):
    newSum = 0 
    for x in range(n+1):
        newSum += x

    print("The sum is:", newSum)

#main program 
sumFirst(0)
sumFirst(1) 
sumFirst(5) #15
sumFirst(10)
sumFirst(50)


#***Exercise 3 - REVISED - Calculate sum of odd numbers***
def sumFirstOdd(amountOfNum):
    n = 1
    oddSum = 0
    count = 0 
    while (n % 2) != 0:
        oddSum = oddSum + n
        n = n + 2 #increment to next uneven number - 3 
        count += 1


        if count >= amountOfNum: #compare to print out when the count is the same amount of numbers inputted into parameter to print out (ie. 3) 
            print("The odd sum is", oddSum)
            break

sumFirstOdd(3)
sumFirstOdd(5) 
sumFirstOdd(20)

    
#Exercise 4 - Swapping Values
print("\n")
def swap(a,b):
    newA = b
    newB = a

    print(newA)
    print(newB)

swap(3,5)
swap("Boo","Hoo")

#Exercise 5 - Area

def area(a, b, c,):
    area = (a+b+c)/2 #Heron's formula
    print("The area of the triangle is", int(area))
    
area(3,4,5)

#Exercise 6 - Angles (opposite side in a triangle)

def angle(a,b,c):
    sideAAngle = ((b**2) + (c**2) - (a**2)) / (2 * b * c)
    newAAngle = math.acos(sideAAngle) 
    newAAngle = (newAAngle * 180) / math.pi #convert to degrees from radians 
    
    print("The angle of side A is", round(newAAngle), "degrees")

angle(3,4,5)


