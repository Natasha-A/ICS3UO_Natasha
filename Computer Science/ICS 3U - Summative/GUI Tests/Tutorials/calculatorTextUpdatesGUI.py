#Updating Text - Calculator App
from tkinter import *
'''
root = Tk()

label1 = Label(root, text = "Enter your expression:")
label1.pack()

#update a label
def evaluate(event):
    data = e.get() #take 'e' by 'getting' #takes all info from expression

    #setting the text from different location using CONFIG 
    ans.configure(text = "Answer:" + str(eval(data)))  #takes data and changes into new answr
    

#entry - to get value call in EVALUATE()
e = Entry(root)

#user enters 'enter key'

#binding - for enter key - takes what 'e' holds
e.bind("<Return>", evaluate)
e.pack()

#answer of label
ans = Label(root)
ans.pack()


#evaluate input and display 
root.mainloop()
'''
#updating text using StringVar()
root = Tk()

#***if want label's text to update, everytime change stringvars() text, the label's text will also update
equation = StringVar() #resets every time btnPress()

equa = ""
 
calculation = Label(root, textvariable = equation) #setting to equation -- changes as it updates using
# textvariable

#set value of text
equation.set("23+54")

#creates grid 
calculation.grid(columnspan = 4)

#calling functions for every button
def btnPress(num): #holds string of equation
    global equa #changing global variable
    equa = equa + str(num) #add the new number to the string of new number
    equation.set(equa)

#lamdba - doesnt need a return statement - allows to display for fields 
Button0 = Button(root, text = "0", command = lambda: btnPress(0)) #lamda function creates instanationalusy
Button0.grid(row = 4, column = 3) #allows it to be DISPLAYED in the program

Button1 = Button(root, text = "1", command = lambda: btnPress(1)) #lamda function creates instanationalusy
Button1.grid(row = 1, column = 0)

Button2 = Button(root, text = "2", command = lambda: btnPress(2)) #lamda function creates instanationalusy
Button2.grid(row = 1, column = 1)

Button3 = Button(root, text = "3", command = lambda: btnPress(3)) #lamda function creates instanationalusy
Button3.grid(row = 1, column = 2) #allows it to be DISPLAYED

Button4 = Button(root, text = "4", command = lambda: btnPress(4)) #lamda function creates instanationalusy
Button4.grid(row = 2, column = 0) #allows it to be DISPLAYED

Button5 = Button(root, text = "5", command = lambda: btnPress(5)) #lamda function creates instanationalusy
Button5.grid(row = 2, column = 1) #allows it to be DISPLAYED

Button6 = Button(root, text = "6", command = lambda: btnPress(6)) #lamda function creates instanationalusy
Button6.grid(row = 2, column = 2) #allows it to be DISPLAYED

Button7 = Button(root, text = "7", command = lambda: btnPress(7)) #lamda function creates instanationalusy
Button7.grid(row = 3, column = 0) #allows it to be DISPLAYED

Button8 = Button(root, text = "8", command = lambda: btnPress(8)) #lamda function creates instanationalusy
Button8.grid(row = 3, column = 1) #allows it to be DISPLAYED\

Button9 = Button(root, text = "9", command = lambda: btnPress(9)) #lamda function creates instanationalusy
Button9.grid(row = 3, column = 2) #allows it to be DISPLAYED\

Plus = Button(root, text = "+", command = lambda: btnPress("+")) #lamda function creates instanationalusy
Plus.grid(row = 1, column = 3) #allows it to be DISPLAYED\

Minus = Button(root, text = "-", command = lambda: btnPress("-")) #lamda function creates instanationalusy
Minus.grid(row = 2, column = 3) #allows it to be DISPLAYED\

Divide = Button(root, text = "/", command = lambda: btnPress("/")) #lamda function creates instanationalusy
Divide.grid(row = 3, column = 3) #allows it to be DISPLAYED\

Mutliply = Button(root, text = "*", command = lambda: btnPress("*")) #lamda function creates instanationalusy
Multiply.grid(row = 4, column = 3) #allows it to be DISPLAYED\

#Equal = Button(root, text = "/")
#Equal.grid(row = 4, column = 2)

#Equal = Button(root, text = "/")







root.mainloop()






