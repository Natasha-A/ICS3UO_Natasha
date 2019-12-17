'''
Name: Natasha Ahammed
Date: October 7, 2019
File Name: Natasha_Ahammed_21.py
Description: Program that takes two users' birthdays and checks who is older by comparing the their age in years, months, and days
Test Cases: Tesring out when the years the not the same, when they are the same, and subsequently when the months are equal/not equal and then finally when the days are equal and not equal. 
'''

#User inputs: first and second users' Birthday Dates (day/month/year)

#First User's Birthdate
birthdayTitle = print("Enter the birthday for the first person \n---------------------------------------")
#First person's info 
dayFirst = int(input("Day: "))
monthFirst = int(input("Month: "))
yearFirst = int(input("Year: "))
print("\n")

#Second User's Birthdate
birthdayTitle = print("Enter the birthday for the second person \n---------------------------------------")
#Second person info
daySecond = int(input("Day: "))
monthSecond = int(input("Month: "))
yearSecond = int(input("Year: "))

#Evaluate birthdats and determine who is older based on who has the lowest year, month and day

if yearFirst < yearSecond: #If the FIRST person was born in a lower year, they are older. 
    print("The first person is older in years.")
if yearSecond < yearFirst: #If the SECOND person was born in a lower year, they are older. 
        print("The second person is older in years.")

#If they are born in the SAME year, move onto comparing the months and days     
if yearFirst == yearSecond:
    if monthFirst == monthSecond: #if Months ARE same, compare days
        if dayFirst == daySecond:
            print("They are both the same age")
        elif dayFirst < daySecond: #If not equal in days, check who is older in days by checking who has a lower day in their bd
            print("The first person is older in days")
        elif daySecond < dayFirst:
            print("The second person is older in days")
    elif monthFirst < monthSecond: #Months are NOT same, compare who is older in months by checking who has a lower month in their bd
        print("The first person is older in months")
    elif monthSecond < monthFirst:
        print("The second person is older in months")
    
