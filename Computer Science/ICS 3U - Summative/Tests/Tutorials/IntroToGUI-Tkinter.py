#Introduction to GUI - using Tkinter (built in library)

from tkinter import * #imports everything

#(1) building the window

root = Tk() #build object from class - creates a blank window

#creating text - "label"

#use label object:
theLabel = Label(root, text="Displaying Text!") #(placement, text)\
#tell where to place information
theLabel.pack() #where ever possible adds to

#running through loop in order to display continously 
root.mainloop()



