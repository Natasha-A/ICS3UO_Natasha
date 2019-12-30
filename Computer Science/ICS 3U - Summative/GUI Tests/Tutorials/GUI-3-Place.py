import tkinter as tk

# Constant Variables
#makes values easier to change
HEIGHT = 700
WIDTH = 800

#root window
root = tk.Tk()

# ----widgets----
#creating a canvas (size dimensions of screen) - goes into root
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack() #displays canvas

#organizing widgets - frame
frame = tk.Frame(root, bg="#80c1ff")

#USING PLACE - Best Practice
# - able to place exactly where needed
# anchor - what point is at position eg) NW is default

#relx,rely used to center screen by making 10% towards boundaries at all times
#relwidth,relheight used to determine the sizing for the widget screen relative to parent screen
frame.place(relx = 0.1, rely = 0.1, relwidth=0.8, relheight=0.8) #fills entirely relative to parent screen

# button, multiple key word arguments that can be passed
# button = tk.Button(root, text="Test Button", fg='blue')
button = tk.Button(frame, text="Test Button", fg='blue') #display in frame

#places at top left, fills by 0.25 and 0.25 from frame
button.place(relx=0,rely=0, relwidth=0.25,relheight=0.25)

#label widget
label = tk.Label(frame, text="This is a label", bg="yellow")
#places off by 0.3 from button, width is greater, height same
label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)

#entry text widget
#offest by 0.8 to start at 0.8
entry = tk.Entry(frame, bg="green")
entry.place(relx=0.8, rely=0, relwidth=0.45, relheight=0.25)
#run application
root.mainloop()
