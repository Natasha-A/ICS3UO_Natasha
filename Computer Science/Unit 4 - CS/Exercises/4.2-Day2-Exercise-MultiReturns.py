#4.2 - Day 2 - Exercise - Multiple Return Values

import math

    #1) Get Names

while True:
    def getNames():
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        
        return print(firstName + "," + lastName) #computates firstName and lastName 

    getNames()

    #2) Take Quotients

    def quot_rem(num1, num2):
        try:
            divide = num1 // num2
            quotient = num1 % num2

            total = print("Quotient:", divide, "Remainder:", quotient)

            return total 

        except:
            print("Error - cannot divide numbers")


    quot_rem(7,2)
    quot_rem(18,5)
    quot_rem(72,12)
    quot_rem(0,12)
    quot_rem(3,8)
    quot_rem(3,0)

    #3) Roots - Quad Equation

    def roots(a,b,c): #y = ax^2 + bx + c
        xOne = 0
        xTwo = 0
        try:
            divideBy = 2 * a 
            squareRoot = math.sqrt((b**2) - (4 * a * c))
            xOne = ((-1 * b) + squareRoot) / divideBy
            xTwo = ((-1 * b) - squareRoot) / divideBy

            print("The roots are:", round(xOne, 2), "and", round(xTwo, 2))
        except:
            print("The numbers are imaginary")


    roots(1,-4, 4)
    roots(1, 3, -5)
    roots(1,1,1)



    

 
