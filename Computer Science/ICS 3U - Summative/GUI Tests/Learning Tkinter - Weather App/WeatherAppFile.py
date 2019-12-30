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

frame = tk.Frame(root, bg='#80c1ff', bd=5) #creates border space 'bd'
#anchors north makes it go does the top
frame.place(relx = 0.5, rely = 0.1, relwidth=0.75, relheight=0.1, anchor="n") #fills entirely relative to parent screen

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1) #fills the entire box as 1

button = tk.Button(frame, text="Test Button", font=40) #display in frame
button.place(relx=0.7, relwidth=0.3,relheight=1) #fills rest of screen

#lower frame - below entry and button

lowerFrame = tk.Frame(root, bg='#80c1ff', bd=10)
#has same width as 'frame' different height
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lowerFrame) #inside lowerframe, and remains within border of frame, and fills completely
#places off by 0.3 from button, width is greater, height same
label.place(relwidth=1, relheight=1)

root.mainloop()

