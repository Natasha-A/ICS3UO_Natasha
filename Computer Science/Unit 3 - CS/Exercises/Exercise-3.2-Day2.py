
#Exercise 1 - repeat word
word = ""
while not word == "quit":
    word = str(input("Enter a word of your choice: "))
    print(word)
print("Goodbye!")

#Exercise 2 - square root numbers

amount = 1
numbOfInt = int(input("Enter the amount of numbers to calculate: "))
inputtedNums = 0
squaredNum = 0
sumOfNums = 0 
while amount <= numbOfInt:
    amount += 1
    inputtedNums = int(input("Enter a number to add to square: "))
    if inputtedNums >= 1: 
        squaredNum = inputtedNums ** 2
        sumOfNums += squaredNum
        print(sumOfNums)
    else:
        print("You have entered a negative number. The previous sum is", sumOfNums)
        break

#Exercise 3 - largest of n positive integers

amount = 1
number = 1
largestNum = 0
numbers = int(input("Enter the amount of numbers to determine the largest of them: "))

while amount <= numbers:
    amount += 1
    number = int(input("Enter a number: "))
    if number > largestNum:
        print("The largest number is:", number)
        largestNum = number
    if number < largestNum:
        print("The second largest number is:", number)

#Exercise 4 - user enters word to amounts and can change termination key word

terminateWord = ""
newTerminateWord = str(input("Enter a word that will terminate the program: "))


while terminateWord != newTerminateWord:
    word = str(input("Enter a word to display: "))
    numberDisplay = int(input("Enter the amount of times to display the word: "))
    print((word*numberDisplay),sep=" ")
    terminateWord = str(input("Enter the terminate word to end the program: "))


