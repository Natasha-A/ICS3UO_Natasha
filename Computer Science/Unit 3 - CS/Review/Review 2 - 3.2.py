#Review 2 - 3.2 While Loops
'''
#Correct math problem

userMathA = 0
while not userMathA == 8: #while condition is not met as true..
    try:
        userMathA = int(input("What is the square root of 64? ")) #ask question
        if not userMathA == 8: #if any number but answer of 8...
            print("You have entered the incorrect answer, try again.")
    except: #if they have failed to enter a number... (continues back up to while loop
        print("Please enter a number")
print("You have entered the correct answer of 8.") #if enters 8, breaks while loop since now userMathA == 8


    
#Exercise 4 - user enters word to amounts and can change termination key word

terminateWord = ""
newTerminateWord = str(input("Enter a word that will terminate the program: "))


while terminateWord != newTerminateWord:
    word = str(input("Enter a word to display: "))
    numberDisplay = int(input("Enter the amount of times to display the word: "))
    print((word*numberDisplay),sep=" ")
    terminateWord = str(input("Enter the terminate word to end the program: "))


#Exercise 3 - largest of n positive integers (?)
amount = 1
number = 0
smallNum = 0
largeNum = 0
secondLarge = 0
previous = 0

numbers = int(input("Enter the amount of numbers to determine the largest of them: "))
while amount <= numbers:
    amount += 1
    number = int(input("Enter a number: "))
    previous = number
    if number > largeNum:
        largeNum = previous
        print("The largest number is:", largeNum)

    if number < largeNum:
        secondLarge = previous #second largest is a small number than largest, 
        print("A smaller number is:", secondLarge)
    
    if secondLarge > number: #now comparing second largest against rest of the numbers to see if there are other numbers that are the second largest 
        print("The second largest is,", secondLarge)

    
print("TOTAL \n")

print("The largest number is:", largeNum)
print("The second largest is:", secondLarge)
   

#c) sum of positive integers***

previous = 0
newNum = 0
go = True
number = 0

while go == True:
    try:
        number = int(input("Enter a positive number: "))
        while number >= 1:
            digit = number % 10
            number = number // 10
            newNum = digit + previous
            previous = newNum

        print("The sum of the digits are:", newNum)
        previous = 0 #resets to zero to recount new numbers 

    except:
        print("A number was not entered")
        go == True

#d) looking for the longest consecutive
'''
while True:
    num = int(input("Enter a positive integer: "))
    previous = 2000 #assign any value that will not be true the first run
    while num >= 1:
        digit = num % 10
        num = num // 10
        print(digit)

#to check if numbers are consecutive in ascending order ie) 345
        if (previous - digit) == 1:
            counter += 1 #If there is a difference of 1, the numbers are consecutive

        else:
            counter = 0 #resets counter, since not consecutive

        if counter == 2: #was able to find consecutive between 2 changes, 3 integers ie) 5 - 4 = 1, 4 - 3 = 1
            print("There are three ascending consecutive integers.")

# to check if numbers are consecutive in descending order ie) 543
        if (previous - digit) == -1:
            descendingCounter += 1
        else:
            descendingCounter = 0

        if descendingCounter == 2:
            print("There are three descending consecutive integers.")

        previous = digit #assign previous right at the end, providing new digit





        










