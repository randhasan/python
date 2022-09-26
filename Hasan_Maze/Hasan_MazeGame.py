'''
Rand Hasan
This program displays a unique maze with rectangles
'''
import pygame, random
import sys #used to close window after program ends

#initialize pygame
pygame.init()

w = 1000
h = int(36/48*w)
mazew = w
mazeh = h
mazexu = mazew/48
mazeyu = mazeh/36
size = (w,h)
surface = pygame.display.set_mode(size)
pygame.display.set_caption("Rand's Maze Program")

#color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,225)

#player icon
avatarRect = pygame.Rect(w/18,h/15,23,42)
avatarImage = pygame.image.load('avatar.png')

#gem images
redGem = pygame.image.load('redGem.png')
orangeGem = pygame.image.load('orangeGem.png')
yellowGem = pygame.image.load('yellowGem.png')
greenGem = pygame.image.load('greenGem.png')
tealGem = pygame.image.load('tealGem.png')
blueGem = pygame.image.load('blueGem.png')
purpleGem = pygame.image.load('purpleGem.png')
whiteGem = pygame.image.load('whiteGem.png')
blackGem = pygame.image.load('blackGem.png')
gems = [redGem,orangeGem,yellowGem,greenGem,tealGem,blueGem,purpleGem,whiteGem,blackGem]

#initialize walls
borderWalls = [pygame.Rect(0,0,48*mazexu,2*mazeyu),pygame.Rect(0*mazexu,34*mazeyu,22*mazexu,3*mazeyu),pygame.Rect(24*mazexu,34*mazeyu,22*mazexu,3*mazeyu),pygame.Rect(0,0,2*mazexu,36*mazeyu),pygame.Rect(46*mazexu,0,3*mazexu,36*mazeyu)]
horzWalls = [pygame.Rect(2*mazexu,5*mazeyu,11*mazexu,2*mazeyu),pygame.Rect(5*mazexu,10*mazeyu,13*mazexu,2*mazeyu),pygame.Rect(2*mazexu,15*mazeyu,6*mazexu,2*mazeyu),pygame.Rect(2*mazexu,20*mazeyu,11*mazexu,2*mazeyu),pygame.Rect(5*mazexu,29*mazeyu,8*mazexu,2*mazeyu),pygame.Rect(16*mazexu,29*mazeyu,7*mazexu,2*mazeyu),pygame.Rect(22.5*mazexu,28*mazeyu,4*mazexu,2*mazeyu),pygame.Rect(21*mazexu,5*mazeyu,6*mazexu,2*mazeyu),pygame.Rect(21*mazexu,10.75*mazeyu,6*mazexu,2*mazeyu),pygame.Rect(21*mazexu,16*mazeyu,11*mazexu,2*mazeyu),pygame.Rect(27.5*mazexu,26*mazeyu,5*mazexu,2*mazeyu),pygame.Rect(16*mazexu,23*mazeyu,7*mazexu,2*mazeyu),pygame.Rect(35*mazexu,5*mazeyu,8*mazexu,2*mazeyu),pygame.Rect(40.5*mazexu,10*mazeyu,6*mazexu,2*mazeyu),pygame.Rect(40.5*mazexu,15*mazeyu,6*mazexu,2*mazeyu),pygame.Rect(28*mazexu,32.5*mazeyu,8.5*mazexu,2*mazeyu),pygame.Rect(26*mazexu,21*mazeyu,17*mazexu,2*mazeyu)]
vertWalls = [pygame.Rect(16*mazexu,2*mazeyu,2*mazexu,10*mazeyu),pygame.Rect(11*mazexu,15*mazeyu,2*mazexu,7*mazeyu),pygame.Rect(5*mazexu,25*mazeyu,2*mazexu,6*mazeyu),pygame.Rect(11*mazexu,25*mazeyu,2*mazexu,11*mazeyu),pygame.Rect(21*mazexu,5*mazeyu,2*mazexu,13*mazeyu),pygame.Rect(30*mazexu,0,2*mazexu,17*mazeyu),pygame.Rect(16*mazexu,27.75*mazeyu,2*mazexu,3*mazeyu),pygame.Rect(18*mazexu,30*mazeyu,2*mazexu,6*mazeyu),pygame.Rect(16*mazexu,15*mazeyu,2*mazexu,10*mazeyu),pygame.Rect(21*mazexu,23*mazeyu,2*mazexu,8*mazeyu),pygame.Rect(26*mazexu,21*mazeyu,2*mazexu,9*mazeyu),pygame.Rect(31*mazexu,26*mazeyu,2*mazexu,3*mazeyu),pygame.Rect(36*mazexu,26*mazeyu,2*mazexu,10*mazeyu),pygame.Rect(35*mazexu,12*mazeyu,2*mazexu,10*mazeyu),pygame.Rect(41*mazexu,21*mazeyu,2*mazexu,10*mazeyu)]
exitRect = pygame.Rect(22*mazexu,34*mazeyu,2.1*mazexu,3*mazeyu)

