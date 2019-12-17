#Number Flipper - Waterloo Challenge Program

numList = [0,1,2,3,4]
hvList = []
previous = [0,1,2,3,4] #has to start as original list
x = 1

print(numList[1], numList[2])
print(numList[3], numList[4])

userInput = str(input("Enter sequence of H and V: "))

hvList = userInput

for index in range(len(hvList)):

    #Horizontal Switches
    if hvList[index] == "H": 
        print(index, "H inputted")

    
        while x <= len(previous):
            if x == 1:
                del(numList[3])
                numList.insert(3, (previous[x])) #list.insert(index, element)
                print(x, numList)

            if x == 2:
                del(numList[4])
                numList.insert(4, (previous[x]))
                print(x, numList)

            if x == 3:
                del(numList[1])
                numList.insert(1, (previous[x]))
                print(x, numList)

            if x == 4:
                del(numList[2])
                print(x)

                numList.insert(2, (previous[x]))
                print(x, numList)

            x += 1

        
        x = 1 
        print("New Num List:", numList)

        previous = numList #assign new horitzontally changed list as previous list 



            
        







        

    elif hvList[index] == "V":
        print("V inputted")

    
    



