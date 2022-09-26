'''
Rand Hasan
Description: This program runs the game of snake in which the user moves a snake around the board.
'''

import pygame, sys, math, random

#initialize game engine
pygame.init()

#Set up drawing surface
w = 500
h = 500
size=(w,h)
surface = pygame.display.set_mode(size)

#set window title bar
pygame.display.set_caption("Snake")

#Color constants
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED =   (255,  0,  0)
GREEN = (  0,255,  0)
BLUE =  (  0,  0,255)
YELLOW = (255, 255, 0)
DRK_GREEN = (19, 98, 7)
CYAN = (89, 212, 234)
PURPLE = (164,66,220)
colors = [[RED,"Red"],[YELLOW,"Yellow"],[DRK_GREEN,"Green"],[CYAN,"Cyan"],[PURPLE,"Purple"]] #list of colors that the user can choose their snake to be.

#Other constants
clock = pygame.time.Clock()
numRows,numCols = 20,20
eat = pygame.mixer.Sound('eat.wav') #sound that is played when the snake eats.

#----------Main Program Loop ----------
'''
The drawScreen function is the view of the program.  At the beginning of the game, text is blitted onto the screen to welcome the user and tells the
user to choose a color for their snake.  Once a color is chosen, the rest of the view is displayed. 
'''
def drawScreen(snakeBoard,gameOver,colorChosen,color):
    surface.fill(YELLOW) 
    if not colorChosen: #color has not been chosen
        pygame.draw.rect(surface,RED,(w/(numRows+2),h/(numCols+2),numRows*(w/(numRows+2)),numCols*(h/(numCols+2))),0)
        pygame.draw.rect(surface,BLACK,(w/(numRows+2),h/(numCols+2),numRows*(w/(numRows+2)),numCols*(h/(numCols+2))),2)  
        pygame.draw.rect(surface,BLACK,(0,0,w,h),3)
        welcomeText,welcomeBounds = showMessage("Welcome to the Snake Game!",30,w/2,h/5,WHITE,BLACK)
        surface.blit(welcomeText,welcomeBounds)
        chooseColorText, chooseColorBounds = showMessage("Choose a color for your snake.",20,w/2,h/3.5,WHITE,BLACK)
        surface.blit(chooseColorText, chooseColorBounds)
        a = 4
        for i in range(len(colors)): #buttons of different colors are drawn onto the screen and the user can choose the color of their snake by clicking one of them.
            pygame.draw.rect(surface,colors[i][0],(w/3,(a*h)/10,30,30),0)
            pygame.draw.rect(surface,BLACK,(w/3,(a*h)/10,30,30),3)
            colorText,colorBounds = showMessage(colors[i][1],20,w/2,((a*h)/10)+15,WHITE,BLACK)
            surface.blit(colorText,colorBounds)
            a+=1
        
    elif colorChosen: #when the color is chosen, the rest of the view is displayed
        x,y = w/(numRows+2),h/(numCols+2)
        for a in range (len(snakeBoard)):
            for b in range (len(snakeBoard)):
                pygame.draw.rect(surface,WHITE,(x,y,w/(numRows+1),h/(numCols+1)),0)
                if snakeBoard[a][b] > 0:
                    pygame.draw.ellipse(surface,color,(x,y,w/(numRows+1),h/(numCols+1)),0) #snake body
                    pygame.draw.ellipse(surface,BLACK,(x,y,w/(numRows+1),h/(numCols+1)),2) #outline to make the snake body look nicer
                if snakeBoard[a][b] < 0:
                    pygame.draw.ellipse(surface,GREEN,(x,y,w/(numRows+1),h/(numCols+1)),0) #food
                    pygame.draw.ellipse(surface,BLACK,(x,y,w/(numRows+1),h/(numCols+1)),2) #outline for food
                x+= w/(numRows+2)
            x = w/(numRows+2)
            y+=h/(numCols+2)
        pygame.draw.rect(surface,BLACK,(w/(numRows+2),h/(numCols+2),numRows*(w/(numRows+2)),numCols*(h/(numCols+2))),3) #outline
        pygame.draw.rect(surface,BLACK,(0,0,w,h),3) #outline
        if gameOver == True:
            gameOverText,gameOverBounds = showMessage("Game Over",30,w/2,h/2,RED,BLACK)
            surface.blit(gameOverText,gameOverBounds)
     
'''
The placeFood function keeps picking random locations on the snakeBoard to put a -1 until it picks a location that the snake is not part of.
'''
def placeFood(snakeBoard):
    isFood = False
    while isFood == False:
        a = random.randint(0,9)
        b = random.randint(0,9)
        if snakeBoard[a][b] == 0:
            snakeBoard[a][b] = -1
            isFood = True
    return snakeBoard

