'''
Name: Natasha Ahammed
Date: November 28 2019 
File Name: Natasha_Ahammed_assign4_triplet.py
Description: Program which takes users inputs and based on input will determine different outcomes, such as pairs, added numbers, consecutive numbers
Test Cases: Try and Except ensures that values are either numbers, different data types tested
'''
def getSet():
    while True:
        try:
            n1 = int(input("Enter the first positive integer: "))
            n2 = int(input("Enter the second positive integer: "))
            n3 = int(input("Enter the third positive integer: "))

            assert n1 >= 0 and n2 >= 0 and n3 >= 0 #test for positive integers

            break

        except AssertionError: #if negative integer inputted...
            print("Please enter only positive integer.")
            
        except ValueError: #if non-int value inputted....
            print("Please enter only integers.")

    return n1, n2, n3

def pairs(n1, n2, n3):

    #two numbers are the same 
    if n1 == n2:
        if n2 != n3:
            return "d"
    elif n2 == n3 or n1 == n3:
            return "d"

    #non of the numbers are the same 
    elif n1 != n2 and n1 != n3:
        return "s"

    #all three of the numbers are the same 
    else: 
        return "t"
    

def add(n1, n2, n3):

    if (n1 + n2 == n3) or (n1 + n3 == n2) or (n2 + n3 == n1):
        return True

    else:
        return False


def order(n1, n2, n3):

    ascendList = []
        
    ascendList.append(n1)
    ascendList.append(n2)
    ascendList.append(n3)

    ascendList.sort() #put list in ascending order

    firstNum = ascendList[0]
    secondNum = ascendList[1]
    thirdNum = ascendList[2]

    return firstNum, secondNum, thirdNum 


def consec(n1, n2, n3):
    #ordered numbers

    n1, n2, n3 = order(n1,n2,n3)
    previous = 2000
    numberChecked = 0
    digit = n1
    consecList = []
    counter = 0

    consecList.append(n1)
    consecList.append(n2)
    consecList.append(n3)

    for x in range(3):
        digit = consecList[x]
        
        if (digit - previous) == 1:
            counter = counter + 1
        else:
            counter = 0
        

        previous = digit
      
    if counter == 2:
            return True #There are three consecutive numbers
            #print("True)

    else:
        return False #There are not three consecutive numbers
        #print("False")
    



###### MENU ###############
def getOption(n1, n2, n3):
    choice = ""
    
    
    while choice != 5:
        print("Welcome to the Program")
        print(" ")
        print("Your options are:")
        print(" ")
        print("1) Check what numbers are", "2) Check for number of pairs", "3) Check if numbers add up to each other", "4) Check consecutive order", "5) Quit Calculator", sep="\n")

        if choice == 1:
            n1, n2, n3  = getInput()

            print("The three numbers you have entered are:", n1, n2, n3)

        #....not enough time to complete menu check 
            

#Main Program (of set input with functions) 
n1, n2, n3 = getSet()

pairs(n1, n2, n3)
add(n1, n2, n3)
order(n1, n2, n3)
consec(n1, n2, n3)






