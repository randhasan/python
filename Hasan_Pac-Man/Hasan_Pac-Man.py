'''
Rand Hasan
Pac-Man Program
Description: This is a program of the game Pac-Man
'''

import pygame, sys, math, random

#initialize game engine
pygame.init()

#Set up drawing surface
w = 600
h = 500
mazexu = w/30
mazeyu = h/25
size=(w,h)
surface = pygame.display.set_mode(size)

#set window title bar
pygame.display.set_caption("Pac-Man")

#Color constants
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED =   (255,  0,  0)
GREEN = (  0,255,  0)
BLUE =  (  0,  0,255)

#pac-man icon
pacManImageR = pygame.image.load('pacManR.png')
pacManImageL = pygame.image.load('pacManL.png')
pacManImageU = pygame.image.load('pacManU.png')
pacManImageD = pygame.image.load('pacManD.png')
pacManRect = pygame.Rect(11*mazexu,16.2*mazeyu,10,12)

logo = pygame.image.load('Pac-ManLogo.png')
logoBounds = pygame.Rect(mazexu*10.1,mazeyu*.2,200,52)
foodImage = pygame.image.load('food.png')

#initialize walls
borderWalls = [pygame.Rect(0,3*mazeyu,30*mazexu,1*mazeyu),pygame.Rect(0,3*mazeyu,1*mazexu,22*mazexu),pygame.Rect(0,24*mazeyu,30*mazexu,1*mazeyu),pygame.Rect(29*mazexu,3*mazeyu,1*mazexu,22*mazeyu)]
horzWalls = [pygame.Rect(2*mazexu,5*mazeyu,4*mazexu,1*mazeyu),pygame.Rect(7*mazexu,5*mazeyu,6*mazexu,1*mazeyu),pygame.Rect(14*mazexu,4*mazeyu,2*mazexu,2*mazeyu),pygame.Rect(17*mazexu,5*mazeyu,6*mazexu,1*mazeyu),pygame.Rect(24*mazexu,5*mazeyu,4*mazexu,1*mazeyu),pygame.Rect(2*mazexu,7*mazeyu,5*mazexu,1*mazeyu),pygame.Rect(10*mazexu,7*mazeyu,10*mazexu,1*mazeyu),pygame.Rect(14*mazexu,8*mazeyu,2*mazexu,2*mazeyu),pygame.Rect(23*mazexu,7*mazeyu,5*mazexu,1*mazeyu),pygame.Rect(mazexu*1,mazeyu*9,mazexu*6,mazeyu*2),pygame.Rect(mazexu*1,mazeyu*12,mazexu*6,mazeyu*2),pygame.Rect(23*mazexu,9*mazeyu,6*mazexu,2*mazeyu),pygame.Rect(23*mazexu,12*mazeyu,6*mazexu,2*mazeyu),pygame.Rect(7*mazexu,19*mazeyu,3*mazexu,2*mazeyu),pygame.Rect(20*mazexu,19*mazeyu,3*mazexu,2*mazeyu),pygame.Rect(11*mazexu,21*mazeyu,2*mazexu,2*mazeyu),pygame.Rect(14*mazexu,21*mazeyu,2*mazexu,2*mazeyu),pygame.Rect(17*mazexu,21*mazeyu,2*mazexu,2*mazeyu),pygame.Rect(20*mazexu,22*mazeyu,3*mazexu,1*mazeyu),pygame.Rect(7*mazexu,22*mazeyu,3*mazexu,1*mazeyu),pygame.Rect(2*mazexu,21*mazeyu,4*mazexu,2*mazeyu),pygame.Rect(24*mazexu,21*mazeyu,4*mazexu,2*mazeyu),pygame.Rect(2*mazexu,19*mazeyu,2*mazexu,2*mazeyu),pygame.Rect(26*mazexu,19*mazeyu,2*mazexu,2*mazeyu),pygame.Rect(10*mazexu,11*mazeyu,2*mazexu,1*mazeyu),pygame.Rect(18*mazexu,11*mazeyu,2*mazexu,1*mazeyu),pygame.Rect(5*mazexu,15*mazeyu,4*mazexu,1*mazeyu),pygame.Rect(21*mazexu,15*mazeyu,4*mazexu,1*mazeyu),pygame.Rect(14*mazexu,13*mazeyu,2*mazexu,2*mazeyu),pygame.Rect(8*mazexu,13*mazeyu,5*mazexu,1*mazeyu),pygame.Rect(17*mazexu,13*mazeyu,5*mazexu,1*mazeyu),pygame.Rect(8*mazexu,12*mazeyu,1*mazexu,1*mazeyu),pygame.Rect(21*mazexu,12*mazeyu,1*mazexu,1*mazeyu),pygame.Rect(10*mazexu,15*mazeyu,10*mazexu,1*mazeyu),pygame.Rect(13*mazexu,18*mazeyu,4*mazexu,2*mazeyu),pygame.Rect(11*mazexu,17*mazeyu,8*mazexu,1*mazeyu),pygame.Rect(5*mazexu,17*mazeyu,5*mazexu,1*mazeyu),pygame.Rect(20*mazexu,17*mazeyu,5*mazexu,1*mazeyu),pygame.Rect(9*mazexu,9*mazeyu,4*mazexu,1*mazeyu),pygame.Rect(17*mazexu,9*mazeyu,4*mazexu,1*mazeyu)]
vertWalls = [pygame.Rect(2*mazexu,15*mazeyu,2*mazexu,3*mazeyu),pygame.Rect(26*mazexu,15*mazeyu,2*mazexu,3*mazeyu),pygame.Rect(8*mazexu,7*mazeyu,1*mazexu,4*mazeyu),pygame.Rect(21*mazexu,7*mazeyu,1*mazexu,4*mazeyu),pygame.Rect(5*mazexu,18*mazeyu,1*mazexu,2*mazeyu),pygame.Rect(11*mazexu,18*mazeyu,1*mazexu,2*mazeyu),pygame.Rect(18*mazexu,18*mazeyu,1*mazexu,2*mazeyu),pygame.Rect(24*mazexu,18*mazeyu,1*mazexu,2*mazeyu)]
centerRect = pygame.Rect(13*mazexu,11*mazeyu,4*mazexu,1*mazeyu)
topRect = pygame.Rect(0,0,30*mazexu,3*mazeyu)

