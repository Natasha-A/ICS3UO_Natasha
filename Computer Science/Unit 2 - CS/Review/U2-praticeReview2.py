#Practice Review 2 - Exercise 2.3

'''
Name: Natasha Ahammed
Date: October 4, 2019
File Name: U2-praticeReview2
Description: Reviewing nested ifs and boolean cases, 2.3 and 2.4 exercises
Test Cases: multiple values, both negative and decimals
'''

#Exercise 2

#Input - tire pressures
rFrontPressure = int(input("Enter the right front pressure: "))
lFrontPressure = int(input("Enter the left front pressure: "))
rRearPressure = int(input("Enter the right rear pressure: "))
lRearPressure = int(input("Enter the left rear pressure: "))

if (rFrontPressure != lFrontPressure) or (rRearPressure != lRearPressure):
    if rFrontPressure == lFrontPressure:
        print("Front tires are ok")
    if rFrontPressure != lFrontPressure:
            print("Front are not ok")
    if rRearPressure == lRearPressure:
        print("Back tires are ok")
    if rRearPressure != lRearPressure:
            print("Back are not ok")
else:
    print("Tire inflation is ok")



age = int(input("Enter your age: "))
income = int(input("Enter your income: "))

min_age = 12
min_income = 40000

if age > min_age:
    if income >= min_income:
        print("Accept")
    else:
        print("Reject")

#2.4 - Medical program

name = str(input("Enter your name: "))
gender = str(input("Enter your gender: "))
position = str(input("Enter your position: "))

if position.lower() != "doctor":
    if gender.lower() == "female":
        print("Mrs.", name)
    elif gender.lower() == "male":
        print("Mr.", name)
else:
    print("Dr.", name)

for n in range(1, 6):
	print("n\n")

