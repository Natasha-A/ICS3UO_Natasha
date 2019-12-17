#Unit 2 Review - Exercise 4 - INTEGER VALUES

#Good to practice!***
number = int(input("Please enter an integer: "))
#A)
numberRemainder = number % 2 #if remainder is zero, the number is even, if the remainder, 1, the number is odd.

if numberRemainder == 1:
    print("The number is odd.")
elif numberRemainder == 0:
    print("The number is even.")
else:
    print("Incorrect number inputted.")

numDivideFour = number % 4
numDivideNine = number % 9

#B,C,D) Divisible by 4, 9, 0
if number > 0:
    if numDivideFour == 0 or numDivideNine == 0:
        if numDivideFour == 0 and numDivideNine == 0:
            print("The number can be divided by 4 and 9")
        elif numDivideFour == 0:
            print("The number can be divided by four.")
        elif numDivideFour != 0:
            print("The number cannot be divided by four.")
        elif numDivideFour != 0 and numDivideNine != 0:
            print("The number cannot be divided by 4 and 9")
else:
    print("The number is not a positive integer")

print("\n")

#E) Largest of two integers
firstInteger = int(input("Enter the first integer: "))
secondInteger = int(input("Enter the second integer: "))

if firstInteger > secondInteger:
    print("The first integer is larger than the second integer.")
elif firstInteger == secondInteger:
    print("They are the same integers.")
elif secondInteger > firstInteger:
    print("The second integer is larger than the first integer.")

#F) Enter three digits:

print("\n")

firstInt = int(input("Enter the first integer once more: "))
secondInt = int(input("Enter the second integer once more: "))
thirdInt = int(input("Enter the third integer once more: "))

#Good to practice!***
if firstInt >= secondInt and firstInt >= thirdInt: #firstInt is the biggest
        print("The first number is the largest.") 
elif secondInt > thirdInt:#firstInt isn't the biggest, check if secondInt is
        print("The second number is the largest.")
else: #firstInt and secondInt isn't biggest, thirdInt then has to be
    print("The third is the largest.")
     
     
    
    
