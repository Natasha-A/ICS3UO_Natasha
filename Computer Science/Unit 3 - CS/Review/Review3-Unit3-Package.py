#Review - Unit 3 - Review Package

#3 - Table of Values for Function
import random
'''
#a)
for x in range(0,31,3):
    funcTotal = (2 * x) + 5
    print("x =", str(x) + ",", "2x + 5", "=", funcTotal)
    


#4) Entering to add up average 

total = 0
count = 0 
num = 0

while num != "Done":
    for x in range(10):
        num = input("Enter an integer: ") #able to leave input as not an integer, instead use as str to allow for done to be entered 
        count += 1 
        total += int(num)
        average = total/count
    print("The average of these ten numbers is", round(average,2))


#####Modified to be able to count until user enters done#####
total = 0
count = 0
average = 0
go = True

num = input("Enter an integer: ")

while go == True:
    try:
        count += 1
        total += int(num)
        num = input("Enter an integer: ")
        average = int(total/count)
    except:
        go == True
        if num == "Done":
            print(num)
            go == False
            break

print("The average of these numbers is:", round(average, 2))

#5) Printing message

count = 0
userInput = ""
while userInput != "no":
    print("I am so smart")
    count += 1
    userInput = input("Would you like to continue? ")

print("The number of times the line was printed is", count)
'''
#6) - Animal to Food Supply Ratio
animalCount = 10
foodSupply = 1000
hour = 0
while animalCount < foodSupply:
        hour += 1 #increment hours
        animalCount = animalCount * 2 
        foodSupply = foodSupply + 4000
        print("Hour:", hour, "Animals:", animalCount, "Food Supply:", foodSupply)
print("It took", hour, "hours to run out of food!")
        
#7) - Deducting Integers in a Number
eightCounter = 0
product = 1
num = int(input("Enter a positive integer: "))
numEven = 0
numOdd = 0
while num >= 1:
    digit = num % 10
    num = num // 10
    print(digit)

#a) count eights
    if digit == 8:
        eightCounter += 1
    '''
#b) ****product of all digits***
    productOfDigits = previous * digit
    totalProduct += productOfDigits


    previous = digit #NOTE:ASSIGN PREVIOUS AT END AS DIGIT so next loop digit will be previous value 
    
    '''
#b) redone - only need to multiply all together, not previous and new digit and create sum
    product = product * digit

#c)
    if digit % 2 == 0:
        numEven += 1

    else:
        numOdd += 1

print("The total number of 8's is:", eightCounter)
print("The product of the digits is:", product)
print("The total number of even digits is:", numEven)
print("The total number of odd digits is:", numOdd)

#7 - random numbers

numberOne = random.randint(1,20)
numberTwo = random.randint(1,20)
numberThree = random.randint(1,20)
print(numberOne)
print(numberTwo)
print(numberThree)

#a) - exactly two numbers same
if (numberOne == numberTwo and numberOne != numberThree) or (numberOne == numberThree and numberOne != numberThree)\
   or (numberTwo == numberThree and numberTwo != numberOne):
    print("Exactly two of the numbers are the same")

#b) largest number

if numberOne >= numberTwo:
    if numberOne >= numberThree:
        print(numberOne, "is the largest number")
    else:
        print(numberThree, "is the largest number")
elif numberTwo > numberThree:
    print(numberTwo, "is the largest number")
else:
    print(numberThree, "is the largest number")
    
    
#c) even numbers

if numberOne % 2 == 0:
    print(numberOne, "is even")

if numberTwo % 2 == 0:
    print(numberTwo, "is even")

if numberThree % 2 == 0:
    print(numberThree, "is even")
