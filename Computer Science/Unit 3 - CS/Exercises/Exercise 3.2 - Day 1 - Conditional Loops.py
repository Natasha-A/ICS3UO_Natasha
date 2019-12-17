#Exercise 3.2 - Day 1 - Conditional Loops

#Exercise 2 - multiples given integer until exceeds 10,000
integer = int(input("Enter a digit to multiply by three: ")) #300
newInteger = integer * 3 #initial multiplication by 3
while newInteger <= 10000: #0
    print(newInteger)
    newInteger = newInteger * 3 #continue multiplying by 3

#Exercise 3 - Enters for correct name

name = ""
incorrectNameCounter = 0

while name != "tim" and name != "natasha":
    name = str(input("Enter your name: ")).lower()
    if name != "tim" and name != "natasha":
        print("You are not Tim or natasha!")
        incorrectNameCounter += 1

if name == "tim":
    print("You are Tim.")
elif name == "natasha":
    print("Your name is Natasha!")

if name == "tim" or name == "natasha":
    print("The number of incorrect name attempts are: ", incorrectNameCounter)

userMathA = 0
while not userMathA == 8:
    userMathA = int(input("What is the square root of 64? "))
    if not userMathA == 8:
        print("You are entered the incorrect answer, try again.")

if userMathA == 8:
    print("You have entered the correct answer of 8.")

    
    
