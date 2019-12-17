import random

#thisList = [4,6,2,8,6,9] #samples


def listValues():
    userList = int(input("Enter the amount of numbers in the list: "))
    listValues = []
    
    for x in range(userList):
        listValues.append(random.randint(1,10))
    print(listValues)

    return listValues     

def sumOfTwelves():
    thisList = listValues()
    addToTwelve = 0
    totalValuesCheck = 0
    lengthOfList = len(thisList)   # *(1) issue with range: unable to include last value of 9
    
    for listIndexValue in range(lengthOfList): #0-5 (6 values)
        valueToCompare = thisList[listIndexValue] # thisList[0] = "4"
        x = 0
        print("")
        print("value to compare:", valueToCompare)
        
        for x in range((listIndexValue + 1), lengthOfList): #****in order to not compare with itself and thus duplicate the number of twelves use +1  so that the next value is compared 4 --> 6,2,8,6,9
            print("value of x:", (listIndexValue + 1))

            if (valueToCompare + thisList[x]) == 12: # *(1) run time error without changes above 
                addToTwelve += 1
                print(valueToCompare, "+", thisList[x], "= 12" )
                print("")

            totalValuesCheck += 1


    return print("Total amount of sums of twelves is:", addToTwelve)
        

def checkRunProgram():
    runProgram = "yes"

    while True:
        try:
            runProgram = input("Would you like to run the program again? ").lower() #if "yes", program runs again
            #print("printed as:", newProgram)

            if runProgram == "yes":
                return True #if yes, continues running 

            if runProgram == "no":
                return False #no longer runs 
            
            else:
                x = 5/0 #Forces except to be run, since value is not either yes/no - until true will keep running 
        except:
            print("incorrect input") #runs, and then escapes back to while statement 

            
#Main Program

sumOfTwelves() #run without checking first to loop again 

while checkRunProgram(): #while this is true... (continues looping until "no")
    sumOfTwelves() #displays program

print("Program ended")
