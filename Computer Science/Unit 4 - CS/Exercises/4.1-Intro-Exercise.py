#4.1-Intro-Exercises
import time 
#1) print name

def printName():
    print("Natasha")

printName()

#2) print address
def printAddress():
    print("MTCC-6860") #calla to print function 

printAddress()

#3) print signature

def printSignature():
    print("*" * 20)
    printName()
    printAddress()
    print("*" * 20)

printSignature()

#4) checkName

def checkName():
    while True:
        name = input("Enter your name: ")
        print(name)
        break

checkName()

#5) CountDown

def countDown():
    for x in range(10,-1,-1):
        time.sleep(1) #delays 1 second
        print(x)

countDown()
    
