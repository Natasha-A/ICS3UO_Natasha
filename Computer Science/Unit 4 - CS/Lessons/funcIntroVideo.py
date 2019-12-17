def hello_func(): #defining a function 
    #pass #no values yet
    print("Hello function!") #no longer need to print hello

#allows to put code with specific needs repeatedly, changing in one location (Dont Repeat Yourself)

#hello_func() #runs function code


hello_func()
hello_func()
hello_func()
hello_func()

#allows us to operate on data and respond with a new results

#treat return value as data type as it is - as a string 
def helloFunc():
    return "Hello Function returned!" #able to return value 

print(helloFunc()) 

print(helloFunc().upper) #able to treat return as data type

#greeting is a varialbe == hi 
def hello_function(greeting, name:"You"): #set default value as "You"
    return '{} Function.'.format(greeting,name)

print(hello_function("Hi", name: "Corey")) #able to have different cases 
#8.08





