
import tkinter as tk
import time

def Draw():
    global text

    frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)

    text2=tk.Label(frame,text="Welcome to Python Pokemon!")
    text2.pack()
    root.after(10000, Draw) # every second...

    text=tk.Label(frame,text="To begin, choose your character!")
    text.pack()
    root.after(4000, Draw) # every second...


def SecondDraw():
    global text

    frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)

    text=tk.Label(frame,text="Choose a pokemon!")
    text.pack()
    root.after(1000, Draw) # every second...        
        

def Refresher():
    global text

    text.configure(text="Trainer RED wants to battle!")
    print("calling root.after")
    root.after(5000, Draw) # every second...
        


root=tk.Tk()
Draw()
Refresher()
root.mainloop()

