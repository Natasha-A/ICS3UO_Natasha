#Exercise 5.3 - Searching and Sorting Lists

#1) Using previous functions
import string

'''
#a) store number of threes in list

def getInput():
    while True:
        try:
            n = int(input("Enter the number in the list: ")) #Get integer - input, check for
            #correct data type

            if n >= 0:
                print("*pos. int entered*") #confirm what time of integer is inputted

            if n == -1:
                break
            
            elif n <= 0:
                #print("*neg. int entered*") #see that a negative int was inputted 
                x = 5/0 #forces except*** can use any incorrect operation that forces the program to crash when this negative constraint is met, so that it will go to except and force a
                #postive input instead each time.
                
        except:
            print("Incorrect Input. Please enter a positive integer below.")
        
    return n #returns value if computated (and breaks)

def linearList():
    listOfNum = []
    numOfThrees = 0 
    
    while True:
        try:
            n = int(input("Enter the number in the list: ")) #Get integer - input, check for
            #correct data type

            if n >= 0:
                print("*pos. int entered*") #confirm what time of integer is inputted
                listOfNum.append(n) #adds to list
                print(listOfNum)

            if n == -1:
                break
            
            elif n <= 0:
                #print("*neg. int entered*") #see that a negative int was inputted 
                x = 5/0 #forces except*** can use any incorrect operation that forces the program to crash when this negative constraint is met, so that it will go to except and force a
                #postive input instead each time.

        except:
            print("Incorrect Input. Please enter a positive integer below.")
            print(listOfNum)



    for numIndex in range(len(listOfNum)):
        if listOfNum[numIndex] == 3:
            numOfThrees += 1

    return print("The number of threes in the list are:", numOfThrees)

    return listOfNum


linearList()

#b) determine number of vowels

def vowelList():
    listOfLetters = []
    vowels = ["A", "E", "I", "O", "U"]
    numOfVowels = 0
    alphabet = list(string.ascii_uppercase) #***import string module to extract alphabet list
    userInput = ""
        
    print(alphabet)

    # (?) Best way to interpet is a value is a letter? (Since a number can be interpreted (inferenced) as a string?)
    
    while userInput != "done":
        try:
            userInput = input("Enter the letter in the list: ") #Get integer - input, check for
            #correct data type
            userInput = userInput.lower()
            upperCaseLetter = userInput.upper()

             #Option 1 - use alphabet to see if in list
            if userInput.lower() == "done":
                break
            
            if upperCaseLetter not in alphabet:
                x = 5/0 #force except -- value is not a letter
            else:
                listOfLetters.append(upperCaseLetter) #adds to list, if letter
                print(listOfLetters)


'''
'''
            #Option 2 - determine if number
            if int(letter) > -100000000000000 and int(letter) < 10000000000000000:
                print("****This is a number")

            
            #Option 3 - determine if same type as letter (string) - yet num is interpeted as string ?   
            elif type(letter) == type(isLetter):
                print("This is a letter")
                print(type(letter))
            
           

        except:
            print("Incorrect Input. Please enter a letter.")


    for letterIndex in range(len(listOfLetters)): #length - 0 to 5 (5 cases 
        for vowel in range(len(vowels)):
            if listOfLetters[letterIndex] == vowels[vowel]:
                numOfVowels += 1
                print(listOfLetters[letterIndex])
                

    return print("The number of vowels in the list are:", numOfVowels)

    return listOfLetters

vowelList()
'''

#c) Random lists containing n elements and determine reverseal of each other

def randomList():
    rdmList = []
    num = 1
    
    while num <= 5: 
        try:
            print(num,end=": ")
            rdmNum = int(input("Enter an integer for the list: "))
            rdmList.append(rdmNum) #add num to list 
            
            num += 1 #increase list to contain only 5 elements 
        except:
            print("Please enter an integer.")

    return rdmList


def reversalList():
    firstList = randomList() #instance of first list
    secondList = randomList() #instance of second list

    firstList.reverse() #instance of lists reversed 

    if firstList == secondList:
        print("The lists are reversals of each other.")

    else:
        print("The lists are not reversals.")

#main program
#reversalList()

#d) prices from user, second most expensive item

def getInput():
    priceList = []
    num = 1
    runProgram = True
    
    print("Enter a list of 5 prices, enter -1 to exit the program.")
    while runProgram:
        try:
            n = float(input("Enter a price: ")) #Get integer - input, check for
            #correct data type

            if n == -1:
                runProgram = False  #exit out of loop

            else:
                #number is not -1, check if pos value (if not go to exception)
                assert n >= 0 #check in number is correct value, then can increment nums

                #if true, continue by adding instance to list  
                priceList.append(n)

        except AssertionError: #if negative integer inputted...
            print("Please enter only positive integer.")
        
        except ValueError: #if non-float value inputted....
            print("Please enter only integers.")

    
    return priceList #returns value if computated


def expensive2nd():
    priceList = getInput()
    priceList.sort() #sort list
    priceList.reverse() #reversed to highest to lowest
    
    expensive2nd = priceList[1] #second value, second highest

    print("Second most expensive item in the list:", "$" + str(expensive2nd))

    
#main program
#expensive2nd()

#2) common lists

def randomFiveList():
    rdmList = []
    num = 1
    
    while num <= 5: 
        try:
            print(num,end=": ")
            rdmNum = int(input("Enter an integer for the list: "))
            rdmList.append(rdmNum) #add num to list 
            
            num += 1 #increase list to contain only 5 elements 
        except:
            print("Please enter an integer.")

    return rdmList


def common():
    aList = randomFiveList()
    bList = randomFiveList()

    commonList = []

    for index in range(5):
        if aList[index] == bList[index]:
            commonList.append(aList[index])
            #print(aList[index], "is at the index", bList)

        #else:
            #print(aList[index], "is not at the same index", bList)

    commonList.sort()

    return print(commonList)

#main program
common()

#3) sorting algorithim - find smallest value in a list, and swaps it with the first element.
#locates the next smallest value, and swaps it with the second element and so forth...

def sort():
    listRandom = [5,2,6,4,3,1]
    previous = 10000000

    for x in range(len(listRandom)):
        if listRandom[x] < previous:
            
            


