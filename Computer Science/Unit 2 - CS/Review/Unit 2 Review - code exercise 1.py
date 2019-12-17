#Unit 2 Review - Exercise 1 - DATES
month = int(input("Enter the the number of a month: "))

numJan = 31
numFeb = 28
numMar = 31
numApr = 30
numMay = 31
numJune = 30
numJul = 31
numAug = 31
numSep = 30
numOct = 31
numNov = 31
numDec = 30

if month <= 12 and month >= 1:
    if month == 1:
        print("The month of January has 31 days.")
    elif month == 2:
        print("The month of February has 28 days.")
    elif month == 3:
        print("The month of March has 31 days.")
    elif month == 4:
        print("The month of April has 30 days.")
    elif month == 5:
        print("The month of May has 31 days.")
    elif month == 6:
        print("The month of June has 30 days.")
    elif month == 7:
        print("The month of July has 31 days.")
    elif month == 8:
        print("The month of August has 31 days.")
    elif month == 9:
        print("The month of September has 30 days.")
    elif month == 10:
        print("The month of October has 31 days.")
    elif month == 11:
        print("The month of November has 31 days.")
    elif month == 12:
        print("The month of December has 30 days.")
else:
    print("You have entered an incorrect month number")
