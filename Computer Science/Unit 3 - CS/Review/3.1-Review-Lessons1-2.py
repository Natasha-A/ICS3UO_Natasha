#Review - #3.1

#3.1 - For Loops 
#e) good example
for posIntegersUnderHundred in range(100,0,-10): #incriments by decreasing by 10, starting at 100
    print(posIntegersUnderHundred) #Goes over 9 times (if end value was -1, would stop at 0

#f) incorporating try and except 
blastOff = True 
while blastOff == True: #if except is run, goes back to while loop 
    try: #if try is not true, and data type is incorrect, goes to except 
        countdownTimer = int(input("Enter time to countdown to: "))
        for countdown in range(countdownTimer,-1,-1): #Have to use -1 to count down to 0 and print statement afterward 
            print(countdown)
        print("Blast off!")
        blastOff = False
    except:
        print("You must enter a number")


#Different values for for loops 
m = int(input("Enter the starting value: "))
n = int(input("Enter the ending value: "))
s = int(input("Enter the step count: "))


for userCount in range(m,n,s):
    print(userCount)


if m < n: 
    for userCount in range(m,n,s):
        print(userCount)
elif m > n:
    for userCount in range(n,m,s):
        print(userCount)
else:
    print("You have entered an incorrect step count")

    


number = int(input("Enter a number to multiply by: "))

for i in range(1,13):
    print(i, "x", number, "=", (i * number))



#For Loops - Day 2 and 3 - Accumlation

for x in range(1,101):
    numberDivisible = x % 17 #Isn't true until x = 17 (eg) 36 remainder of 17 = 36-34 = 2
    #therefore, not true that remainder is 0 
    if numberDivisible == 0: #if remainder is zero, the number can be evenly dividied 
        print(x,end=" ")


#Exercise 1 - Grocery Items and (try Average Grades, E2)
print("\n")
total = 0
costItem = 0
itemsAmount = 0 

groceries = True
while groceries == True:
    try: #checks if a number is used for items, if not, prints execept condition and loops 
        itemsAmount = int(input("Enter the amount of items on your grocery bill: "))
        for x in range(1, (itemsAmount + 1)):
            costItem = float(input("Enter the cost of the item which is:" ))
            total = costItem + total
            print(total)
        if x == (itemsAmount):
            groceries == False
            break
    except:
        print("You must enter a number")
print("The total cost of your groceries is", total)

#Exercise 3.1 - Day 3 - For Loops 1, a,b, 4 - c
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


#b) Fibonanci -- Good practice!
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
