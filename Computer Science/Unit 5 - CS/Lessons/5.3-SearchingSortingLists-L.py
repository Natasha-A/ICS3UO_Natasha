#5.3 - Search and Sorting Lists - Lesson
#.sort() method, sorted fuction

#1) .sort() method - sorts a list in place (changes the original list, doesn't return anything

a = [2,10,4,3,7]
a.sort()
print(a)

#2) sorted() function - returns a new sorted list without modifying the original list

a = [4,3,4,9,2]
sortedA = sorted(a)
print(a)
print(sortedA)

#Difference between .sort() and sorted
# - exactly the same except that sorted returns a new list instead of modifying the given list

#Example 1
a = ["world","hello"]
sortedA = a.sort() #makes no sense, error made 
print(sortedA)








#SEARCHING LISTS
#linear search algorithm -- move from item to item, sequential ordering
#until find what we are looking for or run out of items
#If run out out items -- searched item is not present

def linearSearch(myList, item):
    pos = 0
    found = False
    
    while pos < len(myList) and not found: #found is false - contine
        if myList[pos] == item:
            found = True #found true - stop program
        else:
            pos = pos + 1 #keep incremeting position to look for other values in list that may have the value,
        
    return found #check value of found
    
testList = [1,2,32,8,17,19,42,13,0]

print(linearSearch(testList, 3)) #looking for 3 - returns FALSE
print(linearSearch(testList, 13)) #looking for 13 - returns TRUE

#Other ways to search lists
# (1) is an element in a list - can use "in" and "not in"
items = ["book", "computer", "keys", "mug"]

if "computer" in items:
    print("computer in items")
    
if "atlas" in items:
    print("atlas in items")
else:
    print("atlast not in items")

if "marker" not in items: #TRUE
    print("marker not in items")

# (2) .index method - pass argument that matches a value in list, returns the index
#where the value is FIRST found, if no value found, an exception is thrown 

values = ["uno", "dos", "tres", "cuatro"]

n = values.index("dos")
print(n, values[n])

n = values.index("tres")
print(n, values[n])

try:
    n = values.index("?")
    print(n)
except:
    print("Not found ")


