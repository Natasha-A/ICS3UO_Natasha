#3.6 - Nested Loops - Lesson

#Review - have studied counted loops using for statement
for i in range(10):
    print("Math is awesome")

#Example 1
for i in range(1,4): #prints for the amount of times of i - 3 times
    for j in range (1, 4): # prints for the amount times in j  - 3 times 
        print(i * j) #prints total for each changes

#Example 2
#Output numbers from 1 - 10 (numerically and graphically (using character of choice)

#Print the number
for i in range(1,11):
    print(i, end=" ") #prints out key value of what the iteration of i is at each loop (ends with a space between next_string)

    #print the right number of stars
    for j in range(i): #uses based on the amount of i, when i = 2, print 2 **
        print("*", end="")

    print("\n") #key is to have this to have new line

    
#Program enhanced
symbol = input("What symbol would you like to use? ")
low = int(input("Enter the number to start at: "))
high = int(input("Ehter the number to end at: "))

#Print the number
for i in range(low, high+1): #to get to correct number
    print(i, end=" ")

    #Print the symbols
    for j in range(i):
        print(symbol, end="")

    print("\n")


#Example 3
count = 0
for die1 in range(1,7):
    for die2 in range(1,7):
        total = die1 + die2
        if total < 8:
            count += 1

print("1: There are", count, "possible rolls that sum to 8 or less.")

#Modify the program - previous program to count all the combinations that are divisible by 4 or 5
count = 0

for die1 in range(1,7): #takes range from first die
    for die2 in range(1,7): #takes range from second die 
        total = die1 + die2
        if total % 5 == 0 or total % 4 == 0:
            count += 1

print("2: There are", count, "possible rolls that are divisible by 4 or 5.")


    
