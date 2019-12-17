#5.1 - Exercise - Intro to Lists

#a) changing elements

fiveList = ["*", "*", "*", "*", "*"]
print("The amount of elements in the list:", len(fiveList))

fiveList[3] = "#" #reasssigning: third element becomes #

print(fiveList[3]) #prints #

print(fiveList[4]) #prints last value

print("")

#b) numbers list

fiveZeroList = [0,0,0,0,0]

fiveZeroList[3] = "dog"

#version 1
for index in fiveZeroList:
    print(index)

print("")

#version 2 
for key in range(len(fiveZeroList)):
    print(str(key+1) + ":", end="") #extraneous - to display value in len 
    # (starting at 1) items
    
    print(fiveZeroList[key])

print("") 

#c) slicing words


mineCraft = "Minecraft"

print(mineCraft[0:4]) #prints the first 4 letters - mine
print(mineCraft[4:9]) #need to go 5-9 for elements - craft

#d) Lists

zeros = [0] * 7 #creates a list of [0,0,0,0,0,0,0]

print(zeros) #list of 0's

ones = [1] * 7

print(zeros + ones) #prints: [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
print(zeros * 3) #prints: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(ones + zeros)#prints: [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
print(zeros + [2,2,2])#prints:[0, 0, 0, 0, 0, 0, 0, 2, 2, 2]



