#5.1 - Append: Day 2 - Exercises
import random

#1) linear list

#a)
def linearList(n):
    listOfNum = []

    for num in range(1,(n+1)):
        listOfNum.append(num) #adds to list 

    return print(listOfNum)

linearList(8)
linearList(20)


#b)

def randomList(n,m,k):
    randomList = []

    # m = random.randint(1,20)

    for x in range(n): #10
        
        randomNum = random.randint(m,k)

        randomList.append(randomNum) #list adds new random number 

    return print(randomList)

randomList(10,3,12)

#c)userList

def userList():
    n = int(input("Enter the number of numbers to create a list: "))
    userNumlist = []
    
    for x in range(1,(n+1)):
        userNumlist.append(x)

    print(userNumlist)

#Main program
userList()


#2 - using program to write functions


#a) read 10 integers

def tenUserList():

    totalList = []

    sumOfNum = 0
    largestNum = 0
    smallestNum = 10000
    numOfEven = 0
    numOfOdd = 0

    for integer in range(0,10):

        userNum = int(input("Enter a number: "))

        totalList.append(userNum)

        sumOfNum += userNum

        average = round((sumOfNum / 10),2)

        if userNum > largestNum:
            largestNum = userNum

        if userNum < smallestNum:
            smallestNum = userNum

        if (userNum % 2) == 0:
            numOfEven += 1
        else:
            numOfOdd += 1 
            
        
    return print("total:", totalList), print("Sum:", sumOfNum), print("Average:", \
         average), print("L:", largestNum), print("S:", smallestNum), print


#Main program 
tenUserList()


#b)**** 5 element list****

def fiveRandomList():
    randomList = []
    descendingOrder = 0

    
    for randomNum in range(0,5):
        randomValue = random.randint(1,5)
        randomList.append(randomValue)

    
    
    for x in range(0,4): #0--4 #only need four checks between 
        if randomList[x] >= randomList[x+1]: #check between 1st-2nd, 2nd-3rd, 3rd-4th, 4th-5th
            descendingOrder += 1
    

    if descendingOrder == 4: #if true, there is a descending order
        print("The numbers are in descending order")
    else:
        print("The numbers are not in descending order")

        
    return print("Random 5 Element List:", randomList)

#main program 
fiveRandomList()


#b)**** REVISED: (able to input any value for checking order) 5 element list****

def anyRandomList(randomValuesGenerated):
    randomList = []
    descendingOrder = 0

    
    for randomNum in range(0,randomValuesGenerated):
        randomValue = random.randint(1,5)
        randomList.append(randomValue)
    
    
    for x in range(0,(randomValuesGenerated - 1)): #0--4 #only need four checks between 
        if randomList[x] >= randomList[x+1]: #check between 1st-2nd, 2nd-3rd, 3rd-4th, 4th-5th
            descendingOrder += 1
    

    if descendingOrder == (randomValuesGenerated - 1):
        print("The numbers are in descending order")
    else:
        print("The numbers are not in descending order")

        
    return print("Random 5 Element List:", randomList)


#main program    
anyRandomList(10)


#c)

def twoList():
    n = int(input("Enter the length of the first list: "))
    m = int(input("Enter the length of the second list: "))
    listOne = []
    listTwo = []

    for num in range(1,(n+1)):
        listOne.append(num)

    for num in range(1, (m+1)):
        listTwo.append(num)

    sumOfLists = listOne + listTwo

    return print("The lists combined creates:", sumOfLists)

#main program
twoList()

    
        
        


        

