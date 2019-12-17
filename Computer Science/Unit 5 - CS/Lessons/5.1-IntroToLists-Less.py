#5.1 - Intro To Lists - Lesson

#Groups of elements that are accessed by indexing - built in array data types

#List of numbers
x = [1,2,3]
print(type(x)) #<class 'list'> #type as list

x = ["hello", "world"] #string list

#can be multiple
'''
drawer, full of drawers in it
x have 3 drawers in it, with 3 items in it

x = [1,2, "hello", "world", ["another, "lists"]]

'''

#Indexing in lists - value

alist = [1, 2, "J", 23, "o", "", 0, "to", -4]
print(alist[4]) #prints o
print(alist[2]) #prints J
print(alist[0]) #prints 1
print(alist[-2]) #goes to last one, printing -4 (don't go beyond -1)

#Indexing in Lists

alist = [1, 2, "J", 23, "o", "", 0, "to", -4]
alist[5] = -67.8 #reassigning position of 5 as -67.8
alist[1] = "dog"

print(alist) #print: [1, 'dog', 'J', 23, 'o', -67.8, 0, 'to', -4]


print("")
#LEN - short for length

x = [6,7,8] 

#tells how many items are in the list
print(len(x)) #this gives how much items are in the list

print(x[len(x)-1]) #2 - giving the last item (within 0-2) length = 2 --> print(x[2]) prints index 2 - "8" 
#takes last value - printing 8 

#print(x[len]) #looking for the element in 3 (length), yet there is only 0-2 values ERROR


print("")
#ADDING AND MULTIPLYING LISTS

a = [1,2,3]
b = [4,5]

print(a + b) #[1, 2, 3, 4, 5] puts lists together

print(b * 3) #[4, 5, 4, 5, 4, 5] puts lists 3 times of b 4,5 * three


print("")
#SLICING LISTS - getting a part of a list
x = ["r", "o", "p", "e"]

print(x[0:2]) #Prints: ['r', 'o'] #goes from 0-1
print(x[1:4]) #Prints: ['o', 'p', 'e'] #prints out 1-4 not including "r"

str1 = "Computer Science"

print(str1[0:8]) #prints the first 8 letters - "Computer"
 #as characters...
a = "Computer"
b = "Science"

#or.... as variables
myList = [a,b]

print("a[0:2]=",a[0:2]) #printss first and second letters "Co"
print("myList[0:1]=", myList[0:1]) #prints "Computer" as a list 



print("")
#Using for loops with LISTS

#1) By element
b = [17, "i", 3, 5.6]

for i in b: #can take lists iterate elements of the list b - in range (element) 0-3
    print(b) #each element is assigned in loop

print("")

#2) By index 
b = [17, "i", 3, 5.6]

for i in range(len(b)): #using length to determine amount in list (4)
    print(b[i]) #iternations througn b[0] = 17, b[1] = i, b[2] = 3, b[3] = 5.6




