'''
Name: Natasha Ahammed
Date: December 9 2019
File Name: Natasha_Ahammed_Assignment5.py
Description: Inventory program which allows user to be able to control various aspects of an inventory, including its products,\
details, stock, sales product, and save to a file in order to continually update from existing inventory
Test Cases: Try and Except ensures that values are correct data types, mutiple types/values and test and multipe testing menu \
program with changes to data to observe correct computations and displays
'''
#list of Products (updates based on mutable functions)
products = []
#**********CLASS***************#

#************* Class - 'product' object *************#
class Product():
    def __init__(self, prodCode = 0, descrip = 0, stockQty = 0, totalStock = 0, \
                 totalSales = 0): #default values of instance without alternate arguments provided. 
        self.prodCode = prodCode
        self.descrip = descrip
        self.stockQty = stockQty
        self.totalStock = totalStock
        self.totalSales = totalSales
    
    #format instance for user display
    def instTotalInfo(self):
        return '{:<15}{:<35}{:<15}{:<15}{:<15}'.format(self.prodCode,self.descrip,self.stockQty,self.totalStock,self.totalSales)


#*********READ / WRITE functions**********#
def writeInventory():
    with open("Products_List.txt", "w") as writeFile:
        productsValues = []
        productsList = []
        for x in range(len(products)):
            prodCode = products[x].prodCode
            descrip = products[x].descrip
            stockQ = products[x].stockQty
            totStock = products[x].totalStock
            totSales = products[x].totalSales

            #Creates a list of an instance to store in 2D .txt list
            productsList = [prodCode, descrip, stockQ, totStock, totSales]
            
            #instance added to parent list
            productsValues.append(productsList)


        #once iterated through instances, write to file 2D list
        writeFile.write(str(productsValues))

def readInventory():
    with open("Products_List.txt", 'r') as readFile:
        line = eval(readFile.readline())

        #iterate through written instances to be read back into program (as list objects)
        for x in range(len(line)):
            prodCode = line[x][0]
            descrip = line[x][1]
            stockQ = line[x][2]
            totStock = line[x][3]
            totSales = line[x][4]

            #instance of Product() object readded into list of products 
            product = Product(str(prodCode), str(descrip), int(stockQ), int(totStock), int(totSales)) #create/load instances
            
            products.append(product)


#************* General Functions (User Inputs, Format Display) *************#

#(1) user creates a product code:
def prodCode():
    codeCheck = True
    while codeCheck:

        try:
            code = input("Enter the product code: ")
            #print("Num of products in list:", len(products))

            if not code:  #code is empty (eg. user presses ENTER)
                raise AssertionError 

            if len(products) >= 1: #code is ALWAYS unqiue when only one product, once increase products
                #need to check for duplicate '.prodCode'

                for x in range(len(products)):
                    if code not in products[x].prodCode:
                        #print("code is NOT in products already")
                        codeCheck = False

                    elif code in products[x].prodCode:
                        #print("code is already in the products list")
                        raise ValueError

                        #codeCheck = True

            #code doesn't exist yet, able to use code (append to list)
            else:
                codeCheck = False

        except AssertionError:
            print("Please enter a valid code.")
            codeCheck = True

        except ValueError:
            print("Please enter a unique product code.")
            codeCheck = True

    return code


#(2) description of new product 
def description():
    
    descrip = input("Enter a brief description of the product: ")
    
    #no description provided (eg presses enter) (false)
    if not descrip:
        descrip = "None"
        
    #descirption is under capped length
    elif len(descrip) <= 30:
        descrip = descrip
    
    #descirption is greater than capped length
    else:
        descrip = descrip[0:30]
        descrip = descrip + "..."

    return descrip

#(3) Qty in stock (newly added) 
def stockQty():
    stockQty = True

    while stockQty:
        try:
            qty = int(input("Enter the quantity of the product: "))
            assert qty >= 0

            stockQty = False

        except AssertionError:
            print("Please enter a positive value.")
            stockQty = True

        except ValueError:
            print("Please enter the quantity of a product as a number.")
            stockQty = True
                                                
    return qty

# User enter quantity of items sold 
def newSale():
    addSale = True
    
    while addSale:
        try:
            sale = int(input("Enter the quantity of the product sold: "))
            if sale < 0:
                raise AssertionError
            else:
                #print("correct sale amount inputted")
                addSale = False

        except AssertionError:
            print("Please enter the sales of the product as a positive value.")
            addSale = True
            
        except:
            print("Enter the sale as a positive integer.")
            

    return sale

#Check user's search for a product, condition is if Product Code exists
def checkUserCodeInput():
    checkCode = True

    while checkCode:
        searchCode = input("Enter the code of the existing product: ")
        for x in range(len(products)):
            if searchCode == products[x].prodCode.lower():
                print("Product","'" + str(products[x].prodCode) + "'","found.")
                checkCode = False
                return products[x] #returns instance where corresponding prodCode is chosen
            checkCode = True #run through to check new user inputted prodCode


    
