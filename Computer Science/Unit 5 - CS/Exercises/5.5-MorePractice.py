#5.5 - Exercises - More Practice
#1) (a) product list

def product(alist):
    productList = alist
    previous = 1 

    for indexNum in range(len(productList)):
        sumProduct = productList[indexNum] * previous
        #print(sumProduct)
        
        previous = sumProduct

    print("The products of the list is:", productList)


testList = [3, 5, -1, 4, 3]
product(testList)

'''
def unique(alist):
    uniqueList = alist
    duplicateNum = 0
    uniqueNums = []

    for checkForNum in range(len(uniqueList)):
        for aNum in range(len(uniqueList)):
            if uniqueList[checkForNum] == uniqueList[aNum]:
                duplicateNum += 1 #true for same value once, then check for duplicates
                print(uniqueList[checkForNum], "IS## equal to:", uniqueList[aNum],end="")
                print("Numb of duplicates:", duplicateNum)


            else:
                print(uniqueList[checkForNum], "is not equal to:", uniqueList[aNum])
                print("***Numb of duplicates", duplicateNum)
                
            dulicateNum = 0 

        if duplicateNum > 2:
            print("\n")
            print(uniqueList[checkForNum], "has duplciates")
        else:
            print("\n")
            print(uniqueList[checkForNum], "is UNQUE")
            uniqueNums.append(uniqueList[checkForNum])
            print(uniqueNums)
                
'''

#1.b
'''

def unique(alist):
    theList = alist
    duplicateNums = 0
    unqiueNums = []

    for checkForNum in range(len(theList)):
        for aNum in range(len(theList)):
            if checkForNum in theList:
                duplicatesNums += 1


        if duplicateNums >= 2:
            print(unqiueNums[checkForNum], "is not unqiue")

        else:
            print(unqiueNums[checkForNum], "IS unqiue")
    
    




'''

'''
def unique(alist):
    uniqueList = alist
    duplicateNum = 0
    uniqueNums = []

    for checkForNum in range(len(uniqueList)):
        for aNum in range(len(uniqueList)):
            if uniqueList[checkForNum] == uniqueList[aNum]:
                duplicateNum += 1 #true for same value once, then check for duplicates
                print(uniqueList[checkForNum], "IS## equal to:", uniqueList[aNum],end="")
                print("Numb of duplicates:", duplicateNum)


            else:
                print(uniqueList[checkForNum], "is not equal to:", uniqueList[aNum])
                print("***Numb of duplicates", duplicateNum)
                
            dulicateNum = 0 

        if duplicateNum > 2:
            print("\n")
            print(uniqueList[checkForNum], "has duplciates")
        else:
            print("\n")
            print(uniqueList[checkForNum], "is UNQUE")
            uniqueNums.append(uniqueList[checkForNum])
            print(uniqueNums)
         
testList = [1, 2, 1, 3, 2, 5]
unique(testList)
'''

'''
Notes:
#example 1
listOne = [1,2,3,4,5,6]
del(listOne[0]) #removes from list one - 1
print("first element removed:", listOne)#prints: [2, 3, 4, 5, 6]


del(listOne[0:3])
print("list one values with 0-2 deleted:", listOne)

######Adding/Deleting Elements#######

#To add and element - method (modifies the object, doesn't just print or return a value)
#.append(value)

#To insert an element into the list, use...
#.insert(index,value)

#to reverse a list, use...
#.reverse()

#remove the first occurance of a value, regardless of how many time it appears..
#.remove(value)

#EXAMPLE

l = [1,2,3]
l.append(4) #prints: [1,2,3,4]
l.insert(2,-5) #prints: [1, 2, -5, 3, 4] --- inserts -5 at 2 (spot 3)
l.remove(1) #prints: [2, -5, 3, 4] -- removes 1
l.reverse() #prints: [4, 3, -5, 2] --- reversed
print(l)


#Difference between del and .remove

#.remove - method searches through list for value and removes the FIRST instance of it
#del - function where can specify the exact location of element that you want to remove

L = ["school", "is", "not", "awesome"]

L.remove("not") #removes "not"

del(L[len(L)-1]) #removes 4 - 1 ---> third element : "awesome"
print(L)


'''

#1.c) duplicates

def duplicate(alist):
    duplicateNums = 0
    #theList = alist
    dupsList = []
    
    for index in range(len(alist)):
        for num in range(len(alist)):
            if alist[index] == alist[num]:
                duplicateNums += 1
            else:
                print("not a duplicate.")
        if duplicateNums == 2:
            print("this is a duplicated num:", alist[index])
            dupsList.append(alist[index])
            
        else:
            print("this is NOT a duplicated num:", alist[index])
        duplicateNums = 0 #RESETS TO ZERO        


    setList = list(set(dupsList)) #takes only unqiue values of list!!

    print(setList)


#2) fibonacci list
#b) Fibonanci -- Good practice!

def fibSeq(numbersInFib):
    previous = 0
    sumOfNum = 1
    newNum = 0
    fibList = []

    #in order to avoid duplicate of each number, divide by two
    numbersInFibRemainder = numbersInFib / 2 #check to see if number is even or not
    if (numbersInFib % 2) != 0:
        print(sumOfNum) #if not even, can print extra number to add to proper numbersInFib amount 

    numbersInFib = numbersInFib // 2 #since printing twice, only need half expected numbers 
    for amount in range(int(numbersInFib)):
        newNum = previous + sumOfNum
        previous += sumOfNum #two seperate sequencial fib caluations taking place at once, same results, one stores as the previous number, while the other stores as next number 
        #print(newNum)
        fibList.append(newNum)
        sumOfNum = previous + sumOfNum #creates next following fib number by add previous two nums
        #print(sumOfNum)
        fibList.append(sumOfNum)

    return fibList

    

fibs = fibSeq(20)
print("Fib. List:", fibs)




randomList = [1,2,1,3,2,5]

duplicate(randomList)
