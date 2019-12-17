#Assignment 4

#'products' function will be over written with product class
'''
class product():
    pass

    - To create list of product instances, look to Swift notes on classes
    - Able to append and remove class instances like would with lists?

'''

#total product object -- will be turned into list, which will then be appended to TOTAL list in menu function for user choice to view ENTIRE list

#individual OBJECT - added to total list 
def product():
    #product ONE will have the index of 0
    products = []

#************READ / WRITE METHODS*************#
def readCodes():
    print("Reading code list...")

    
    #Method 1 - list of str objects as one 
    with open("codesList.txt", 'r') as readFile:  
        for line in readFile:
            print(line.strip())
    

    '''
    #Method 2 - creating each object as a seperate list
    with open("codesList.txt", 'r') as readFile:  
        for line in readFile:
            x = list(line.split(";")) #without any other arugments, uses what will seperate the list 
            print(x)
    '''

def writeCodes():
    codes = prodCode() #taking lists of codes and writing to file

    print("Writing new code list...")


    #Method 1 - append to list
    writeFile = open("codesList.txt", "a")
    writeFile.write(str(codes))
    writeFile.close()

    '''
    #Method 2 - overwrites list
    with open("codesList.txt", 'w') as writeFile:
        writeFile.write(str(codes))
    '''


#************OBJECT METHODS*************#
#(1) NEW PRODUCT CODE
def prodCode():
    codes = []
    print("Creating new product code...")
    
    try:
        for x in range(3):
            code = input("Enter a product code: ")

            #already exisiting code, NOT able to use code:
            if code in codes:
                assert code not in codes #If runs false (code IS in Codes... runs except)

            #code doesn't exist yet, able to use code (append to list)
            else:
                codes.append(code)

    except AssertionError:
        print("Code already exists. Please enter a unique code.")

    return codes




#*************MENU PROGRAM*****************#
'''
    - will take all of the products and create a list, including each instance memeber able to be accessed and modified based on user input...
'''
def menu():
    productObjects = []

    '''
    read current list....
        - empty at first
    '''



readCodes()
writeCodes()
readCodes()

