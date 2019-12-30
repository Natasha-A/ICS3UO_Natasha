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
#relx,rely used to center screen by making 10% towards boundaries at all times
#relwidth,relheight used to determine the sizing for the widget screen relative to parent screen
frame.place(relx = 0.1, rely = 0.1, relwidth=0.8, relheight=0.8) #fills entirely relative to parent screen

# button, multiple key word arguments that can be passed
# button = tk.Button(root, text="Test Button", fg='blue')
button = tk.Button(frame, text="Test Button", fg='blue') #display in frame

#USING GRID - able to use row/columns
button.grid(row=0,column=0)

#label widget
label = tk.Label(frame, text="This is a label", bg="yellow")
label.grid(row=1,column=1) # goes beside button for column =2

#entry text widget
entry = tk.Entry(frame, bg="green")
entry.grid(row=2, column=2)

#run application
root.mainloop()
