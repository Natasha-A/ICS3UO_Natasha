'''
NOTES:

#** Multiple Return Values **#
#Example 1
#A function can return more than one value by listening them after the return statement
def sumProduct(numOne, numTwo):
    sum = numOne + numTwo
    product = numOne * numTwo
    return sum, product #returns two values back to the main program

#Main program
s, p = sumProduct(3,5) #Need to make sure that you use the same number of variables to store
#the results
print(s, p)

#Example 2 - Midpoint - returns the midpoint of the line segment

def midpoint(x1, y1, x2, y2):
    midx = (x1 + x2) / 2
    midy = (y1 + y2) / 2

    return midx, midy

#Main program
x,y = midpoint(9,4,-3,-4) #midx = x (stored in each variable), midy = y
print("The midpoint is, (" + str(x) + "," + str(y) + ").")

'''

#Exercise 1
def printFavourite():
    print("My favourite number is 6") 

#Exercise 2
def favourite():
    return "My favourite number is 6"

#Exercise 3

def findLargest(x, y, z):
    unOrderedList = [x, y, z]

    unOrderedList.sort()
    unOrderedList.reverse()

    largestNum = unOrderedList[0]

    return largestNum

#Main Program
printFavourite()
print( favourite())
print("largest Number:", findLargest(18,9,13))

#4 - logical errors

def sum(a,b):
    print(a + b)

    
#print(sum(10,11))#function already prints values, no need to reprint, only causes none value since none is returned. 

sum(4,5)#function already prints values, no need to reprint, only causes none value since none is returned. 


#5 - count duplicates

def countDups(x, y, z): #1,2,3
    dup = 0
    if x == y:
        dup += 1
    if x == z:
        dup += 1

    if dup >= 2:
        return 3
    elif dup == 1:
        return 2
    else:
        return 0

duplicates = countDups(1,8,3)
print("Num of duplicates:", duplicates)
     
