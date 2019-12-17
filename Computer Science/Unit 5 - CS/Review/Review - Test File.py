a = "letter"

print(a[2:4])

b = [4,5.6,3, 20]

for num in b: #can take lists iterate elements of the list b - in range (element) 0-3
    print(num) #each element is assigned in loop

maxMinList = [4,56,2,19,-4, 0.2]

print(max(maxMinList)) #prints 56
print(min(maxMinList)) #prints -4 

my_list = [8, 6, 7, 2, 6, 8]

del(my_list[3])  #Removes value from the index at 3 
print(my_list) #[8, 6, 7, 6, 8] #Removes 2


my_list.remove(6)  #Calls method to remove specific value in list 

print(my_list)#[6, 7, 6, 8]

alist = [4, 6, 3, -1]
alist.insert(-1, -5) #if were to index at (-1) a negative value, would move one position left from last value (after -1),

print(alist)
