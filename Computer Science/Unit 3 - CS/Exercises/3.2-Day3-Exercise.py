#Exercise 3.2 - Day 3 - Conditional Loops
'''
#******Exercise 1 - user name and password******
userNameOne = "username"
passWordOne = "password"
enterUserName = ""
enterPassWord = ""

userNameTwo = "usernametwo"
passWordTwo = "passwordtwo"

maxAttempts = 3
attemptsMade = 0

chooseUser = str(input("Please print if you are either 'UserOne' or 'UserTwo': ")).lower()

while attemptsMade < maxAttempts:
    if chooseUser == "userone":
        while enterUserName != userNameOne and enterPassWord != passWordOne:
            enterUserName = str(input("Enter your username: "))
            enterPassWord = str(input("Enter your password: "))
            if enterUserName != userNameOne and enterPassWord != passWordOne:
                attemptsMade += 1

                if attemptsMade == maxAttempts:
                    print("You have attempted too many times.")
                else:
                    print("User One: Either your username or password is incorrect, try again.")
                break
            
            if enterUserName == userNameOne and enterPassWord == passWordOne:
                print("User One has successfully entered the system.")
                break
            
    elif chooseUser == "usertwo":
         while enterUserName != userNameTwo and enterPassWord != passWordTwo:
            enterUserName = str(input("Enter your username: "))
            enterPassWord = str(input("Enter your password: "))
            if enterUserName != userNameTwo and enterPassWord != passWordTwo:
                attemptsMade += 1

                if attemptsMade ==  maxAttempts:
                    print("You have attempted too many times.")
                else:
                    print("User Two: Either your username or password is incorrect, try again.")
                break
            
            if enterUserName == userNameTwo and enterPassWord == passWordTwo:
                print("User Two has successfully entered the system.")
                break
    else:
        print("You have entered the incorrect user choice.")
        break

#*********Exercise 2 - Collatz Conjecture**********

while True:
    number = int(input("Enter a natural number (positive integer): ")) #4
    evenNumber = number % 2 
    newNum = number #4
    counter = 0 

    if evenNumber == 0: #true
        while newNum != 1: #true
            newNum = newNum / 2 #2
            print("The new even number is =", int(newNum))
            counter += 1
    else:
        while newNum != 1:
            newNum = (newNum * 3) + 1
            print("The new odd number is =", int(newNum))
            counter += 1
            
    if newNum == 1:
        print("The amount of times for the number to reach 1 is:", counter)

    
#******Exercise 3 - analyzing numbers using modulus ******* PP

#Extracts each digit from the end:

#'''''''''''''''''''''''''''''''''''''#
num = int(input("Enter a positive integer: "))

while num >= 1: #only takes values from 0 up 
    digit = num % 10 #Extracts value from tens column - left with ones column remainder /
    #eg) 223 - goes into 10, 23 times. 223 - 220 = 3 
    num = num // 10 #then takes orignal number 223 divides by 10 evenly (so 220 / 10 = 22) = 22, continues process
    print(digit)

#'''''''''''''''''''''''''''''''''''''#
   

#a) *******number of sevens in a integer*********
num = int(input("1: Enter a positive integer to look for number of sevens: "))
sevenCounter = 0

while num >= 1:
    digit = num % 10 
    num = num // 10
    print(digit)
    if digit == 7:
        sevenCounter += 1
print("The amount of sevens in the number are:", sevenCounter)
    

#b) ********count odd digits, even digits, in a integer********
integer = int(input("2: Enter a postive integer to count number of even and odd numbers: "))
positiveInts = 0
negativeInts = 0

while integer >= 1:
    digit = integer % 10
    integer = integer // 10
    print(digit)
    evenNumber = digit % 2
    if evenNumber == 0:
        positiveInts += 1

    else:
        negativeInts += 1

print("The number of positive digits are:", positiveInts)
print("The number of negative digits are:", negativeInts)


#c) *** sum of positive integers ***
previous = 0
newNum = 0

number = int(input("3: Enter a positive number: "))
while number >= 1:
    digit = number % 10
    number = number // 10
    newNum = digit + previous #extracts each digit, adding the previous digit/sum of previous digits to the new digit
    previous = newNum 
print("The sum of the digits are:", newNum)


#d)*******integer containing three consecutive digits that are consecutive integers /
#in ascending order ********** PP

while True:
    num = int(input("4: Enter a positive intege to check for the consecutive ints: "))
    #Example: 345 - able to work for ascending consective integers ( minus 1 to check) 
    previous = 2000 #assign any value that will not be true the first run 
    while num >= 1:
        digit = num % 10
        num = num // 10
        print(digit)

# to check if numbers are consecutive in ascending order ie) 345
        if (previous - digit) == 1:
            counter = counter + 1 #If the difference is 1, the numbers are consecutive, start counting the amount of consecutive number
        else:
            counter = 0 #resets counter, starts all over again in order to check for consective numbers

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
'''


        
