#5.2 - Working with Lists - Lesson

#Examples of list functions and methods

#MAX AND MIN funcs
#max and min functions for the largest and smallest values in a list

numbers = [1,2, 3.14, 99.99]
letters = ['x', 'y', 'z']
letnum = ['a', 'b', 1, 2]

print(max(numbers))
print(min(letters)) #simply by amount, x is first - so min, z last - so max.
#print(max(letnum)) cannot have different types


#DEL func - delete element for certain position (rather than by value)

#can remove single element or ALL elements defined by a slice

#example 1
listOne = [1,2,3,4,5,6]
del(listOne[0]) #removes from list one - 1
print("first element removed:", listOne)#prints: [2, 3, 4, 5, 6]


del(listOne[0:3])
print("list one values with 0-2 deleted:", listOne)

'''
listTwo = [0,1,2,3]
x = 10
del(listTwo[x]) #non existent, since no value at 10

print("list two:", listTwo)
'''


#*** del func does not return list with element removed. It CHANGES the List, cannot reassign:
# eg --> newlist = del(L[0])

#SUM function - returns sum of all elements in a list (doesn't have to be same time)

total = sum([1,2,3])
print(total) #prints: 6



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

#########################################

#Difference between del and .remove

#.remove - method searches through list for value and removes the FIRST instance of it
#del - function where can specify the exact location of element that you want to remove

L = ["school", "is", "not", "awesome"]

L.remove("not") #removes "not"

del(L[len(L)-1]) #removes 4 - 1 ---> third element : "awesome"
print(L)