#set speed, sound and time variables
SPEED = 10
sound1 = pygame.mixer.Sound('sound1.wav')
sound2 = pygame.mixer.Sound('sound2.wav')
sound3 = pygame.mixer.Sound('sound3.wav')
sound4 = pygame.mixer.Sound('sound4.wav')
sound5 = pygame.mixer.Sound('sound5.wav')
sound6 = pygame.mixer.Sound('sound6.wav')
sound8 = pygame.mixer.Sound('sound8.wav')
sound9 = pygame.mixer.Sound('sound9.wav')
pygame.time.set_timer(pygame.USEREVENT,1000)
#------------Main Program Loop-------------   
'''
The drawScreen function displays the maze, as well as the avatar image and bounding box, text for when the user wins or loses,
user points, the time the user has remaining and the gem images and bounding boxes.
'''

def drawScreen(gemList,userWins,seconds,gameOver,gem,userPoints):
    drawMaze() #displays maze border and walls
    for gemRect in gemList:
        surface.blit(gem,gemRect)
    surface.blit(avatarImage,avatarRect)
    timeLeftText, timeLeftBounds = showMessage(str(seconds),30,48*w/50,h/35,WHITE,BLACK)
    surface.blit(timeLeftText, timeLeftBounds)    
    if userWins==True: #user wins
        userWinsText, userWinsBounds = showMessage("You Win!",30,w/2,h/2,GREEN,BLACK)
        playAgainText, playAgainBounds = showMessage("Press enter to play again",30,w/2,3*h/5,GREEN,BLACK)
        surface.blit(playAgainText, playAgainBounds)
        surface.blit(userWinsText, userWinsBounds)
        gameOver = True
    if userWins == False and gameOver == True: #user loses
        userLosesText, userLosesBounds = showMessage("You Lose!",40,w/2,h/2,RED,BLACK)
        playAgainText, playAgainBounds = showMessage("Press enter to play again",30,w/2,3*h/5,RED,BLACK)
        surface.blit(userLosesText, userLosesBounds)
        surface.blit(playAgainText, playAgainBounds)  
        gameOver = True
    userPoints = collectGems(gemList,gem,userPoints)
    pointsText, pointsBound = showMessage(str(userPoints),30,44*w/50,h/35,WHITE,BLACK)
    surface.blit(pointsText, pointsBound)
    return userPoints

'''
The chooseGem function chooses a gem from a list of different gems, each set of gems are worth a different number of points.
'''

def chooseGems():
    gem = random.choice(gems)
    return gem

'''
The drawMaze function displays all of rectangles that make up the walls of the maze.
'''

def drawMaze():
    #draws border walls
    for i in range(len(borderWalls)):
        pygame.draw.rect(surface,BLACK,borderWalls[i],0)
        i += 1
    #draws horizontal walls
    for i in range(len(horzWalls)):
        pygame.draw.rect(surface,BLACK,horzWalls[i],0)
        i += 1    
    #draws vertical walls
    for i in range(len(vertWalls)):
        pygame.draw.rect(surface,BLACK,vertWalls[i],0)
        i += 1    
    pygame.draw.rect(surface,RED,exitRect,0)
    
'''
The movePlayer function moves the avatar image's bounding box as a result of the user input (the keys they click.)
'''
    
def movePlayer(keys):
    if keys[pygame.K_LEFT]:
        avatarRect.left -= SPEED
    if keys[pygame.K_RIGHT]:
        avatarRect.left += SPEED
    if keys[pygame.K_UP]:
        avatarRect.top -= SPEED
    if keys[pygame.K_DOWN]:
        avatarRect.top += SPEED
    playerCollide(keys)
    
'''
As the avatar image's bounding box collides with a gem image's bounding box, they are awarded points based on the color of the
set of gems.  The gem is also removed from the list and is not longer blitted onto the screen.  Additionally, a different sound is played
for each set of gems.
'''
    
def collectGems(gemList,gem,userPoints):
    for gemRect in gemList:
        if gemRect.colliderect(avatarRect):
            if gem == redGem:
                sound1.play()
                userPoints += 1
            if gem == orangeGem:
                sound2.play()
                userPoints += 2
            if gem == yellowGem:
                sound3.play()
                userPoints += 3
            if gem == greenGem:
                sound4.play()
                userPoints += 4
            if gem == tealGem:
                sound5.play()
                userPoints += 5
            if gem == blueGem:
                sound6.play()
                userPoints += 6
            if gem == whiteGem:
                sound8.play()
                userPoints += 8
            if gem == blackGem:
                sound9.play()
                userPoints += 9 
            gemList.remove(gemRect)
    return userPoints

'''
If a bounding box object collides with another bounding box object, the collide variable is set to True.
'''
                
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
    return collide

'''
If collide is true, the avatar image's bounding box will not be able to go across a border or wall.
'''
                
