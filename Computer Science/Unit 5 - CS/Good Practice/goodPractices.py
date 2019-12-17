
################5.1 - Exercise day 2###################
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

#Differenates list, instead of y = x, slices from 999
x = [1,2,3]
y = x[:]

y.append(999)

print(x, "  ",y)

'''
########################## 5.2 - exercises ##################
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


\\\\\\IMPORTANT NOTE: use while! instead of loop, stops range from changing//////////////
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
'''
#b) 5.3 - Sorting Lists: Exercise 1 b) - determine number of vowels

def vowelList():
    listOfLetters = []
    vowels = ["A", "E", "I", "O", "U"]
    numOfVowels = 0
    alphabet = list(string.ascii_uppercase) #*** OPTION 1: import string module to extract alphabet list
    userInput = ""
        
    
    while userInput != "done":
        userInput = input("Enter the letter in the list: ") #Get integer - input, check for

        #correct data type
        userInput = userInput.lower()
        upperCaseLetter = userInput.upper()

        
        if userInput.lower() == "done":
            break
        
        '''
        #Option 1 - use alphabet to see if in list
        try:
            
            if upperCaseLetter not in alphabet:
                x = 5/0 #force except -- value is not a letter
            else:
                listOfLetters.append(upperCaseLetter) #adds to list, since letter
                print(listOfLetters)
                
        except:
            print("Incorrect Input. Please enter a letter.")
        '''
        
        
        #Option 2 - check if integer or not****

        try:
            num = int(upperCaseLetter) #if convetable from string to int - value is a integer
            print(num, "is a number. Please enter a letter.")
        except:
            print(upperCaseLetter, "is a letter.")
            listOfLetters.append(upperCaseLetter) #adds to list, since letter
            print(listOfLetters)


    for letterIndex in range(len(listOfLetters)): #length - 0 to 5 (5 cases
        for vowel in range(len(vowels)):
            if listOfLetters[letterIndex] == vowels[vowel]:
                numOfVowels += 1
                print(listOfLetters[letterIndex])
                

    return print("The number of vowels in the list are:", numOfVowels)

    return listOfLetters

vowelList()

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
expensive2nd()
