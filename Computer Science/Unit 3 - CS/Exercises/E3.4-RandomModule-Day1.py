#Exercise 3.4 - Random Module - Day 1
import random
'''
#1) *** Random module ***

#a) sum of two dice rolled

dies = random.randint(2,12) #generates integer between two values (values of 2 dice)

sumOfDies = dies
print("The sum of 2 dies are:", sumOfDies)

#b) sum of two dice rolled - seperate numbers

diceOnee = random.randint(1,6)
diceTwo = random.randint(1,6)

sumOfDiceOneTwo = diceOnee + diceTwo
print("The sum of two seperate dies are:", sumOfDiceOneTwo)

#c) - first senario: only chance of generating one value, the second chance generating 2 values

#2) *** Exercise 2: Floating Point ***

#generate a number between 0 and 1 inclusive
randomFloat = random.random()
print(randomFloat)

#a) point between 5 and 15
randomFiveFloat = 5
while randomFiveFloat >= 5:
    randomFiveFloat = 15*random.random() #generates float between 0 and 15
    if randomFiveFloat >= 5:
        print(randomFiveFloat)
        break
    else:
        randomFiveFloat = 5 #If number is equal to or less than 5, resets to 5 

#b) tax rate - between 10 to 20%
randomTax = 10
item = float(input("Enter the price of an item: "))
             
while randomTax >= 10:
    randomTax = 20*random.random()
    if randomTax >= 10:
        itemTax = item - (item * (randomTax/100))
        print("The cost of the item with a tax of", str(round(itemTax, 2)) + "%", "is $", round(itemTax, 2))
        break
    else:
        randomTax = 10

#c) comparing letters in name

letterOne = random.choice("NATASHA")
print(letterOne)
letterTwo = random.choice("NATASHA")
print(letterTwo)
letters = True

while letters == True:
    if letterOne == letterTwo:
        print("The same letters chosen are,", letterOne)
        letters = False
    if letterOne != letterTwo:
        print("The letters are not the same.")
        break


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

randomOne = random.choice(alphabet)
randomTwo = random.choice(alphabet)
randomThree = random.choice(alphabet)

counter = 0
if randomOne == "A" or randomOne == "I" or randomOne == "E" or randomOne == "I" or randomOne == "O":
    counter += 1
    print("1", counter)

if randomTwo == "A" or randomTwo == "I" or randomTwo == "E" or randomTwo == "I" or randomTwo == "O":
    counter += 1
    print("2", counter)


if randomThree == "A" or randomThree == "I" or randomThree == "E" or randomThree == "I" or randomThree == "O":
    counter += 1
    print(counter)


if counter == 2:
    print("There are two letters selected that are vowels.")
    count = False
    
elif counter == 3:
    print("There are three letters selected that are vowels")
    count = True
else:
    print("There are zero or one letter that is a vowel.")
    count = True

#***Exercise 3 - Coin Flip***
'''
heads = 0
tail = 0

changes = 0
headCount = 0
tailCount = 0
previous = "a"

consecutiveHeads = 0
consecutiveTails = 0

for i in range(1,21):
    coinFlip = random.choice("HT")
    print(coinFlip)
    if coinFlip == "H":
        heads += 1
#*** A) Number of heads flipped ***
#print("The number of heads is,", heads)


#*** B) Changes in Sequence ***
for i in range(20):
    coinFlip = random.choice("HT")
    newCoin = coinFlip
    if coinFlip == "H":
        previous == "H"
        headCount += 1

    if coinFlip == "T":
        previous = "T"
        tailCount += 1
        
    if previous != newCoin:
        changes += 1
         
print("Head count is", headCount)
print("Tail count is", tailCount)
print("The number of changes are", changes)



    

    
        
        
    









        
        
        


