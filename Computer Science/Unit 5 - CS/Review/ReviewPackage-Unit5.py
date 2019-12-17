#Review Package - Unit 5 Exercises

#1) create a list of 100 zeros

hundredList = [0] * 100
print(hundredList)

#2) First and last values of list

aList = [55 , 41, 52, 68, 45, 27, 40, 25, 37, 26]

lengthOfList = len(aList)

lastNum = aList[lengthOfList - 1]
firstNum = aList[0]

print("First value:", firstNum)
print("Second value:", lastNum)

#3) Swap values

def swapList(userList):
    alist = userList
    
    first, second = aList[1], aList[0] #SWAPS VALUES - first = 41, #second = 55
 
    newAList = aList[2:] #creates a copy of the list, NOT including first two values (all the way to end)

    newAList.insert(0, first)
    newAList.insert(1, second)

    print("The new list with the swapped values:\n" + str(newAList))

aList = [55,41, 52, 68, 45, 27, 40, 25, 37, 26]

swapList(aList)

#4) Print each elemet of list

def printList(aList):
    elements = aList
    
    for num in elements:
        print(num, sep="\n")

#NOTES
'''
outputList = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]

printList(outputList)
        
print(outputList.sort()) #returns none, since value is computated by no result is stored to print

#instead call method, THEN print:

outputList.sort()

#print(outputList) #modified list

methodSort = outputList.sort()
print(methodSort)#doesn't work - value is not passed, since OBJECT is modified
print(outputList) #works since the object has been modified and can now be printed 

functionList = sorted(outputList)

print(functionList) #works, since function takes list, modified, and then returns value 

#or store as variable
'''

#5) Returns list of numbers that are even

def evenList(aList):
    numList = aList
    evenNums = []

    for num in range(len(numList)):
        if numList[num] % 2 == 0:
            evenNums.append(numList[num])

    print("The even numbers in the list are:", evenNums)

aList = [5,3,5,-2,6,7,8]

evenList(aList)

#6) Find errors in code

def count_numbers(list, key): #(1) shouldn't be using list keyword (type) as a variable.
    #countList = alist need to declare countList
    count = 0
    for i in range(len(list)): #(3) need to use 'len' for range
        if list[i] == key: #(2)need to index value of elements in list
            count += 1

    return count
    
    
my_list = [3,4,32,4,2,4,5,5,4,3,4,2,43,56,43,2,4]

c = count_numbers(my_list,2) #(4)calling instance of function, returns none

count = c #can assign return statement as value. 

print(count) #need to assign count 

