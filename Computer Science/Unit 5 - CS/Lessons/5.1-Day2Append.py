#5.1 - Lists - Day 2 - Lesson

#Adding elements to a list

x1 = [1, 2, 3]

#Let's say I wanted to add the numbers 4,5 and 6, to the end of the list. There are two ways to do it:

x1 = [1,2,3] + [4,5,6]

#or...

x2 = [1, 2, 3]

x2.append(4)
x2.append(5)
x2.append(6)

print(x1)
print(x2)

#Using a FOR loop to Add Elements to a List
alist1 = []

for i in range(10):
    alist1 = alist1 + [2 * i] #adds to new list value multipled by 2

print(alist1)


#OR
alist = []

for i in range(10):
    alist.append(2*i)

print(alist) #A list is creates: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


