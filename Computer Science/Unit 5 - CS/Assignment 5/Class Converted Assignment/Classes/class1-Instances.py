#class example

#A class is a blueprint for creating instances - each instance will represent each employee

#---Employee Class---

class Employee:
    #(INSTANCE) Option 2 - using init() able to create within class initial user info.

    #constructor
    def __init__(self, first, last, pay): #usually called self first, then other variables
        #when using methods, recieves the instance as the first argument

        #doesn't have to be self.first = first, can be self.fname... - first
        self.first = first #*NOTE: same thing as emp1.first = "Corey" - same object 
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    #Using method - put functionality into one place for an action - eg displaying first name and last name

    #***always include self arguement***
    def fullName(self): #calls the instance of self
        
        return '{} {}'.format(self.first, self.last) #calls each instance using defined
        #properties so that each object can make use of the fullName method
        
emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

#(3) calling - calls instance itself, no need to pass as argument
print("\nUsing Instance:")

print(emp1.fullName()) #takes fullName() method and prints out for instance of emp1
print(emp2.fullName()) #takes fullName() method and prints out for instance of emp2
#works the same way in creating instances with properties/methods called:
print(emp1.email)
print(emp2.email)


#(3) calling - Also can run mentods using class name itself
print("\nUsing Method:")
print(Employee.fullName(emp1)) #call method on class, and need to pass instance to know where to pass
#passing emp1 as self instead 








''' No longer necessary 
#(INSTANCE) Option 1 - manually set up initial user information
#Two seperate instances
emp1 = Employee() #contains data for each variable that is unique to it
emp2 = Employee()

#Both are now two seperate objects at different locations:
print(emp1)
print(emp2)

#creating new variable for instance of a employee 1
emp1.first = "Corey"
emp1.last = "Schafer"
emp1.email = "Corey.Schafer@company.com"
emp1.pay = 50000


#creating new variable for instance of a employee 2
#now each instanc e
emp2.first = "Test"
emp2.last = "User"
emp2.email = "Test.User@company.com"
emp2.pay = 60000

print(emp1.email) #prints out emails
print(emp2.email)
'''