#speed, time and sound variables
SPEED = 2
pygame.time.set_timer(pygame.USEREVENT,1000)
#----------Main Program Loop ----------
def drawScreen(foodList,userPoints,pacManImage,keys,seconds,gameOver,userWins,level):
    surface.blit(logo,logoBounds)
    drawMaze()
    for foodRect in foodList:
        surface.blit(foodImage,foodRect) 
    pacManImage = movePacMan(keys)
    surface.blit(pacManImage,pacManRect)
    timeLeftText, timeLeftBounds = showMessage(str(seconds),20,2*w/50,h/26,WHITE,BLACK)
    surface.blit(timeLeftText, timeLeftBounds)   
    levelText, levelBounds = showMessage("Level: "+str(level),20,8*w/50,h/26,WHITE,BLACK)
    surface.blit(levelText, levelBounds)     
    if userWins==True:
        userWinsText, userWinsBounds = showMessage("You Win!",30,w/2,h/2,GREEN,BLACK)
        nextLevelText, nextLevelBounds = showMessage("Press space to move onto the next level",20,w/2,3*h/5,WHITE,BLACK)
        startOverText, startOverBounds = showMessage("Press enter to start over",20,w/2,3.5*h/5,WHITE,BLACK)
        surface.blit(userWinsText, userWinsBounds)
        surface.blit(nextLevelText, nextLevelBounds)
        surface.blit(startOverText, startOverBounds)
        gameOver = True
    if userWins == False and gameOver == True:
        userLosesText, userLosesBounds = showMessage("You Lose!",30,w/2,h/2,RED,BLACK)
        playAgainText, playAgainBounds = showMessage("Press enter to start over",20,w/2,3*h/5,WHITE,BLACK)
        surface.blit(userLosesText, userLosesBounds)
        surface.blit(playAgainText, playAgainBounds)  
        gameOver = True    
    userPoints = eatFood(foodList,userPoints)
    pointsText, pointsBound = showMessage("Points: "+str(userPoints),20,44*w/50,h/26,WHITE,BLACK)
    surface.blit(pointsText, pointsBound)    
    return userPoints

def drawMaze():
    pygame.draw.rect(surface,WHITE,centerRect,3)
    pygame.draw.rect(surface,BLACK,topRect,3)    
    for i in range(len(borderWalls)):
        pygame.draw.rect(surface,BLUE,borderWalls[i],3)
        i += 1
    for i in range(len(horzWalls)):
        pygame.draw.rect(surface,BLUE,horzWalls[i],3)
        i += 1  
    for i in range(len(vertWalls)):
        pygame.draw.rect(surface,BLUE,vertWalls[i],3)
        i += 1  
        
def placeFood():
    foodList = []
    while len(foodList)<50:
        x = random.randint(0,w-18)
        y = random.randint(0,h-18)    
        foodRect = pygame.Rect(x,y,18,18)
        foodList.append(foodRect)
        for i in foodList: 
            collide = collidesWithWall(i)
            if collide == True or foodRect.colliderect(centerRect):
                foodList.remove(foodRect)
                x = random.randint(0,w-18)
                y = random.randint(0,h-18)    
                foodRect = pygame.Rect(x,y,18,18)
                collide = collidesWithWall(i)             
    return foodList    
    
def movePacMan(keys):
    pacManImage = pacManImageR
    if keys[pygame.K_LEFT]:
        pacManRect.left -= SPEED
        pacManImage = pacManImageL
    if keys[pygame.K_RIGHT]:
        pacManRect.left += SPEED
        pacManImage = pacManImageR
    if keys[pygame.K_UP]:
        pacManRect.top -= SPEED
        pacManImage = pacManImageU
    if keys[pygame.K_DOWN]:
        pacManRect.top += SPEED
        pacManImage = pacManImageD
    pacManCollides(keys)
    return pacManImage
    
