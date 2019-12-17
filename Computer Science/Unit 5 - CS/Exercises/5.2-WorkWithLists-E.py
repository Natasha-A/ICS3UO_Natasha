#5.2 - Exericises - Working with Lists
import random
'''
#1) - (a) names list

def nameList(numNamesToAdd):
    namesList = ["Anna", "Rachel", "Sam", "Troy", "Alex"]

    for name in range(numNamesToAdd):
        try:
            namesToAdd = input("Enter a name you would like to add: ")
            namesList.append(namesToAdd)
        except:
            print("Incorrect input")

    for names in range(len(namesList)): #print names in one list
        print(namesList[names], end=", ")

numNamesToAdd = int(input("Enter the number of names you want to add: "))

#main program
nameList(numNamesToAdd)

#1) - (b) dice

diceRoll = 0 
diceValues = []
total = 0 

while diceRoll != 6:
    diceRoll = random.randint(1,6)
    diceValues.append(diceRoll)

for diceIndex in range(len(diceValues)):
    total += diceValues[diceIndex]

average = round((total / len(diceValues)),2)

print("")
print("The average is", average)

#2) - a: solve tasks using yesterday's functions


def getTestInput():
    while True:
        try:
            n = int(input("Enter the number of number of a list: ")) #Get integer - input, check for
            #correct data type

            if n >= 0:
                #print("*pos. int entered*") #confirm what time of integer is inputted
                break

            if n <= 0:
                #print("*neg. int entered*") #see that a negative int was inputted 
                x = 5/0 #forces except*** can use any incorrect operation that forces the program to crash when this negative constraint is met, so that it will go to except and force a
                #postive input instead each time.
                
        except:
            print("Incorrect Input. Please enter a positive integer below.")
        
    return n #returns value if computated (and breaks)

def linearList():
    n = getTestInput()
    listOfNum = []

    for num in range(1,(n+1)):
        listOfNum.append(num) #adds to list
        listOfNum.append(0)

    return print(listOfNum)

linearList()

#2 - b)largest three numbers

def largestThree():
    highest = -10000000000
    highest2nd = -100000
    highest3rd = -1000
    
    n = getTestInput()
    numList = []

    for x in range(1, (n+1)):
        numList.append(x) #create list from lowest to highest


    numList.reverse()#reverse list from highest to lowest 
    
    for num in range(len(numList)):
        newNum = numList[num]
        #print(newNum) #print out reversed list

    highest = numList[0]
    secondHighest = numList[1]
    thirdHighest = numList[2]


    return print("Highest:", highest), print("Second highest:", secondHighest), print("Third highest:", thirdHighest)
        
        
largestThree() 

'''
#3)*****read user values and computate different information*****

def removeFromList():
    numList = []
    
    while True:
        try: #if not an integer... cannot add to list
            n = int(input("Enter a number for the list: ")) #Get integer - input, check for
            #correct data type
            
            if n != -1:
                #print("*pos. int entered*") #confirm what time of integer is inputted
                numList.append(n)
                print("length of list:", len(numList)) #eg) [4,8,12,9,7]
                print("")
                
            else: #if they no longer need to store values, computate results with what
                #has been given
                numIndexValue = 0

                while numIndexValue < len(numList): #**make sure to use len - check if the value
                    #of numbers is less than list length

                    currentNum = numList[numIndexValue] #create instance for each num
                    #in the list

                    if (currentNum % 3) == 0 or (currentNum % 4) == 0: #check if multiple of it
                        del(numList[numIndexValue]) #delete the value 
                        numIndexValue = numIndexValue - 1 #***NOW INDEX OF LIST changes, thus
                        #need to reduce index by 1, so that new index will have new index positions
                        #which are correct to the senario 
                        print("number IS a multiple 3/4:", currentNum)

                    else:
                        print("number not multiple 3/4:", currentNum)

                    if len(numList) % 5 == 0:
                        print("**The list length is a multiple of 5.**")
                    

                    numIndexValue = numIndexValue + 1 #increase the index by 1, so that it will reach until
                    #the length of the list

                print("The new list is:", numList)

        except:
            print("Incorrect input. Please enter a number.")
            

#main program              
removeFromList()



    
    
    

    


    
        
