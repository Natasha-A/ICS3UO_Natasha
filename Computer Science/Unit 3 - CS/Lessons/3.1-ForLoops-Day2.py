#3.1 For Loops - Day 2 - Lesson

number = int(input("Enter a number to multiply by: "))

for i in range(1,13):
    print(i, "x", number, "=", (i * number))

#Squares and cubes
    

#Accumulating Values - examples: adding student grades, cash register total

sum = 0 #Need to initalize sum - know where to start from

print("This program will add 3 integers: ")

for i in range (3):
    num = int(input("Enter number: "))
    sum += num

print("The sum is ", sum)

#example 2
win = 0
loss = 0 

for game in range(10):
    userInput = input("Enter result of game (W) or (L): ").lower()
                      
    if userInput == "w":
        win = win + 1        
    elif userInput == "l":
        lose = lose + 1
    else:
        print("You entered the incorrect value")
        
print("You won", win, "game(s).")
print("You loss", loss, "games(s).")


#For Loops - Day 3 - Lesson

for x in range(1,101):
    numberDivisible = x % 17 #Isn't true until x = 17 
    if numberDivisible == 0:
        print(x,end=" ")

    

        




