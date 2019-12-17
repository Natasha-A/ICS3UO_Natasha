#class example

#A class is a blueprint for creating instances - each instance will represent each employee

#---Employee Class---

class Employee:
    #PROPERTIES - accessed to entire class
    #Class Variables - variables that are shared among all instances of a class

    #(2) creating class varialves
    numOfEmps = 0 #inital value 
    raiseAmount = 1.04

    #constructor - init - runs EVERYTIME we create a new employee
    
    def __init__(self, first, last, pay): #usually called self first, then other variables
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
        

#(1)      
emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

'''
Option 1 - individually apply raise to each instance
print(emp1.pay)
emp1.applyRaise()
print(emp1.pay)
'''

#Option 2 - Use class variable

#or from instance...
print(emp1.raiseAmount) #doesn't have attribute raiseAmount, accesing the class' raise amount
print(emp2.raiseAmount) #creates raise amount attribute for instance

#can access from class directly...
print(Employee.raiseAmount)

#To illustrate difference between instance atributes and class attributes...


#print(emp1.__dict__) #create key and value of instance and it's atributes
#print(Employee.__dict__) #includes raiseAmount value in class, which can be accesed by each
#instance

#What is just wanted to change the raise amount for one employee?
print("\nChange to raise for employee 1:")
emp1.raiseAmount = 1.05 #changes value for instance of emp1 ONLY
print(emp1.raiseAmount)

#check to see if change was made in instance:
#print(emp1.__dict__) #DOES have raiseAmount attribute added 
#print(emp2.__dict__) #DOESNT have raiseAmount attribute added to it 

#(2) For each instance, able to increment value of employees, which is addressed for each
#object created from class (2 objects)
print("\nNumber of Employees:")
print(Employee.numOfEmps)

