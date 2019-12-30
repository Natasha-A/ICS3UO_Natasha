#2) Organizing the layout
from tkinter import *

#always include root (main object) and mainLoop()

root = Tk()

#containers 
topFrame = Frame(root) #goes in the main window
topFrame.pack() #tells frame to be placed into window 
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM) #tell where to place (in reference to top window)

#creating widgets - buttons
button1 = Button(topFrame, text="Button 1", fg="red") #creates button object (choose a Frame, text info, colour)
button2 = Button(topFrame, text="Button 2", fg="blue") 
button3 = Button(topFrame, text="Button 3", fg="green") 
button4 = Button(bottomFrame, text="Button 4", fg="purple")

#displays buttons 
button1.pack(side=LEFT) #places as far left as possible 
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

]
root.mainloop()