def playerCollide(keys):
    collide = collidesWithWall(avatarRect)
    if collide == True:
        for wall in borderWalls:
            if avatarRect.colliderect(wall):
                if keys[pygame.K_RIGHT]:
                    avatarRect.left -= SPEED
                if keys[pygame.K_LEFT]:
                    avatarRect.right += SPEED
                if keys[pygame.K_UP]:
                    avatarRect.top += SPEED
                if keys[pygame.K_DOWN]:
                    avatarRect.bottom -= SPEED       
        for wall in horzWalls:
            if avatarRect.colliderect(wall):
                if keys[pygame.K_RIGHT]:
                    avatarRect.left -= SPEED
                if keys[pygame.K_LEFT]:
                    avatarRect.right += SPEED
                if keys[pygame.K_UP]:
                    avatarRect.top += SPEED
                if keys[pygame.K_DOWN]:
                    avatarRect.bottom -= SPEED
        for wall in vertWalls:
            if avatarRect.colliderect(wall): 
                if keys[pygame.K_RIGHT]:
                    avatarRect.left -= SPEED
                if keys[pygame.K_LEFT]:
                    avatarRect.right += SPEED
                if keys[pygame.K_UP]:
                    avatarRect.top += SPEED
                if keys[pygame.K_DOWN]:
                    avatarRect.bottom -= SPEED 
                    
'''
Five gems are blitted onto the screen each game.  The placeGems function randomly chooses locations for each of the gems.
If the location of a gem image's bounding box would cause a collision between the bounding box and a wall, the gem is removed from the list
and replaced until a bounding box that doesn't collide with any walls is added to the list.
'''                   

def placeGems():
    gemList = []
    while len(gemList)<5:
        x = random.randint(0,w-40)
        y = random.randint(0,h-40)    
        gemRect = pygame.Rect(x,y,40,40)
        gemList.append(gemRect)
        for i in gemList: 
            collide = collidesWithWall(i)
            if collide == True or gemRect.colliderect(exitRect):
                #if a gem image's bounding box collides with a wall or the exit rectangle, it will be replaced.
                gemList.remove(gemRect)
                x = random.randint(0,w-40)
                y = random.randint(0,h-40)
                gemRect = pygame.Rect(x,y,40,40)
                collide = collidesWithWall(i)    
    return gemList

'''
The showMessage function is a function that was commonly used in our previous programs.
It is used to make text that will later be blitted onto the screen.
'''

def showMessage(message,size,x,y,color,bg=None):
    font = pygame.font.SysFont("Arial",size,True,False)
    text = font.render(message,True,color,bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text,textBounds
    
def main():
    collide = False #no collisions at the beginning of the game
    seconds = 60 #user has a minute to collect all of the gems and make it to the exit block.
    gem = chooseGems() #set of gems is chosen
    gemList = placeGems() #location of gem image's bounding boxes will be chosen
    gameOver = False 
    userWins = False
    userPoints = 0 #user starts with 0 points
    
    while(True):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN and event.key==pygame.K_RETURN and gameOver==True:
                collide = False #if the game is over, the user can press the enter key to play again.  All variables are reinitialized.
                seconds = 60
                gem = chooseGems()
                gemList = placeGems()
                gameOver = False
                userWins = False
                userPoints = 0
                avatarRect.topleft = (w/18,h/15) #avatar image's bounding box is moved back to the starting position.
                
            if event.type == pygame.USEREVENT and seconds>0 and gameOver == False:
                seconds -= 1 #amount of time left decreases each second and stops decreasing once the time is equal to 0 seconds.
            
        #game logic goes here
        if not gameOver: # if the game isn't over the user can still move
            movePlayer(keys)
            collide = collidesWithWall(avatarRect)
        if len(gemList)==0 and seconds!=0 and avatarRect.colliderect(exitRect): #if the user has collected all gems, goes to the exit of the maze and still has time left, they win!
            userWins = True
            gameOver = True
        if (len(gemList)!=0 or (not avatarRect.colliderect(exitRect))) and seconds==0: #if the user doesn't collect all of the gems within one minute or doesn't make it to the exit of the maze before time runs out, they lose.
            gameOver = True
        if not (len(gemList)==0 and seconds!=0): #if the user collides with the exit of the maze and they haven't collected all of the gems, the game is sill in play.
            if avatarRect.colliderect(exitRect): 
                collide = True
                if keys[pygame.K_RIGHT]:
                    avatarRect.left -= SPEED
                if keys[pygame.K_LEFT]:
                    avatarRect.right += SPEED
                if keys[pygame.K_UP]:
                    avatarRect.top += SPEED
                if keys[pygame.K_DOWN]:
                    avatarRect.bottom -= SPEED           
        
        #drawing code goes here
        surface.fill(WHITE)
        userPoints = drawScreen(gemList,userWins,seconds,gameOver,gem,userPoints)

        #don't forget - update
        pygame.display.update()   
main()