def collidesWithWall(aRect):
    collide = False
    for wall in borderWalls:
        if aRect.colliderect(wall):
            collide = True
    for wall in horzWalls:
        if aRect.colliderect(wall):
            collide = True
    for wall in vertWalls:
        if aRect.colliderect(wall):
            collide = True
    if aRect.colliderect(topRect):
        collide = True
    return collide

def pacManCollides(keys): 
    collide = collidesWithWall(pacManRect)
    if collide == True:
        for wall in borderWalls:
            if pacManRect.colliderect(wall):
                if keys[pygame.K_RIGHT]:
                    pacManRect.left -= SPEED
                if keys[pygame.K_LEFT]:
                    pacManRect.right += SPEED
                if keys[pygame.K_UP]:
                    pacManRect.top += SPEED
                if keys[pygame.K_DOWN]:
                    pacManRect.bottom -= SPEED
        for wall in horzWalls:
            if pacManRect.colliderect(wall):
                if keys[pygame.K_RIGHT]:
                    pacManRect.left -= SPEED
                if keys[pygame.K_LEFT]:
                    pacManRect.right += SPEED
                if keys[pygame.K_UP]:
                    pacManRect.top += SPEED
                if keys[pygame.K_DOWN]:
                    pacManRect.bottom -= SPEED
        for wall in vertWalls:
            if pacManRect.colliderect(wall): 
                if keys[pygame.K_RIGHT]:
                    pacManRect.left -= SPEED
                if keys[pygame.K_LEFT]:
                    pacManRect.right += SPEED
                if keys[pygame.K_UP]:
                    pacManRect.top += SPEED
                if keys[pygame.K_DOWN]:
                    pacManRect.bottom -= SPEED
        if pacManRect.colliderect(topRect):
            if keys[pygame.K_RIGHT]:
                pacManRect.left -= SPEED
            if keys[pygame.K_LEFT]:
                pacManRect.right += SPEED
            if keys[pygame.K_UP]:
                pacManRect.top += SPEED
            if keys[pygame.K_DOWN]:
                pacManRect.bottom -= SPEED 
                            
def eatFood(foodList,userPoints):
    for foodRect in foodList:
        if foodRect.colliderect(pacManRect):
            userPoints += 10
            foodList.remove(foodRect)
    return userPoints
                    
def showMessage(message,size,x,y,color,bg=None):
    font = pygame.font.SysFont("Arial",size,True,False)
    text = font.render(message,True,color,bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text,textBounds                    
    
def main():
    collide = False
    gameOver = False
    foodList = placeFood()
    userPoints = 0
    pacManImage = pacManImageR
    seconds = 100
    secondsList = [100,90,80,70,60,50,40,30,20,10]
    userWins = False
    level = 1
    num = 0
    
    while(True):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()              
                
            if event.type == pygame.KEYDOWN and event.key==pygame.K_RETURN and gameOver==True and userWins == False:
                pacManRect.topleft = (11*mazexu,16.2*mazeyu)
                collide = False
                gameOver = False
                foodList = placeFood()
                userPoints = 0
                pacManImage = pacManImageR
                seconds = 100
                userWins = False
                level = 1
            if event.type == pygame.KEYDOWN and event.key==pygame.K_RETURN and gameOver==True and userWins == True:
                pacManRect.topleft = (11*mazexu,16.2*mazeyu)
                collide = False
                gameOver = False
                foodList = placeFood()
                userPoints = 0
                pacManImage = pacManImageR
                seconds = 100
                userWins = False
                level = 1
                
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE and gameOver==True and userWins == True:
                num+=1
                collide = False
                gameOver = False
                foodList = placeFood()
                pacManImage = pacManImageR
                seconds = secondsList[num]
                userWins = False
                level += 1  
                pacManRect.topleft = (11*mazexu,16.2*mazeyu)

            if event.type == pygame.USEREVENT and seconds>0 and gameOver == False:
                seconds -= 1              
                
        # game logic goes here
        if gameOver!=True:
            movePacMan(keys)
            collide = collidesWithWall(pacManRect)
        if gameOver == True:
            pacManRect.topleft = (11*mazexu,16.2*mazeyu)
        if len(foodList)==0 and seconds!=0 and pacManRect.colliderect(centerRect):
            userWins = True
            gameOver = True
        if (len(foodList)!=0 or not pacManRect.colliderect(centerRect)) and seconds==0:
            gameOver = True
        if len(foodList)!=0:
            if pacManRect.colliderect(centerRect): 
                collide = True
                if keys[pygame.K_RIGHT]:
                    pacManRect.left -= SPEED*2
                if keys[pygame.K_LEFT]:
                    pacManRect.right += SPEED*2
                if keys[pygame.K_UP]:
                    pacManRect.top += SPEED*2
                if keys[pygame.K_DOWN]:
                    pacManRect.bottom -= SPEED*2        

        # set background fill
        surface.fill(BLACK)
        
        # drawing code goes here
        userPoints = drawScreen(foodList,userPoints,pacManImage,keys,seconds,gameOver,userWins,level)
        
        pygame.display.update()
main()