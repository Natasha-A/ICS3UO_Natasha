#class example
import datetime
#A class is a blueprint for creating instances - each instance will represent each employee

#---Employee Class---

class Employee:
    #PROPERTIES - accessed to entire class

    #(2) creating class varialves
    numOfEmps = 0 #inital value 
    raiseAmount = 1.04

    #constructor - init - runs EVERYTIME we create a new employee
    
    def __init__(self, first, last, pay): #usually called self (the class instance) first, then other variables
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.numOfEmps += 1 #only using class since applies to all instances.

    def fullName(self): #calls the instance of self
        
        return '{} {}'.format(self.first, self.last) #calls each instance using defined
        #properties so that each object can make use of the fullName method

    #(1) using instance variables
    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount) #in order to access class' property need
        #to access through class or instance itself

        #using self allows us to change value depending on the instance

    #(3) - CLASS METHOD: WORKING WITH CLASS INSTEAD OF INSTANCE 
    @classmethod #altering the function of method 
    def setRaiseAmount(cls, amount): #cls just represents 'class' 
        cls.raiseAmount = amount #amount - parameter take from raiseAmount

    @classmethod
    def from_string(cls, emp_str): #allowing user to enter emp info differently "from strings"
        first, last, pay = emp_str.split('-') #break up each attribute by splitting at hypens
                                #^
                    #uses any string from employee istances by using argument
        #above is same thing as first, last, pay = emp_str_1.split('-') for an instance

        #1) splits string on hypen....
        #2) creates a new employee object and returns it.

        return cls(first,last,pay) #same thing as: new_emp_1 = Employee(first,last,pay)

    #***STATIC METHOD - give away to use Static Method - if there is no usage of the class
    #or any instances use STATIC METHOD***
    @staticmethod
    def isWorkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


#(1) class variables   
emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

print(Employee.raiseAmount)
print(emp1.raiseAmount) #doesn't have attribute raiseAmount, accesing the class' raise amount
print(emp2.raiseAmount) #creates raise amount attribute for instance


#regular methods is a class - takes the instance as the first argument (self)
#(2) CLASS METHODS - affects entire class, not just specific instance

Employee.setRaiseAmount(1.05) #takes class object, changes amount from class, not instance
print("\nWith class method:")
print(Employee.raiseAmount)
print(emp1.raiseAmount) 
print(emp2.raiseAmount)

#by using @classmethod, same thing as...
Employee.raiseAmount = 1.05

#(3) CREATING ALTERNATIVE CONSTRUCTORS - if user using class has specific cases for user input (eg parsing)
print("\nparsing strings with alternative constructor: ")
emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1) #now can pass new strings (like above) without
#having to parse tje, 

print(new_emp_1.email)
print(new_emp_1.pay)

#(4) STATIC METHODS - connected to class but not instances

#STATIC METHOD - give away to use Static Method - if there is no usage of the class
    #or any instances use STATIC METHOD***
#recap: 1) regular methods automatically pass instance (self) as first argument
# 2) class methods passes class as first argument (cls)
# 3) static methods - doesn't pass anything automatically (behaves as functions) - doesnt
#have any specific value based on instance, just entire class

print("\nStatic method example - checking if date is weekday or weekend")
#example - current date time 
emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

import datetime
myDate = datetime.date(2016,7,10)

print(Employee.isWorkday(myDate))


'''
Option 1
#What looks like in raw form...

print("\nparsing strings: ")
emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

first, last, pay = emp_str_1.split('-') #break up each attribute by splitting at hypens

new_emp_1 = Employee(first,last,pay)

print(new_emp_1.email)
print(new_emp_1.pay)
'''






