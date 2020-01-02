import tkinter as tk
import requests
from tkinter import font

# Constant Variables
#makes values easier to change
HEIGHT = 700
WIDTH = 800

# 6ab0b1938e19d5a796dafd62fcf82b75
#JSON objects
# api.openweathermap.org/data/2.5/weather?q={city name},{country code}

def formatResponse(weather):

    try:
        name = weather['name']
        descrip = weather['weather'][0]['description']
        temp = weather['main']['temp']

        finalStr = 'City: %s \nConditions: %s \nTemperature (C): %s' % (name, descrip, temp)
 
    except:
        finalStr = 'There was a problem retrieving the information.'

    return finalStr


    
def getWeather(city):
    weatherKey = '6ab0b1938e19d5a796dafd62fcf82b75'
    url = 'https://api.openweathermap.org/data/2.5/weather'

    #sending requests to server
    params = {'APPID':weatherKey, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params) #gets to url and params
    weather = response.json() #converts into python dictionary

    #displays LABEL as formatted response from function - UPDATES
    label['text'] = formatResponse(weather)


def displayWeather(entry):
    print("This is the entry:", entry)

#root window
root = tk.Tk()

# ----widgets----
#creating a canvas (size dimensions of screen) - goes into root
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack() #displays canvas

#CREATING BACKGROUND
backgroundImage = tk.PhotoImage(file="landscape.png")
backgroundLabel = tk.Label(root, image=backgroundImage) #places in root,
#which is the entire screen
backgroundLabel.place(relwidth=1, relheight=1)

#organizing widgets - frame
frame = tk.Frame(root, bg="#80c1ff")

#USING PLACE - Best Practice
# - able to place exactly where needed
# anchor - what point is at position eg) NW is default

frame = tk.Frame(root, bg='#80c1ff', bd=5) #creates border space 'bd'
#anchors north makes it go does the top
frame.place(relx = 0.5, rely = 0.1, relwidth=0.75, relheight=0.1, anchor="n") #fills entirely relative to parent screen

entry = tk.Entry(frame, font=("Courier", 18))
entry.place(relwidth=0.65, relheight=1) #fills the entire box as 1

#USING LAMDA - inline function temporary store memory to update and refine
button = tk.Button(frame, text="Get Weather", font=("Courier", 16), command=lambda: getWeather(entry.get()))#DISPLAYS ENTRY text
button.place(relx=0.7, relwidth=0.3,relheight=1) #fills rest of screen

#lower frame - below entry and button

lowerFrame = tk.Frame(root, bg='#80c1ff', bd=10)
#has same width as 'frame' different height
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


#creates fonts - with size in px
#puts into left with border 
label = tk.Label(lowerFrame,font=("Courier", 25), anchor = 'nw', justify='left', bd=4) #inside lowerframe, and remains within border of frame, and fills completely
#places off by 0.3 from button, width is greater, height same
label.place(relwidth=1, relheight=1)


root.mainloop()

