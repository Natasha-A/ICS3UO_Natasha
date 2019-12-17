#3.2 - Conditional Loop Lesson

#While loop is more general than for loop, eg:

#Steps: Set up variable - initalize, create counter, change value, print new value 
#Same to each other:
for count in range(10):
    print(count)

print("")

count2 = 0
while count2 < 10:
    print(count2)
    count2 = count2 + 1 


#Conditional Loops - code will be executed until one or more conditions are false, or runs when always true

# while age >= 16: condition continously checked until not meeting requirements

#Examples 2 and 3:
n = int(input("Please enter a number: "))
while n > 1:
    print(n)
    n /= 2 #same as n = n/2

n = 1
nsquared = 1
while nsquared < 1000:
    print(n, nsquared)
    n += 1 #multiple calcuations being performed and presented side by side
    nsquared = n**2

print("")
#Example 4
age = int(input("Your age? "))

while age < 18:
    print("Too young to vote! Next age!")
    age = int(input("Your age? "))

print("Old enough to vote.")

#Sentinels - processes data until special value reached (must be distingushable, not apart of data)
total = 0
numMarks = 0

mark = int(input("Enter mark: "))

while mark != -1:
    total += mark
    numMarks += 1
    mark = int(input("Enter mark: "))

    avg = total/(numMarks)
    print(avg)



x = 1
while (x > 0):
   x += 1
   print(x)
print("Done.")

    
