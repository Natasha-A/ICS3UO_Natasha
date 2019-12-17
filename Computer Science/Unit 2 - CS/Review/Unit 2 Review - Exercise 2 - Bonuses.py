#Unit 2 Review - Exercise 2 - BONUS AMOUNT

conesSold = int(input("Number of cones sold per week: "))

if conesSold > 150:
    if conesSold >= 151: #Culimintates, so no restrictions needed for range
        firstBonus = 10 + (conesSold * 0.10)
        bonus = True
        totalBonus = firstBonus
    if conesSold > 250:
        secondBonus = conesSold * 0.25
        bonus = True
        totalBonus = firstBonus + secondBonus
    if conesSold > 350:
        thirdBonus = conesSold * 0.35
        bonus = True
        totalBonus = firstBonus + secondBonus + thirdBonus
else:
    print("You will not recieve a bonus.")
    bonus = False
    firstBonus = False
    secondBonus = False
    thirdBonus = False

if bonus == True:
        print("You wil recieve a bonus of", "$" + str(totalBonus), "dollars")

        
        
