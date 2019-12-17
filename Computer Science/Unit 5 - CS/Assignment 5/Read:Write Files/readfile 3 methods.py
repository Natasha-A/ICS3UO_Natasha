
# Method 1 - reads all the lines at once
# The file "filename.txt" is opened. The 'r' opens the file as 'read only'.
# The file is automatically closed after the indented code is completed


'''
filename.txt

#what is written in file:
  123 567 8
onlyOneWord
aaa bbb;   ccc; dHello  World

Below is how it is converted based on the method used...

'''
#reads all the lines at once, and puts it into a list
with open("filename.txt", 'r') as file: #type casts as a file type
    allLines = file.readlines()
    print(type(allLines)) #is a list type
    print(allLines)
print("\n----------------\n")

'''
Prints:

<class 'list'>
['  123 567 8\n', 'onlyOneWord\n', 'aaa bbb;   ccc; dHello  World ']

----------------

'''


# Method 2 - reads one line at a time
# .strip() removes leading and trailing spaces and "\n"

with open("filename.txt", 'r') as file:  #same usage for read only
    for line in file:
        print(line.strip(), type(line), len(line)) #for x in file... reads each line and, and removes any leading and trailing spaces
print("\n----------------\n")

'''
Prints:

123 567 8 <class 'str'> 12
onlyOneWord <class 'str'> 12
aaa bbb;   ccc; dHello  World <class 'str'> 30

----------------

'''


# Method 3 - read one line at a time and convert each line into a list
# .split() splits the line using spaces
with open("filename.txt", 'r') as file:  
    for line in file:
        x = list(line.split()) #seperate each item as a list - casts it into a list
        print(x)
print("\n----------------\n")

'''
['123', '567', '8']
['onlyOneWord']
['aaa', 'bbb;', 'ccc;', 'dHello', 'World']

----------------
'''


#another way of doing method 3
# Method 3 - read one line at a time and convert each line into a list
# .split(";") splits the line using spaces
with open("filename.txt", 'r') as file:  
    for line in file:
        x = list(line.split(";")) #without any other arugments, uses what will seperate the list 
        print(x)
print("\n----------------\n")

'''
['  123 567 8\n']
['onlyOneWord\n']
['aaa bbb', '   ccc', ' dHello  World ']

----------------
'''
