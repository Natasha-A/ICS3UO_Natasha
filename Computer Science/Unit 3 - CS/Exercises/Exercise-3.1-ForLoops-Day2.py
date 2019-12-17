#Exercise 3.1 - Day 2 - For Loops
'''
#Exercise 1 - Grocery Items - ***
itemsAmount = int(input("Enter the amount of items on grocery bill: "))

total = 0 #always set constant
#for x in range(itemsAmount): 
for x in range(1,(itemsAmount + 1)):
    cost = float(input("Enter the cost of each of the items: "))
    total = cost + total #takes old total, adds new cost to it, creates new total
    print(total) #check what total is, if adding up properly

print("The total cost is", "$", total)


#**** Exercise - Averages ****
#Accumulating Values - examples: adding student grades, cash register total
total = 0
listOfMarks = []

marksAmount = int(input("Enter the number of marks: "))
for i in range (marksAmount):
    mark = int(input("Enter the mark: "))
    if mark >= 0 and mark <= 100:
        total += mark
        average = (total/marksAmount)
        #In order to determine highest and lowest marks, add to list mark, and print out below the highest and lowest 
        listOfMarks.append(mark)
    
    else:
        print("You entered a mark that is not between 0 and 100.")
        total -= mark 
print(average)
#Prints out the highest and lowest marks of the list, using predefined functions - mark and min 
print("Highest mark in the list is :", max(listOfMarks),"\nLowest mark in the list is :", min(listOfMarks))

'''
#Startegy 2: Or make use of a number less than the max maximum value
total = 0
marksAmount = int(input("Enter the number of marks: "))
oldSmallerNumber = -1
for i in range (marksAmount):
    mark = int(input("Enter the mark: "))
    if mark >= 0 and mark <= 100:
        total += mark
        average = (total/marksAmount)
        #In order to determine highest and lowest marks, add to list mark, and print out below the highest and lowest 
        if mark > oldSmallerNumber:
            oldSmallerNumber = mark 
            print("Old smaller:",oldSmallerNumber)
        elif mark < oldSmallerNumber:
            smallerNumber = mark
            print("Smaller:", smallerNumber)
    else:
        print("You entered a mark that is not between 0 and 100.")
        total -= mark
print("The average is,", average)
print("The largest number is,", oldSmallerNumber)
print("The smallest number is,", smallerNumber)


