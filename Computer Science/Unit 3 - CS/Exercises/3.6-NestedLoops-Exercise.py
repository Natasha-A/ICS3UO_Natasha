#3.6 - Nested Loops - Exercises
#Exercise 1 - Triangle Row 

numberOfRows = 7

for i in range(0, numberOfRows):
    print((" " * (numberOfRows - i)) + "#", end="")
    for j in range(1, (i+1)):
        print("**", end="")

    print("\n")
    

#Exercise 2 - Drawing Patterns ***
#a) *easy
numberOfRows = 5
numberOfCol = 5

for y in range(0,numberOfRows):
    print("+" * numberOfCol, end="\n")
    for printThree in range(0,3):
            print("-" * numberOfCol, end="\n")

#b)*medium challenge  

initalStars  = 5 
for line in range(0,initalStars):
    print("*", end="") #print out vertical line of * as base to add more * to 
    if line >= 1 and line <= 2: 
        for addedStar in range(1, line + 1): #for the second and third lines, add **, the third line being in range of 3 (2 iterations)
            #so adding **, and then looped again with **, thus equalling 4 ****'s
            print("**", end="")
    if line == 3: #once at three, jumps back to one iteration of **
        print("**")
    print("\n")

#c) *hard challenge - most likely to be given code and try to solve output 
#use spacing from example one

print("\n\n")
numTriangles = 2

for totalTriangles in range(0,3):
    for i in range(0, numTriangles):
        print(" " * (numTriangles - i), end="")
        print("*", end="")
        for j in range(1, i + 1):
            print("**", end="")

        print("\n")

#Exercise 3 - rolling dies

#Example:combinations of two die combining to rolling 8 or less 
total = 0

for die1 in range(1,7): #takes all of the first dice's rolls (1,1,1,1,1,1 and matches with second dices (1,2,3,4,5,6), repeating with the digitis growing for the first die 
    for die2 in range(1,7):
        if die1 + die2 <= 8:
            total += 1
            print(die1, die2)
print("There are", total, "possible rolls that sum to 8 or less.")
       

#a.i) - greater than 9 possibilites
totalNine = 0
for die1 in range(1,7):
    for die2 in range(1,7):
        if die1 + die2 >= 9:
            totalNine += 1
            print(die1, die2)
print("There are", totalNine, "possible rolls that sum to 9 or greater.")
divideCount = 0 
#a.ii) - not divisble by 3 or 5
for die1 in range(1,7):
    for die2 in range(1,7):
        total = die1 + die2 #Takes the sum of each die face add together 
        if total % 5 == 0 or total % 3 == 0: #determines which can be divided in order to evenly
            #do so in 5 and 3
            divideCount += 1

print("There are", divideCount, "possible rolls that are divisible by 4 or 5.")

totalTwelve = 0
#b.i) sum of three die - less than 12
try:
    for die1 in range(1,7):
        for die2 in range(1,7):
            for die3 in range(1,7):
                if (die1 + die2 + die3) < 12:
                    totalTwelve += 1
    print("There are", totalTwelve, "possible rolls that sum to less than 12.")
except:
    print("Issue with inputs")

#b.ii) between 7 and 11 
totalBetween = 1
for die1 in range(1,7):
        for die2 in range(1,7):
            for die3 in range(1,7):
                if (die1 + die2 + die3) >= 7 and (die1 + die2 + die3) <= 11:
                    totalBetween +=1
print("There are", totalBetween, "possible rolls that sum between 7 and 11.")

primeCount = 0
#c.iii) prime number
for die1 in range(1,7):
        for die2 in range(1,7):
            for die3 in range(1,7):
                totalSum = die1 + die2 + die3
                if (totalSum % 2) != 0 and (totalSum % 3) != 0: #remainder from dividing by 2 should be zero, otherwise, prime 
                    primeCount += 1 #2 used to divide against potential even numbers, 3 used for numbers like 9 
                    print(totalSum) 
print("There are", primeCount, "possible rolls that sum as a prime number.")



