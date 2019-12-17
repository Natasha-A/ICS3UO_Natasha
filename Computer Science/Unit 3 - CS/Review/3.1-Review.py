#Review - #3.1
'''
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
'''
#Exercise 3.1 - Day 3 - For Loops 1, a,b, 4 - c

