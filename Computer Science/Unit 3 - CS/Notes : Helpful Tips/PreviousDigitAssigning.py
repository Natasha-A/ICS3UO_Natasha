#assigning previous value - cheat sheet

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
