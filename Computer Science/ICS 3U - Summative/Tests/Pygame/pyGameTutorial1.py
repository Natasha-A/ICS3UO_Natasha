#Py-Game Tutorial - Basic Movements and Key presses
import pygame

#always call first
pygame.init()

#creating a window
window = pygame.display.set_mode((500,500)) #set length and width (can be anything)

#creating a name for the window
pygame.display.set_caption("First Game")

#Creating a character - having attributes
x = 50
y = 50
width = 40
height = 60
vel = 5

#all pygames have main loop - to check for main events (actions, collisions, mouse events)
run = True
while run:
    #creates a 'clock' time delay so doesn't run too fast
    pygame.time.delay(100) #0.1 second delay

    #QUITING
    #to check for events, need a for loop (get's position of all events):
    for event in pygame.event.get():
        #check if they have occured, and if so, run specific code.

        #if they press the 'red' quit button, stop code from running
        if event.type == pygame.QUIT:
            run = False


    #CHARACTER
    window.fill((0,0,0)) #sets to black window fill - prevents againt repeting object display
    #can also use .circle(), .polygon, etc.
    pygame.draw.rect(window, (255, 0, 0), (x,y, width, height)) #'win' taken as first parameter to create a surface
    #2nd parameter is RGB colour, third is position(50,50) and dimensions(40,60)

    #need to tell it to display program
    pygame.display.update()

    #MOVING CHARACTER - telling how to move repeatedly
    keys = pygame.key.get_pressed()

    #events for key pressed
    if keys[pygame.K_LEFT]:
        #starts from left upper corner
        x -= vel #moves left at constant velocity of 5
        
    if keys[pygame.K_RIGHT]:
        x += vel #right

    if keys[pygame.K_UP]:
        y -= vel #up 

    if keys[pygame.K_DOWN]:
        y += vel #down

    
    
pygame.quit() #end the program and closes the window (prevents against errors)


    