def showMessage(message,size,x,y,color,bg=None):
    font = pygame.font.SysFont("Arial",size,True,False)
    text = font.render(message,True,color,bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text,textBounds
'''
The moveSnake function adds the sum of the value of the head and the number one to the new head.  This function grows the snake by one
but the snakes tail will be removed by another function later on in main to fix this. 
'''
def moveSnake(dRow,dCol,snakeBoard,headRow,headCol,gameOver):
    ateFood = False
    newHeadRow,newHeadCol = 0,0
    headRow,headCol,headVal = findSnakeHead(snakeBoard)
    headRow+=dRow
    headCol+=dCol
    newHeadRow,newHeadCol = headRow,headCol    
    if newHeadRow>=0 and newHeadCol>=0 and newHeadRow<numRows and newHeadCol<numCols:
        if snakeBoard[newHeadRow][newHeadCol]==0: #not snake body or food
            snakeBoard[newHeadRow][newHeadCol] = headVal+1
        elif snakeBoard[newHeadRow][newHeadCol]==-1: #-1 is food
            ateFood = True
            snakeBoard[newHeadRow][newHeadCol] = headVal+1
        else:
            gameOver=True #if snake goes off screen or hits itself, the game is over
    return headRow, headCol,newHeadRow,newHeadCol,gameOver,ateFood
    
'''
The findSnakeHead function iterates through the values in the snakeBoard.  It trys to find the greatest value, the head, and stores
the row and column that the head was found in.
'''  
def findSnakeHead(snakeBoard):
    snake = []
    headRow = 0
    headCol = 0
    for a in range(len(snakeBoard)):
        for b in range(len(snakeBoard)):
            if snakeBoard[a][b] > 0:
                headRow = a
                headCol = b                
                snake.append([snakeBoard[headRow][headCol],[a,b]])
    snake.sort() # values are ordered from least to greatest
    headRow = snake[-1][1][0]
    headCol = snake[-1][1][1]
    headVal = snake[-1][0]
    return headRow, headCol,headVal

'''
The removeTail function makes the snake go back to its original size which was extended because of the
moveSnake function.  The removeTail function does this by subtracting 1 from each of the positive values and essentially removing the tail.
'''
def removeTail(snakeBoard):
    for a in range(len(snakeBoard)):
        for b in range(len(snakeBoard)):
            if snakeBoard[a][b]>0: # only positive numbers will get decreased
                snakeBoard[a][b]-=1
    return snakeBoard

'''
The loadBoard function puts the number one in the center of the board where the snake starts in the beginning of the game.  The rest of the values
in the snakeBoard are zero meaning they are not apart of the snake or food.
'''
def loadBoard():
    snakeBoard = []
    for i in range(numRows):
        snakeBoard.append([0]*numCols)
    snakeBoard[int(numRows/2)][int(numCols/2)] = 1
    return snakeBoard

def main():
    colorChosen = False # color isn't chosen at the beginning of the game
    color = None
    gameOver = False
    dRow,dCol = 1,0 # player starts by going down when the game starts
    snakeBoard = loadBoard()
    headRow,headCol,headVal = findSnakeHead(snakeBoard)
    ateFood = False # food hasn't been eaten yet
    snakeBoard = placeFood(snakeBoard) # food is placed on the board
    # color rectangles
    redRect = pygame.draw.rect(surface,colors[0][0],(w/3,(4*h)/10,30,30),0)
    yellowRect = pygame.draw.rect(surface,colors[1][0],(w/3,(5*h)/10,30,30),0)
    greenRect = pygame.draw.rect(surface,colors[2][0],(w/3,(6*h)/10,30,30),0)
    cyanRect = pygame.draw.rect(surface,colors[3][0],(w/3,(7*h)/10,30,30),0)
    purpleRect = pygame.draw.rect(surface,colors[4][0],(w/3,(8*h)/10,30,30),0)
    
    
    while(True):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if( event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
                
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and colorChosen == False: 
                # if the user clicks a button, the color of the button will become the color of the snake
                if redRect.collidepoint(pygame.mouse.get_pos()):
                    color = RED
                elif yellowRect.collidepoint(pygame.mouse.get_pos()):
                    color = YELLOW
                elif greenRect.collidepoint(pygame.mouse.get_pos()):
                    color = DRK_GREEN
                elif cyanRect.collidepoint(pygame.mouse.get_pos()):
                    color = CYAN
                elif purpleRect.collidepoint(pygame.mouse.get_pos()):
                    color = PURPLE
                colorChosen = True # color is chosen and the rest of the view is displayed
                    
            if event.type == pygame.KEYDOWN and (event.key== pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and gameOver==False:
                #snake cannot move if the game is over
                if event.key == pygame.K_UP:
                    dRow = -1
                    dCol = 0
                elif event.key == pygame.K_DOWN:
                    dRow = 1
                    dCol = 0
                elif event.key == pygame.K_RIGHT:
                    dCol = 1
                    dRow = 0
                elif event.key == pygame.K_LEFT:
                    dCol = -1 
                    dRow = 0
                    
            if event.type == pygame.KEYDOWN and event.key== pygame.K_r: # if the "r" key is clicked, the game starts over and the variables are reset
                colorChosen = False
                color = None
                gameOver = False
                dRow,dCol = 1,0
                snakeBoard = loadBoard()
                headRow,headCol,headVal = findSnakeHead(snakeBoard)
                ateFood = False
                snakeBoard = placeFood(snakeBoard)

                    
        if gameOver==False and colorChosen == True: # the snake doesn't begin to move until the color is chosen and does not move if the game is over
            headRow,headCol,newHeadRow,newHeadCol,gameOver,ateFood = moveSnake(dRow,dCol,snakeBoard,headRow,headCol,gameOver)
            if newHeadRow>=0 and newHeadCol>=0 and newHeadRow<numRows and newHeadCol<numCols and snakeBoard[newHeadRow][newHeadCol]!=-1 and ateFood == False and gameOver == False:
                snakeBoard = removeTail(snakeBoard) # tail is removed unless the snake eats or the game ends
            elif newHeadRow>=0 and newHeadCol>=0 and newHeadRow<numRows and newHeadCol<numCols and snakeBoard[newHeadRow][newHeadCol]!=-1 and ateFood == True and gameOver == False:
                eat.play() # sound effect
                snakeBoard = placeFood(snakeBoard) # more food is displayed on the screen
                ateFood = False # variable is reset
            else:
                gameOver = True
                
        # set background fill
        surface.fill(WHITE)
        
        # drawing code goes here
        drawScreen(snakeBoard,gameOver,colorChosen,color)
        
        pygame.display.update()
        clock.tick(12)
main()