#Confirm if user wants to an delete item 
def checkToDelete():
    runProgram = "yes"
    while True:
        try:
            runProgram = input("Are you sure you want to delete this product?").lower() #if "yes", program runs again
            #print("printed as:", newProgram)

            if runProgram == "yes":
                return True #if yes, delete

            if runProgram == "no":
                return False  #if no, don't delete
            
            else:
                raise AssertionError #Forces except to be run, since value is not either yes/no - until true will keep running 
        except AssertionError:
            print("Incorrect Input. Please enter 'yes' or 'no'.") #runs, and then escapes back to while statement 


#Visual display of title/columns: 
def titleFormat(title):
    dash = '-' * 88
    print('{:^85}'.format("•" + str(title) + "•"))
    print(dash)

def columnFormat():
    dash = '-' * 88
    print('{:<15}{:<35}{:<15}{:<15}{:<15}'.format("Code","Description","Stock Qty","Total Stock","Sales"))
    print(dash)
    
#************* Menu Driven functions *************#

#(1) - Add a new product
def newProdAdded():
    #get user input for each parameter of a product instance: 
    pCode = prodCode()
    descrip = description()
    qStock = stockQty()
    totalStk = qStock
    #INSTANCE - new product created...
    product = Product(pCode,descrip,qStock,totalStk)#instance of product upates code, description, and stock quantity
    
    products.append(product) #new product added to the Products List

    #products length increases:
    print("Product", "'" + str(product.prodCode) + "'", "added to inventory.")


#(2) - list current inventory (products having stockQty > 0)
def currentInventory():
    titleFormat("Current Inventory")
    columnFormat()
    
    #products list is not empty
    if len(products) >=  1:
        for x in range(len(products)):
            if products[x].stockQty > 0:
                print(products[x].instTotalInfo())

    #product list IS empty len(products) == 0
    else:
        print("Current inventory is empty.")

#Display all products, regardless of in stock or not
def allProducts():
    titleFormat("Entire Inventory")   
    columnFormat()
    for x in range(len(products)):
        print(products[x].instTotalInfo())

#(3) - List product detail
def displayProductDetail():
    print("Searching for product to display details...")
    
    productChosen = checkUserCodeInput()

    titleFormat("Product Details")
    columnFormat()

    #prints out specific instance chosen based on product chosen 
    print(Product.instTotalInfo(productChosen))


#(4) - Remove product from inventory
def removeProduct():
    print("Searching for product to be deleted...")

    productChosen = checkUserCodeInput()

    #Display format 
    titleFormat("Product To Delete")
    columnFormat()
    
    print(Product.instTotalInfo(productChosen))

    #Condition raised to delete product or not
    while checkToDelete():
        products.remove(productChosen) #product deleted 
        print("Product", "'" + str(productChosen.prodCode) + "'", "is deleted." )
        break

#(5) - Edit product details
def editProductDetails():
    dash = '-' * 50
    print('{:^50}'.format("• Edit Product Details •"))
    print(dash)
    productChosen = checkUserCodeInput()

    print("Enter the new information for the product...")

    #edit product code, user enters new values:
    newProdCode = prodCode()
    newDescrip = description()
    newStockQty = stockQty()
    #if stock quantity changes, add value to total stock... (APPEND)

    #Updated values of instance of product:
    productChosen.prodCode = newProdCode
    productChosen.descrip = newDescrip
    productChosen.stockQty = newStockQty
    #new total stock is overwritten by new (initial) stock qty value changed 
    productChosen.totalStock = newStockQty

    print("Updated Product Code:", productChosen.prodCode)
    print("Updated Description:", productChosen.descrip)
    print("Updated Stock Qty:", productChosen.stockQty)


#(6) - Recieve Product in stock
def recieveStock():
    print("Searching for product to add stock to...")

    #adding to current stockQty, and total stockQty
    productChosen = checkUserCodeInput()
    newStockAdded = stockQty()

    productChosen.stockQty = productChosen.stockQty + newStockAdded
    productChosen.totalStock += newStockAdded

    print("New stock added total:", productChosen.stockQty)

#(7) - Sale of product (enter num items sold - stock qty decreases by that amount)
def productSale():
    print("Searching for a product to add sales...")
    productChosen = checkUserCodeInput()

    #get user input of sale 
    newProductSale = newSale()

    #if the sale is greater than actual stock, not possible to add sale (Results in neg. stock)
    if newProductSale > productChosen.stockQty:
        print("Sales cannot be added since there is not enough quantity.")
    else:
        print("Sale has been added.")
        #total sales increases by amount of new sales made 
        productChosen.totalSales = productChosen.totalSales + newProductSale
        
        #quantity decreasing by amount of sales made
        productChosen.stockQty = productChosen.stockQty - newProductSale

    print("\n")
    print("Updated Total Sales:", productChosen.totalSales)
    print("Updated Stock Quantity:", productChosen.stockQty)

