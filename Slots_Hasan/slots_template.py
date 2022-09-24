'''
Rand Hasan
Period 11
Honors Computer Programming
Assignment: Slots
Purpose: Allows players to bet in game credits on a slot game
'''

import pygame, sys, math, random

#initialize game engine
pygame.init()

#open and set window size
w = 380
h = 450
surface = pygame.display.set_mode((w, h))

#set title bar
pygame.display.set_caption("Slots")

#color constants
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)
YELLOW = (255, 255,   0)


#instantiate picture objects
slot_machine = pygame.image.load("slot_machine.png").convert_alpha()
seven_icon = pygame.image.load("7slot_icon.png").convert_alpha()
banana_icon = pygame.image.load("banana_icon.png").convert_alpha()
bar_icon = pygame.image.load("bar_icon.png").convert_alpha()
bell_icon = pygame.image.load("bell_icon.png").convert_alpha()
cherry_icon = pygame.image.load("cherry_icon.png").convert_alpha()
grape_icon = pygame.image.load("grape_icon.png").convert_alpha()
lemon_icon = pygame.image.load("lemon_icon.png").convert_alpha()
orange_icon = pygame.image.load("orange_icon.png").convert_alpha()
watermelon_icon = pygame.image.load("watermelon_icon.png").convert_alpha()

#instantiate picture objects for winning image and a transparent placeholder image
coin_image = pygame.image.load("bitcoin.png").convert_alpha()
placeholder_image = pygame.image.load("empty.png").convert_alpha()

#--------------------functions--------------------

def drawScene():
    surface.fill(WHITE)
    surface.blit(slot_machine, [0, 0])


#----------------main program loop----------------
def main():       
 
    # data initializations (model)
    
    
    
    
    #main program loop
    while(True):
        
        #controller code
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            #other single keypress events 
 
 
 
 
        #game logic statements here to change the model
            
        
        
        
        #draw the view
        drawScene()

  
  
  
        #updates screen
        pygame.display.update()
        
        
main()