#4.3 - Returns - QUIZ
#** watch for order of stesp**
#following the trail of where functions are called, and prints called and returns of values that are computated 

def a(n): # 6) n = 7
    print(n+1) # 7) PRINTS: 8
    
    return (n-4) # 8) When a(7) called - returns 3 

def b(n): # 1) n = 6 
    print(n-1) # 2) PRINTS: 5 
    w = c(n-1) # 3) *Computates instance: c(6-1) = c(5) <--new n value*
    #(***c(5) is called and runs***)
    
    #will print (since main program runs):
    return (w+2) # 11) h (returned as) = 8, 8 + 2 = 10, therefore PRINTS: 10 

def c(n): # n = 5
    print(n+2) # 4) PRINTS: 7
    h = a(n+2) # 5) Computates instance: n = 5, a(5+2) = a(7) <-- new n value
    #(***a(7) is called and runs***)

    #9) h = a(5+2) = a(7) -> returns: 3

    return (h+5) # 10) returns: h = 8 

print(b(6)) #n = 6 


    
