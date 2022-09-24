'''
Rand Hasan
Period 11 HCP 10/5/2018
Assignment: pyGame Template
'''
import pygame, random
import sys #used to close winow after program ends

#initialize pygame
pygame.init()
background = pygame.image.load("space.png")

w = 600
h = 800
size = (w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Rand Hasan's Rocket Race")

redRocket = pygame.image.load("redRocket.png").convert_alpha()
blueRocket = pygame.image.load("blueRocket.png").convert_alpha()

#color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,225)
clock = pygame.time.Clock()

redRect = redRocket.get_rect()
blueRect = blueRocket.get_rect()

def initRockets():
    redRect.bottom = h
    redRect.centerx = w/4
    blueRect.bottom = h
    blueRect.centerx = 3*w/4
    
def getWinner(rocketChoice):
    if rocketChoice== None:
        return ""
    if redRect.top<blueRect.top and rocketChoice=="red":
        return "Red Wins! You Win!"
    elif redRect.top<blueRect.top and rocketChoice=="blue":
        return "Red Wins! You Lose!"
    elif blueRect.top<redRect.top and rocketChoice=="blue":
        return "Blue Wins! You Win!"
    elif blueRect.top<redRect.top and rocketChoice=="red":
        return "Blue Wins! You Lose!"
    elif blueRect.top==redRect.top:
        return "Tie! You Lose!"
            
def drawScreen(gameInPlay,rocketChoice):
    surface.blit(background,[0,0])
    surface.blit(redRocket,redRect)
    surface.blit(blueRocket,blueRect)
    if not gameInPlay:
        winner = getWinner(rocketChoice)
        winnerText, winnerBounds = showMessage(winner,40,w/2,3*h/5,WHITE) 
        chooseText, chooseBounds = showMessage("Choose a Rocket", 50, w/2, h/2.5, WHITE)
        redButtonText, redButtonBounds = showMessage("Choose Red Rocket", 25, w/4, 4*h/5, WHITE, RED)
        blueButtonText, blueButtonBounds = showMessage("Choose Blue Rocket", 25, 3*w/4, 4*h/5, WHITE, BLUE)        
        surface.blit(winnerText, winnerBounds)
        #blit all messages to the screen
        surface.blit(chooseText,chooseBounds)
        surface.blit(redButtonText, redButtonBounds)
        surface.blit(blueButtonText, blueButtonBounds)        
        
def showMessage(message,size,x,y,color,bg=None):
    font = pygame.font.SysFont("Consolas",size,True,False)
    text = font.render(message,True,color,bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text,textBounds

#------------Main Program Loop-------------
def main():
    initRockets()
    gameInPlay = False
    rocketChoice = None
    redButtonText, redButtonBounds = showMessage("Choose Red Rocket", 25, w/4, 4*h/5, WHITE, RED)  #use button bounds to check collisions with mouse 
    blueButtonText, blueButtonBounds = showMessage("Choose Blue Rocket", 25, 3*w/4, 4*h/5, WHITE, BLUE)
    mouseOver = False
    
    
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K._ESCAPE)):
                pygame.quit()
                sys.exit()
            if ( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if redButtonBounds.collidepoint(pygame.mouse.get_pos()):
                    rocketChoice = "red"
                    initRockets()
                    gameInPlay = True
                elif blueButtonBounds.collidepoint(pygame.mouse.get_pos()):
                    rocketChoice = "blue"
                    initRockets()
                    gameInPlay = True
           
        
        #game logic goes here
        if gameInPlay == True:
            redRect.top=redRect.top-random.randint(1,5)
            blueRect.top=blueRect.top-random.randint(1,5)
            if redRect.top<=0 or blueRect.top<=0:
                gameInPlay = False

        #drawing code goes here
        surface.fill(WHITE)
        drawScreen(gameInPlay, rocketChoice)
        
        #don't forget - update
        pygame.display.update()
        clock.tick(60)
        
main()