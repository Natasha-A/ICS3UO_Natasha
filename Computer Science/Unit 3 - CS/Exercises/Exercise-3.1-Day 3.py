#Exercise 3.1 - Day 3 - For Loops
while True:
    #*** Exercise 1 *** PP
    #a)
    countFactors = 0
    prime = False
    integer = int(input("Enter a number between 1 and 50: "))
    for i in range(1,50):
        integerFactored = integer % i
        if integerFactored == 0: #Just trying to see remainder of integer as 0
                print(integer, "can be factored by", i)
                prime = False
                countFactors += 1
    if countFactors <= 2: #If the number can only be factored by two numbers ie) itself and 1, the number is a prime number
        prime = True
    #b)
    if prime == True:
        print(integer,"is a prime number.")
    elif prime == False:
        print(integer, "is not a prime number.")
            
    #**** Exercise 2 - Fibonanci *** PP
    previous = 0
    sumOfNum = 1
    newNum = 0 

    numbersInFib = int(input("Enter the amount of numbers of the sequence of Fibonacci to output: "))
    
    #in order to avoid duplicate of each number, divide by two
    numbersInFibRemainder = numbersInFib / 2 #check to see if number is even or not
    if (numbersInFib % 2) != 0:
        print(sumOfNum) #if not even, can print extra number to add to proper numbersInFib amount 
    
    numbersInFib = numbersInFib // 2 #since printing twice, only need half expected numbers 
    for amount in range(int(numbersInFib)):
        newNum = previous + sumOfNum
        previous += sumOfNum #two seperate sequencial fib caluations taking place at once, same results, one stores as the previous number, while the other stores as next number 
        print(newNum)
        sumOfNum = previous + sumOfNum #creates next following fib number by add previous two nums
        print(sumOfNum) 


    #***Exercise 3 - Understanding***
    for num in range(1,5):
        print("#"*num) # * operater can print a string multiple times

    for num in range(3,0,-1):
        print("#"*num)


    #***Exercise 4 - String Loops*** PP
    #a)
    for fiftyLines in range(1,51): #ends at 50, one short
        print("*"*fiftyLines)
    #b)
    length = int(input("Enter the length of the rectange: "))
    height = int(input("Enter the height of the rectangle: "))
    for solidRectangle in range(height):
        print("*"*length)
    print("\n")
    #c)
    for hollowRectangle in range(1,height):
        if hollowRectangle == 1:
            print("*"*length)
        if not (hollowRectangle == 1) or (hollowRectangle == height):
            print("*","*",sep=(" "*(length - 2)))
        if hollowRectangle == (height - 1):
            print("*"*length)
        
    

