'''
Rand Hasan
Assignment: Etch-a-Sketch
This program displays a functioning Etch-a-Sketch
'''
import pygame
import sys #used to close window after program ends

#initialize pygame
pygame.init()

w = 640
h = 480
size = (w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Rand's Etch-A-Sketch")

#color constants
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 175, 0)
BLUE = (0, 0, 255)
LTGREEN = (67, 189, 56)
CYAN = (89, 212, 234)
YELLOW = (255, 255, 0)
GREY = (40,40,40)
RED = (255,0,0)
GOLD = (249,166,2)
PURPLE = (164,66,220)
clock = pygame.time.Clock()
etch_screen1 = pygame.Rect(9/100*w,1/12*h,33/40*w,7/10*h)

def drawScreen():
    #draws the etch-A-sketch board
    surface.fill(RED)
    etch_screen = pygame.draw.rect(surface, WHITE, (9/100*w,1/12*h,33/40*w,7/10*h),0)
    pygame.draw.ellipse(surface, GOLD, (1/64*w,19/24*h,1/7*w,1/7*w),0)
    pygame.draw.ellipse(surface, GOLD, (54/64*w,19/24*h,1/7*w,1/7*w),0)
    logo = pygame.image.load("etch.gif")
    surface.blit(logo,[2*w/7,3/4*h])
    
    
def moveBrush(keys,x,y):
    #this moves the brush
    if keys[pygame.K_RIGHT] == True and x<(7.9/100+33/40)*w:
        x+= 1
    if keys[pygame.K_LEFT] == True and x>9/100*w:
        x-= 1
    if keys[pygame.K_UP] == True and y>1/12*h:
        y -= 1
    if keys[pygame.K_DOWN] == True and y<7.7/10*h:
        y += 1
    return x,y
    
def drawBrush(brush_startx,brush_starty,color):
    pygame.draw.ellipse(surface, color, (brush_startx,brush_starty,1/90*w,1/90*w),0)
    
def getColorChoice(event,color):  
    if event.key == pygame.K_1:
        return RED
    if event.key == pygame.K_2:
        return GREEN
    if event.key == pygame.K_3:
        return CYAN
    if event.key == pygame.K_4:
        return YELLOW
    if event.key == pygame.K_5:
        return BLUE 
    if event.key == pygame.K_6:
        return PURPLE
    return color
    
#------------Main Program Loop-------------
def main():
    brush_startx = etch_screen1.centerx
    brush_starty = etch_screen1.centery  
    color = BLACK
    drawScreen()
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                color = getColorChoice(event,color)
                
        keys = pygame.key.get_pressed()
        brush_startx, brush_starty = moveBrush(keys,brush_startx,brush_starty)
        if keys[pygame.K_SPACE]:
            #redraws background
            drawScreen()
            brush_startx = etch_screen1.centerx
        
            brush_starty = etch_screen1.centery
            color = BLACK

        #drawing code goes here
        drawBrush(brush_startx,brush_starty,color)

        #don't forget - update
        pygame.display.update()
        clock.tick(60)
main()
