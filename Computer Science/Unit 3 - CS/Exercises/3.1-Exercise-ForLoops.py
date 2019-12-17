#Exercise 3.1 - For Loops

#a)
for numbers in range(1,21): #need to extend stop value by one (start/finish/step)
    print(numbers)

#b)
print("")
for oddPosInt in range(50,0, 1):
    print(oddPosInt)

#c)
print("")
for name in range(0,21):
    print("Natasha \n")

#d)
print("")

timesNameDisplayed = int(input("Enter the number of times to print out the name: "))

for namePrinted in range(0,timesNameDisplayed):
    print("Natasha-Determined times by user \n")

#e) good example
for posIntegersUnderHundred in range(100,0,-10):
    print(posIntegersUnderHundred)

#f)
countdownTimer = int(input("Enter time to countdown to: "))
for countdown in range(countdownTimer,1,-1):
    print(countdown)
print("Blast off!")
'''
#g)
m = int(input("Enter the starting value: "))
n = int(input("Enter the ending value: "))
s = int(input("Enter the step count: "))

for userCount in range(m,n,s):
    print(userCount)
'''

#g) Revised using if/else to handle incorrect range parameters
m = int(input("Enter the starting value: "))
n = int(input("Enter the ending value: "))
s = int(input("Enter the step count: "))

'''
for userCount in range(m,n,s):
    print(userCount)
'''

if m < n:
    for userCount in range(m,n,s):
        print(userCount)
elif m > n:
    for userCount in range(n,m,s):
        print(userCount)
else:
    print("You have entered an incorrect step count")

    
    

