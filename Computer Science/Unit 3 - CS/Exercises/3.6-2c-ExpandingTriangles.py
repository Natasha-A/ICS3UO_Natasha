#3.6 - 2.c 

n = 4

'''
for x in range(1,4,2):
    print("*" * x) #Gets the one and three
for x in range(1,6,2):
    print("*" * x) #Gets the one and three and five
for x in range(1,8,2):
    print("*" * x) #Gets the one and three and five and eight 

simplifies to...
'''

for n in range(4,9,2): #get 4,6,8 as values
    for x in range(1,n,2):
        space = int(-x/2 + 3.5)
        print(" "* space + "*" * x)

'''

#  x  space (y)
#  -1  4
#  0   3.5
#  1   3
#  3   2
#  5   1
#  7   0
#  y = mx + b
#  space = -x/2 + 3.5  <---how much space needed
#To solve for equation - look at talke

___x
__xxx
___x
--xxx
_xxxxx
___x
--xxx
_xxxxx
xxxxxxx



'''

    
    
