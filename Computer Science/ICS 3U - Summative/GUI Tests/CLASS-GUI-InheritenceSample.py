import tkinter as tk

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        # CONFIG PROPERTIES
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # runs through pages - saving the frames added, and bringing to the front
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

'''
def qf(stringtoPrint):
    print(stringtoPrint)
'''
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #creating a button - calls qf when pressed -- can use to proceed with game?
        # lamba doesn't run immediately - creates in moment
        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne)) # goes to page one
        button.pack()

        button = tk.Button(self, text="Visit Page 2",
                           command=lambda: controller.show_frame(PageTwo))  # goes to page one
        button.pack()

# Page One
class PageOne(tk.Frame):

    # always creating under init, since always working into each 'sel' call of object
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage)) # goes back to start page
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))  # goes back to start page
        button2.pack()

# Page One
class PageTwo(tk.Frame):

    # always creating under init, since always working into each 'sel' call of object
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage)) # goes back to start page
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))  # goes back to start page
        button2.pack()

# when adding new information - create lamda functions which will call game functions in order to run forward

app = SeaofBTCapp()
app.mainloop()