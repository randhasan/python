'''
Rand Hasan
HCP
Assignment: Timer Example with Rotation
Description:Program to rotate a spiral while counting down from 10
'''

import pygame, sys, math,random

#initialize game engine
pygame.init()

#Set up drawing surface
w = 400
h = 400
size=(w,h)
surface = pygame.display.set_mode(size)

#set window title bar
pygame.display.set_caption("Count down")

#set up game timer
pygame.time.set_timer(pygame.USEREVENT,1000)

#load image
spiral = pygame.image.load("spiral.png").convert_alpha()


#Color constants
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED =   (255,  0,  0)
GREEN = (  0,255,  0)
BLUE =  (  0,  0,255)

def showMessage(words, size, font, x, y, color, bg = None):
    text_font = pygame.font.SysFont(font, size, True, False)
    text = text_font.render(words, True, color, bg)
    textBounds = text.get_rect()
    textBounds.center = (x, y)    
    
    #return bounding rectangle for click detection
    return text, textBounds
'''


'''
def drawScreen(seconds, degrees, spiral):
    if seconds>0:
        newSpiral = pygame.transform.rotate(spiral,degrees)
        newSpiralRect = newSpiral.get_rect()
        newSpiralRect.centerx = w/2
        newSpiralRect.centery = h/2        
        surface.blit(newSpiral,newSpiralRect)
    else:
        newSpiral = pygame.transform.scale(spiral,(2*w,2*h))
        newSpiralRect = newSpiral.get_rect()
        newSpiralRect.centerx = w/2
        newSpiralRect.centery = h/2        
        surface.blit(newSpiral,newSpiralRect)
        timeLeftText, timeLeftBounds = showMessage("Boom", 50, "Arial", w/2, h/2,RED,BLACK)
        surface.blit(timeLeftText, timeLeftBounds)
    
#----------Main Program Loop ----------
def main():
    
    #set up the model variables
    seconds = 10
    degrees = 0
    
    #main program loop
    while(True):
        for event in pygame.event.get():
            if( event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            
            # game logic goes here
            if event.type == pygame.USEREVENT and seconds>0:
                seconds -= 1
            
            if seconds == 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                seconds = 10
                degrees = 0
                pygame.time.set_timer(pygame.USEREVENT,1000)
        degrees += 5

        # set background fill
        surface.fill(WHITE)
        
        # drawing code goes here
        drawScreen(seconds,degrees, spiral)
       
        pygame.display.update()
main()