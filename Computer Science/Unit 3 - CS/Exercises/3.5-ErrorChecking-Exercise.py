#3.5 - Error Checking - Exercises **** PP

'''
Error Checking ** Save All Programs in Appropriate Folder **
Day 1: Write a program that calculates the sum of the first n integers.
 Make sure your program does two error checks:
1) checks datatype of input
2) checks that the integer entered is &gt; 0
 Your program should loop until the user enters an appropriate number
Sample Program Interaction:
This program will add up all the numbers from 1 until the number you enter.
Enter number: dog
Invalid input! Please enter a positive integer greater than 0!
Enter number: 10
The sum of the first 10 integers is 55.

Day 2: Finish slide 20/21 – Average Temperature and Average Marks
'''
while True: #Even though answer may break, overall while True continues to run program
    print("\n")
    #**** practice ****
    previous = 0
    sumOfNum = 0
    num = 1
    try: 
        num = int(input("Enter the amount of numbers you would like to calculate the sum of: "))
        while num > 0: 
            for count in range(1, (num + 1)):
                #print(count)
                sumOfNum += count
            print("The sum of the first", num, "digits are", sumOfNum)
            break
    except:
        print("You need to enter a number!") 

    print("\n")

    #Exercise 2: Average of Marks

    print("Enter '-1' if you wish to exit the program: ")
    mark = 1
    average = 0
    numberOfMarks = 0
    average = 0
    total = 0

    
    try:
        while mark != 0:
            mark = int(input("Enter a mark: "))
            numberOfMarks += 1
            total += mark
            average = total / numberOfMarks
            if mark == -1:
                break
            
    except:
        print("You must enter a number!")

    if average > 0:
        print("The average of the marks is,", average)

    print("\n")

    #Exercise 3: Average Temperatures
    temperature = 0
    tempTotal = 0
    tempAverage = 0
    numberOfTemp = 0 

    print("Enter 'done' if you wish to exit the program")
    while True:
        try: #as long as integers are inputted, temperature will be calculated
            numberOfTemp += 1
            temperature = int(input("Enter the temperature: "))
            tempTotal += temperature
            tempAverage = tempTotal / numberOfTemp
        except:
            if temperature == "done":
                break #once a character, such as "done" is inputted, the program will break and results will be displayed

            print("Enter a number!")
    print("The average temperature is", tempAverage)

 

            
