#looking for longest consecutive

while True:
    num = int(input("Enter a positive integer: "))
    #Example: 345 - able to work for ascending consective integers ( minus 1 to check) 
    previous = 2000 #assign any value that will not be true the first run 
    while num >= 1:
        digit = num % 10
        num = num // 10
        print(digit)

# to check if numbers are consecutive in ascending order ie) 345
        if (previous - digit) == 1:
            counter = counter + 1 #If the difference is 1, the numbers are consecutive, start counting the amount of consecutive number
        else:
            counter = 0 #resets counter, starts all over again in order to check for consective numbers

        if counter == 2: #was able to find consecutive between 2 changes, 3 integers ie) 5 - 4 = 1, 4 - 3 = 1
            print("There are three ascending consecutive integers.")


# to check if numbers are consecutive in descending order ie) 543
        if (previous - digit) == -1:
            descendingCounter += 1
        else:
            descendingCounter = 0

        if descendingCounter == 2:
            print("There are three descending consecutive integers.")

        previous = digit #*******assign previous right at the end, providing new digit