# return to main program eg) run mainProgramOptions() print("Returned back to main program")

#(8) - Search for product (based on item code)
def searchForProduct():
    print("Getting search text to find items related in product codes...")
    userSearch = input("Enter search text: ")

    titleFormat("Searching for Products(s)")
    columnFormat()
    for x in range(len(products)):
        if userSearch in products[x].prodCode.lower(): 
            print(products[x].instTotalInfo())

def saveProgram():
    print("Saving program...")
    writeInventory()
    print("Program has been saved.")

        
def quitProgram():
    print("Saving program...")
    writeInventory()
    print("Thank you for using the Inventory Program.")


#************* MENU PROGRAM *************#
def menuOptions():
    dash = '-' * 40
    checkChoice = True
    print('{:^38}'.format("-- Product Inventory Program --"))
    options = [["Option", "Description"],\
               ["A","Add New Item"],\
               ["E", "Edit Item"],\
               ["R","Remove Item"],\
               ["C","Receive Stock"],\
               ["S","Sale of Product"],\
               ["F","Find/Search for item"],\
               ["L","List all items"],\
               ["I", "List Current Inventory"],\
               ["V","Save changes"],\
               ["Q", "Quit Program and Save Changes"]]

    #Format and print out options
    for i in range(len(options)):
        if i == 0:
         #format title of list
          print(dash)
          print('{:<10s}{:>4s}'.format(options[i][0],options[i][1]))
          print(dash)
        else:
          print('{:<10s}{:>4s}'.format(options[i][0],options[i][1]))
    print("\n")

    #Check if the user input corresponds to the letter options
    while checkChoice:
        userChoice = input("Please enter one of the letter options above: ").upper()
                     
        for x in range(len(options)):
            if userChoice == options[x][0]:
                #print("option matches letter", options[x][0])
                return userChoice
                checkChoice = False

            else:
                #print("option DOESN't matches letter", options[x][0])
                #raise AssertionError
                checkChoice = True
     
def inventoryMenu():
    #products = []
    #addedProducts = readInventory()
    #products.append(addedProducts)
    
    print("Length List:", len(products))

    #readNewProducts = readInventory()

    checkChoice = True
    options = [["Option", "Description"],\
               ["A","Add New Item"],\
               ["E", "Edit Item"],\
               ["R","Remove Item"],\
               ["C","Receive Stock"],\
               ["S","Sale of Product"],\
               ["F","Find/Search for item"],\
               ["L","List All Items"],\
               ["I", "List Current Inventory"],\
               ["V","Save changes"],\
               ["Q", "Quit Program and Save Changes"]]

    #'switch' case for option chosen
    while checkChoice:
    
        userChoice = menuOptions()
        
        #(1) - User chooses 'Add New Item' choice:
        if userChoice == options[1][0]:
            print("\n")
            print("Creating new product code...")
            newProdAdded()
            checkChoice = True


        #(2) - User chooses 'Edit Item' choice:
        elif userChoice == options[2][0]:
            print("\n")
            
            editProductDetails()
            checkChoice = True

        #(3) - User chooses 'Remove Item' choice:

        elif userChoice == options[3][0]:
            print("\n")
            
            removeProduct()
            checkChoice = True

        #(4) - User chooses 'Receive Stock' choice:
        elif userChoice == options[4][0]:
            print("\n")
            
            recieveStock()
            checkChoice = True
            
        #(5) - User chooses 'Sale of Product' choice:

        elif userChoice == options[5][0]:
            print("\n")
            
            productSale()
            checkChoice = True

        #(6) - User chooses 'Find/Search for item' choice:

        elif userChoice == options[6][0]:
            print("\n")
            
            searchForProduct()
            checkChoice = True

        #(7) - User chooses 'List all items' choice:

        elif userChoice == options[7][0]:
            print("\n")
            
            allProducts()
            checkChoice = True

        #(8) - User chooses 'List Current Inventory' choice:

        elif userChoice == options[8][0]:
            print("\n")
            
            currentInventory()
            checkChoice = True

        #(9) - User chooses 'Save changes' choice:

        elif userChoice == options[9][0]:
            print("\n")
            saveProgram()
            checkChoice = True

        #(10) - User chooses 'Quit Program and Save Changes' choice:
           
        elif userChoice == options[10][0]:
            print("\n")
            quitProgram()
            checkChoice = False
            

        print("\n")
        

#*****Main Program*******#
#Read inventory for the first time
readInventory()
#Run entire compiled inventory program 
inventoryMenu()

    

    
    

