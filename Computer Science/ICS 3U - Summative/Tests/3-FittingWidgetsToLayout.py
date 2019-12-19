#3 - Fitting Widgets to layout

from tkinter import  *

root = Tk()

one = Label(root, text="One", bg="red", fg="white")
one.pack() #full width, at top

two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X) #makes as large as parent window is,fits in middle

three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y) #moves to side relative to parents


root.mainloop()
