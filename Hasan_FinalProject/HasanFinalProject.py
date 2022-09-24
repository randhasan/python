'''
Rand Hasan
Honors Computer Programming
Period 11
Final Project: Arcade
'''

#-------------------References--------------------#
# All code written was my own however I used or coded graphics based off of the following images.
#
# 1. Used Tetris logo licensed to The Tetris Company used in the drawScreen function from 
# https://www2.instantticketcontest.com/TX/Tetris/winners.html accessed on 5/6/2019
#
# 2. Used Pong logo used in the drawScreen function from 
# https://www.deviantart.com/ringostarr39/art/Pong-logo-525250760 accessed on 5/6/2019
#
# 3. Used Break Out logo used in the drawScreen function from 
# https://www.arcade-museum.com/game_detail.php?game_id=7216 accessed on 5/13/2019
#
# 4. Used Trophy clipart used in the drawScreen function from 
# https://www.freeiconspng.com/img/13762 accessed on 6/2/2019
#
# 5. Coded arcade machine graphics based off of the image from
# https://www.istockphoto.com/vector/arcade-game-cabinet-gm452120377-23875563 accessed on 5/6/2019
#
# 6. Coded the graphics of the game Tetris based off of the image from 
# https://opensource.com/article/18/12/linux-toy-tetris accessed on 5/6/2019

import pygame, sys, math, os, random

#initialize game engine
pygame.init()

#Set up drawing surface
w = 800
h = 600
surface = pygame.display.set_mode((w, h))
xu = w/800
yu = h/600

# set window title bar
pygame.display.set_caption("Rand's Final Project")

# color constants
LIGHT_YELLOW = (255, 255, 100)
RED = (255,  0,  0)
ORANGE = ( 255, 153, 0)
YELLOW = ( 255, 255, 0)
GREEN = ( 0, 255,  0)
DRK_GREEN = ( 19, 98, 7)
CYAN = ( 89, 212, 234)
BLUE =  (  0,  0, 255)
PURPLE = ( 164, 66, 220)
INDIGO = ( 75 ,0, 130)
WHITE = ( 255, 255, 255)
LIGHT_GREY = (134, 136, 138)
MEDIUM_GREY = (50, 50, 50)
DARK_GREY = (30, 30, 30)
BLACK = ( 0, 0, 0)


# logos and other constants
pNumRows, pNumCols = 26, 38 # used in pong

TETRIS_LOGO = pygame.image.load('tetrislogo.png') # logo image
TETRIS_RECT = pygame.Rect(335*xu, 53*yu, 129, 85) # logo bounding box

PONG_LOGO = pygame.image.load('ponglogo.png') # logo image
PONG_RECT = pygame.Rect(105*xu, 97*yu, 120, 39) # logo bounding box

BREAKOUT_LOGO = pygame.image.load('breakoutlogo.jpg') # logo image
BREAKOUT_RECT = pygame.Rect(540*xu, 90*yu, 170, 50) # logo bounding box

BREAKOUT_TROPHY = pygame.image.load('breakoutTrophy.png') # used to identify the leaderboard in Breakout
BTROPHY_RECT = pygame.Rect(160*xu, 10*yu, 40*xu, 40*yu) # trophy image bounding box

clock = pygame.time.Clock()

#---------------------Functions------------------------------------
'''
The showMessage function is used to blit text in specified bounds onto the display.
'''
def showMessage(message, size, x, y, color, bg=None):
    font = pygame.font.SysFont("Fixedsys",size,True,False)
    text = font.render(message,True,color,bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text, textBounds
    
'''
The drawScreen function is the view of the program.  It contains code that blits shapes onto the screen to make the arcade display.  It also has code
for each of the individual games and what their display will look like.
'''
def drawScreen(pReadInstructions, pongBoard, gameChosen, hasChosen, pMoveBlockR, pMoveBlockL, pStartGame, pLeftPlayerPoints, pRightPlayerPoints, pRightWins, pLeftWins, pGameOver, bStartGame, bReadInstructions, bBricks, bBall, bPaddle, bGameOver, bNumLives, bScore, bNameEntered, bUserName, bCheckLeaderBoard, bLeaderBoard, tStartGame, tReadInstructions, tBlock, tetrisBoard, tMoveBlockRow, tMoveBlockCol, tRotateBlock, tNextBlock, tGameOver, tLevel, tNumRowsUntilNextLevel):
    surface.fill(BLACK) # arcade is drawn
    if hasChosen == False:
        x = 0
        pygame.draw.rect(surface, INDIGO,( 20*xu, 520*yu, 760*xu, 60*yu), 0)
        for i in range(3):
            tzoidList = [[(105*xu+x, 90*yu),(225*xu+x, 90*yu),(262*xu+x, 65*yu),(262*xu+x, 140*yu),(245*xu+x, 170*yu),(254*xu+x, 270*yu),(264*xu+x, 303*yu),(228*xu+x, 540*yu),(104*xu+x, 540*yu),(67*xu+x, 303*yu),(78*xu+x, 270*yu),(86*xu+x, 170*yu),(68*xu+x, 140*yu),(68*xu+x, 65*yu)],[(95*xu+x, 90*yu),(235*xu+x, 90*yu),(257*xu+x, 75*yu),(257*xu+x, 140*yu),(240*xu+x, 170*yu),(249*xu+x, 270*yu),(259*xu+x, 303*yu),(223*xu+x, 540*yu),(109*xu+x, 540*yu),(72*xu+x, 303*yu),(83*xu+x, 270*yu),(91*xu+x, 170*yu),(73*xu+x, 140*yu),(73*xu+x, 75*yu)],[(80*xu+x, 140*yu),(250*xu+x, 140*xu),(230*xu+x, 160*yu),(100*xu+x, 160*yu)],[(100*xu+x, 160*yu),(230*xu+x, 160*yu),(241*xu+x, 270*yu),(91*xu+x, 270*yu)],[(91*xu+x, 275*yu),(241*xu+x, 275*yu),(250*xu+x, 300*yu),(81*xu+x, 300*yu)],[(81*xu+x, 310*yu),(250*xu+x, 310*yu),(216*xu+x, 540*yu),(116*xu+x, 540*yu)],[(100*xu+x, 520*yu),(230*xu+x, 520*yu),(225*xu+x, 540*yu),(105*xu+x, 540*yu)]]
            tzoidList1 = [[(145*xu+x, 90*yu),(185*xu+x, 90*yu),(262*xu+x, 25*yu),(262*xu+x, 140*yu),(245*xu+x, 170*yu),(254*xu+x, 270*yu),(264*xu+x, 303*yu),(228*xu+x, 540*yu),(104*xu+x, 540*yu),(67*xu+x, 303*yu),(78*xu+x, 270*yu),(86*xu+x, 170*yu),(68*xu+x, 140*yu),(68*xu+x, 25*yu)],[(135*xu+x, 90*yu),(195*xu+x, 90*yu),(257*xu+x, 35*yu),(257*xu+x, 140*yu),(240*xu+x, 170*yu),(249*xu+x, 270*yu),(259*xu+x, 303*yu),(223*xu+x, 540*yu),(109*xu+x, 540*yu),(72*xu+x, 303*yu),(83*xu+x, 270*yu),(91*xu+x, 170*yu),(73*xu+x, 140*yu),(73*xu+x, 35*yu)]]
            if i == 0 or i == 2: # draws arcade machines on the left and right
                pygame.draw.polygon(surface, DARK_GREY, tzoidList[0], 0)
                pygame.draw.polygon(surface, MEDIUM_GREY,tzoidList[1], 0)
                pygame.draw.rect(surface, YELLOW,( 80*xu+x, 90*yu, 170*xu, 50*yu), 0)
            
            elif i == 1: # draws arcade machine in the middle
                pygame.draw.polygon(surface, DARK_GREY, tzoidList1[0], 0)
                pygame.draw.polygon(surface, MEDIUM_GREY, tzoidList1[1], 0)            
                pygame.draw.rect(surface, YELLOW,( 80*xu+x, 50*yu, 170*xu, 90*yu), 0)
            
            pygame.draw.polygon(surface, DARK_GREY, tzoidList[2], 0)
            pygame.draw.polygon(surface, MEDIUM_GREY, tzoidList[3], 0)
            pygame.draw.rect(surface, BLACK,( 110*xu+x, 175*yu, 112*xu, 80*yu), 0)        
            
            colors = (GREEN, RED, YELLOW, CYAN, BLUE, GREEN, RED, YELLOW, CYAN, BLUE, GREEN, RED, YELLOW, CYAN, BLUE, GREEN, RED, YELLOW)
            machineScreenList = [[(98*xu+x, 180*yu),(109*xu+x, 190*yu),(109*xu+x, 210*yu),(96*xu+x, 213*yu)],[(96*xu+x, 213*yu),(110*xu+x, 210*yu),(109*xu+x, 230*yu),(93*xu+x, 240*yu)],[(93*xu+x, 240*yu),(109*xu+x, 230*yu),(109*xu+x, 255*yu),(91*xu+x, 270*yu)],[(91*xu+x, 270*yu),(109*xu+x, 255*yu),(130*xu+x, 255*yu),(120*xu+x, 270*yu)],[(120*xu+x, 270*yu),(130*xu+x, 255*yu),(160*xu+x, 255*yu),(155*xu+x, 270*yu)],[(155*xu+x, 270*yu),(160*xu+x, 255*yu),(185*xu+x, 255*yu),(190*xu+x, 270*yu)],[(190*xu+x, 270*yu),(185*xu+x, 255*yu),(215*xu+x, 255*yu),(220*xu+x, 270*yu)],[(220*xu+x, 270*yu),(215*xu+x, 255*yu),(222*xu+x, 255*yu),(222*xu+x, 245*yu),(239*xu+x, 252*yu),(241*xu+x, 270*yu)],[(222*xu+x, 245*yu),(239*xu+x, 252*yu),(237*xu+x, 231*yu),(222*xu+x, 225*yu)],[(222*xu+x, 225*yu),(237*xu+x, 231*yu),(235*xu+x, 206*yu),(222*xu+x, 200*yu)],[(235*xu+x, 206*yu),(222*xu+x, 200*yu),(222*xu+x, 185*yu),(232*xu+x, 179*yu)],[(222*xu+x, 185*yu),(233*xu+x, 178*yu),(231*xu+x, 160*yu),(225*xu+x, 160*yu),(222*xu+x, 171*yu)],[(225*xu+x, 160*yu),(222*xu+x, 174*yu),(200*xu+x, 174*yu),(205*xu+x, 160*yu)],[(200*xu+x, 174*yu),(205*xu+x, 160*yu),(178*xu+x, 160*yu),(173*xu+x, 174*yu)],[(178*xu+x, 160*yu),(173*xu+x, 174*yu),(150*xu+x, 174*yu),(144*xu+x, 160*yu)],[(150*xu+x, 174*yu),(144*xu+x, 160*yu),(120*xu+x, 160*yu),(126*xu+x, 174*yu)],[(120*xu+x, 160*yu),(126*xu+x, 174*yu),(110*xu+x, 174*yu),(100*xu+x, 160*yu)],[(110*xu+x, 174*yu),(100*xu+x, 160*yu),(98*xu+x, 180*yu),(109*xu+x, 190*yu)]]
            for i in range(len(machineScreenList)):
                pygame.draw.polygon(surface, colors[i], machineScreenList[i], 0)
            
            # buttons and smaller details are drawn onto the machines
            pygame.draw.rect(surface, DARK_GREY,( 91*xu+x, 270*yu, 151*xu, 5*yu), 0)
            pygame.draw.polygon(surface, YELLOW, tzoidList[4], 0)
            pygame.draw.rect(surface, DARK_GREY,( 81*xu+x, 300*yu, 170*xu, 10*yu), 0)
            pygame.draw.polygon(surface, YELLOW, tzoidList[5], 0)
            pygame.draw.polygon(surface, DARK_GREY, tzoidList[6], 0)
            
            pygame.draw.ellipse(surface, DARK_GREY,( 110*xu+x, 282*yu, 22*xu, 10*yu), 0)
            pygame.draw.rect(surface, MEDIUM_GREY,( 118*xu+x, 275*yu, 7*yu, 16*yu), 0)
            pygame.draw.ellipse(surface, RED,( 115*xu+x, 265*yu, 15*xu, 15*yu), 0)
            
            pygame.draw.ellipse(surface, WHITE,( 160*xu+x, 281*yu, 19*xu, 9*yu), 0)
            pygame.draw.ellipse(surface, BLUE,( 187*xu+x, 287*yu, 19*xu, 9*yu), 0)
            pygame.draw.ellipse(surface, RED,( 215*xu+x, 281*yu, 19*xu, 9*yu), 0)
        
            pygame.draw.rect(surface, WHITE,( 164*xu+x, 278*yu, 10*xu, 7*yu), 0)
            pygame.draw.rect(surface, BLUE,( 191*xu+x, 284*yu, 10*xu, 7*yu), 0)
            pygame.draw.rect(surface, RED,( 219*xu+x, 278*yu, 10*xu, 7*yu), 0)
            
            pygame.draw.ellipse(surface, WHITE,( 164*xu+x, 275*yu, 10*xu, 6*yu), 0)
            pygame.draw.ellipse(surface, BLUE,( 191*xu+x, 281*yu, 10*xu, 6*yu), 0)
            pygame.draw.ellipse(surface, RED,( 219*xu+x, 275*yu, 10*xu, 6*yu), 0)    
            
            pygame.draw.rect(surface, BLACK,( 125*xu+x, 340*yu, 81*xu, 60*yu), 5)
            pygame.draw.rect(surface, RED,( 140*xu+x, 350*yu, 20*xu, 25*yu), 0)
            pygame.draw.rect(surface, BLACK,( 140*xu+x, 350*yu, 20*xu, 25*yu), 3)
            pygame.draw.rect(surface, BLACK,( 140*xu+x, 380*yu, 20*xu, 10*yu), 0)
            pygame.draw.rect(surface, BLACK,( 140*xu+x, 380*yu, 20*xu, 10*yu), 3)
            pygame.draw.ellipse(surface, BLACK,( 181*xu+x, 363*yu, 15*xu, 15*yu), 0)
            
            playText1, playBounds1 = showMessage("Press screen", 18, 165*xu+x, 225*yu, GREEN) # message blit onto "screens" of all three arcade machines
            surface.blit(playText1, playBounds1)
            playText2, playBounds2 = showMessage("to play", 18, 165*xu+x, 237*yu, GREEN)
            surface.blit(playText2, playBounds2)
            
            x += 230*xu
            
        surface.blit(PONG_LOGO, PONG_RECT)
        surface.blit(BREAKOUT_LOGO, BREAKOUT_RECT)
        surface.blit(TETRIS_LOGO, TETRIS_RECT)   
    
    if gameChosen == "Pong":
        pygame.draw.rect(surface, WHITE,( 18*xu, 58*yu, 764*xu, 524*yu), 2) # rectangle
        pygame.draw.rect(surface, WHITE,( 345*xu, 10*yu, 120*xu, 39*yu), 0) # rectangle that logo goes on top of to look nicer.
        pongNewRect = pygame.Rect(345*xu, 10*yu, 120, 39) # bounding box for logo image
        surface.blit(PONG_LOGO, pongNewRect) # blit pong logo image
        pLeftPlayerPointsBounds, pLeftPlayerPointsText = showMessage(str(pLeftPlayerPoints), 30, w/4, 30*yu, WHITE) # player points are displayed
        surface.blit(pLeftPlayerPointsBounds, pLeftPlayerPointsText)
        pRightPlayerPointsBounds, pRightPlayerPointsText = showMessage(str(pRightPlayerPoints), 30, 3*w/4, 30*yu, WHITE)
        surface.blit(pRightPlayerPointsBounds, pRightPlayerPointsText)
        
        y = 0
        for i in range(11): # draws dotted line 
            pygame.draw.rect(surface, WHITE,( w/2, 70*yu+(y*yu), 7*xu, 20*yu), 0)
            y += 60        
            
        x,y = 0, 0
        for r in range(pNumRows):
            for c in range(pNumCols):       
                if pongBoard[r][c] > 0: # ball
                    pygame.draw.ellipse(surface, WHITE,( 20*xu+x, 60*yu+y, 20*xu, 20*yu), 0)
                elif pongBoard[r][c] == -1: # blocks
                    pygame.draw.rect(surface, WHITE,( 20*xu+x, 60*yu+y, 20*xu, 20*yu), 0)
                x += 20*xu
            x = 0
            y += 20*yu    
            
        if pReadInstructions == False: # the instructions for Pong that are blitted onto the screen before the player plays the game
            pygame.draw.rect(surface, WHITE,( 100*xu, 110*yu, 602*xu, 422*yu), 0) # rectangle that instuctions are blit onto
            pWelcomeText, pWelcomeBounds = showMessage("Welcome to the game of Pong!", 40, w/2, 140*yu, BLACK)
            surface.blit(pWelcomeText, pWelcomeBounds)
            textLine1, textBounds1 = showMessage("Here are some instructions to help you understand how the game works.",20, w/2, 170*yu, BLACK)
            surface.blit(textLine1, textBounds1)
            textLine2, textBounds2 = showMessage("Pong is a two player game. As you will notice shortly, there are two blocks", 20, w/2, 190*yu, BLACK)
            surface.blit(textLine2, textBounds2)
            textLine3, textBounds3 = showMessage("on either side of the screen. The game will begin once a player presses", 20, w/2, 210*yu, BLACK)
            surface.blit(textLine3, textBounds3)   
            textLine4, textBounds4 = showMessage("the space key. The ball will start moving in a certain direction. The goal of", 20, w/2, 230*yu, BLACK)
            surface.blit(textLine4, textBounds4)    
            textLine5, textBounds5 = showMessage("the game is to hit the ball and not allow it to hit the wall behind your wall. To hit", 20, w/2, 250*yu, BLACK)
            surface.blit(textLine5, textBounds5)
            textLine6, textBounds6 = showMessage("the ball, you must move your block. The player on the left must use the 'W' key", 20, w/2, 270*yu, BLACK)
            surface.blit(textLine6, textBounds6)
            textLine7, textBounds7 = showMessage("to move your block up and the 'S' key to move your block down. The player on", 20, w/2, 290*yu, BLACK)
            surface.blit(textLine7, textBounds7)        
            textLine8, textBounds8 = showMessage("the right must use the 'UP' arrow to move your block up and the 'DOWN' arrow", 20, w/2, 310*yu, BLACK)
            surface.blit(textLine8, textBounds8)
            textLine9, textBounds9 = showMessage("to move your block down. If you miss the ball and it passes your block, the", 20, w/2, 330*yu, BLACK)
            surface.blit(textLine9, textBounds9)        
            textLine10, textBounds10 = showMessage("other player gets a point. The first player to get 11 points wins the game.", 20, w/2, 350*yu, BLACK)
            surface.blit(textLine10, textBounds10)
            textLine11, textBounds11 = showMessage("Each players score is displayed above their section. Additionally, you may", 20, w/2, 370*yu, BLACK)
            surface.blit(textLine11, textBounds11)        
            textLine12, textBounds12 = showMessage("notice a button in the upper left-hand corner. The button allows you to return", 20, w/2, 390*yu, BLACK)
            surface.blit(textLine12, textBounds12)
            textLine13, textBounds13 = showMessage("to the arcade at any time. Keep in mind that your data from Pong will NOT be", 20, w/2, 410*yu, BLACK)
            surface.blit(textLine13, textBounds13)        
            textLine14, textBounds14 = showMessage("saved if you decide to leave. There is also a second button that will appear", 20, w/2, 430*yu, BLACK)
            surface.blit(textLine14, textBounds14) 
            textLine15, textBounds15 = showMessage("when a player has earned 11 points and the game is over. This button allows", 20, w/2, 450*yu, BLACK)
            surface.blit(textLine15, textBounds15)
            textLine16, textBounds16 = showMessage("you to play Pong again. Each player's points will be reset to zero.", 20, w/2, 470*yu, BLACK)
            surface.blit(textLine16, textBounds16)    
            pygame.draw.rect(surface, BLACK,( 335*xu, 485*yu, 130*xu, 30*yu), 0) # read instructions box
            textLine17,textBounds17 = showMessage("I understand", 25, w/2, 500*yu, WHITE)
            surface.blit(textLine17, textBounds17)
            
        elif pReadInstructions==True: # once instructions have been read, the player needs to press the space key to begin
            startText, startBounds = showMessage("Press space to start", 30, 400*xu, 300*yu, WHITE, BLACK)
            if pStartGame == False:
                surface.blit(startText, startBounds)
            if pRightWins == True: # the winner and loser of the game will be displayed when the game is over
                winnerText, winnerBounds = showMessage("You Win!", 30, 3*w/4, 300*yu, GREEN, BLACK)
                loserText, loserBounds = showMessage("You Lose", 30, w/4, 300*yu, RED, BLACK)
                surface.blit(winnerText, winnerBounds)
                surface.blit(loserText, loserBounds)
            elif pLeftWins == True:
                winnerText, winnerBounds = showMessage("You Win!", 30, w/4, 300*yu, GREEN, BLACK)
                loserText, loserBounds = showMessage("You Lose", 30, 3*w/4, 300*yu, RED, BLACK)
                surface.blit(winnerText, winnerBounds)
                surface.blit(loserText, loserBounds) 
            # play again button
            if pGameOver == True and (pRightPlayerPoints == 11 or pLeftPlayerPoints == 11): # play can press the rectangle to play again
                pygame.draw.rect(surface, BLACK,( 100*xu, 10*yu, 40*xu, 40*yu), 0)
                pygame.draw.rect(surface, WHITE,( 100*xu, 10*yu, 40*xu, 40*yu), 2)
                pygame.draw.arc(surface, WHITE,( 110*xu, 21*yu, 20*xu, 20*yu), math.pi, math.pi/2, 3)
                triList2 = [(113*xu, 22*yu),(120*xu, 18*yu),(120*xu, 26*yu)]
                pygame.draw.polygon(surface, WHITE, triList2, 0)            
        # return to the main page button
        pygame.draw.rect(surface, BLACK,( w/20, 10*yu, 40*xu, 40*yu), 0)
        pygame.draw.rect(surface, WHITE,( w/20, 10*yu, 40*xu, 40*yu), 2)
        pygame.draw.rect(surface ,WHITE,( 53*xu, 27*yu, 21*xu, 7*yu), 0)
        triList1 = [(45*xu, 30*yu),(52*xu, 23*yu),(52*xu, 37*yu)]
        pygame.draw.polygon(surface, WHITE, triList1, 0)
        
    elif gameChosen == "Tetris":
        #draws help, stats and next blocks onto screen as well as text and the game board rectangle
        pygame.draw.rect(surface, WHITE,( 260*xu, 110*yu, 270*xu, 450*yu), 2)
        pygame.draw.rect(surface, WHITE,( 595*xu, 110*yu, 155*xu, 160*yu), 2)
        pygame.draw.rect(surface, WHITE,( 595*xu, 315*yu, 155*xu, 245*yu), 2)
        pygame.draw.rect(surface, WHITE,( 50*xu, 110*yu, 155*xu, 120*yu), 2)
        
        tNextText, tNextBounds = showMessage("Next", 35, 672*xu, 130*yu, WHITE)
        surface.blit(tNextText, tNextBounds)
        
        tHelpText, tHelpBounds = showMessage("Help", 35, 672*xu, 335*yu, WHITE)
        surface.blit(tHelpText, tHelpBounds)
        
        tLeftText, tLeftBounds = showMessage("Left", 25, 635*xu, 365*yu, WHITE)
        surface.blit(tLeftText, tLeftBounds)
        pygame.draw.rect(surface, WHITE,( 700*xu, 360*yu, 25*xu, 7*yu), 0)
        tTriList1 = [( 700*xu, 355*yu),( 700*xu, 372*yu),( 692*xu, 363.5*yu)]
        pygame.draw.polygon(surface, WHITE, tTriList1, 0)
        
        tRightText, tRightBounds = showMessage("Right", 25, 640*xu, 395*yu, WHITE)
        surface.blit(tRightText, tRightBounds)
        pygame.draw.rect(surface, WHITE,( 700*xu, 390*yu, 25*xu, 7*yu), 0)
        tTriList2 = [( 725*xu, 384*yu),( 725*xu, 401*yu),( 733*xu, 392.5*yu)]
        pygame.draw.polygon(surface, WHITE, tTriList2, 0)
        
        tRotateText, tRotateBounds = showMessage("Rotate", 25, 645*xu, 425*yu, WHITE)
        surface.blit(tRotateText, tRotateBounds)
        pygame.draw.rect(surface, WHITE,( 709*xu, 420*yu, 7*xu, 15*yu), 0)
        tTriList3 = [( 704*xu, 420*yu),( 720*xu, 420*yu),( 712.5*xu, 412*yu)]
        pygame.draw.polygon(surface, WHITE, tTriList3, 0)    
        
        if tStartGame == False:
            tStartText, tStartBounds = showMessage("Start", 25, 638*xu, 455*yu, BLACK, WHITE) # highlights the word start in the help box
        else:
            tStartText, tStartBounds = showMessage("Start", 25, 638*xu, 455*yu, WHITE)
        surface.blit(tStartText, tStartBounds)
        tSText, tSBounds = showMessage("s", 25, 713*xu, 455*yu, WHITE)
        surface.blit(tSText, tSBounds)        
        
        tQuitText, tQuitBounds = showMessage("Quit", 25, 635*xu, 485*yu, WHITE)
        surface.blit(tQuitText, tQuitBounds)
        tQText, tQBounds = showMessage("q", 25, 713*xu, 485*yu, WHITE)
        surface.blit(tQText, tQBounds)
        
        if tGameOver == True: # the words play again are displayed and highlighted when the game is over
            tPlayAgainText1, tPlayAgainBounds1 = showMessage(" Play ", 25 , 636*xu, 510*yu, BLACK, WHITE)
            tPlayAgainText2, tPlayAgainBounds2 = showMessage("Again", 25 , 636*xu, 528*yu, BLACK, WHITE)
            surface.blit(tPlayAgainText1, tPlayAgainBounds1)
            surface.blit(tPlayAgainText2, tPlayAgainBounds2)
            tPText, tPBounds = showMessage("p", 25, 713*xu, 515*yu, WHITE)
            surface.blit(tPText, tPBounds)
        
        tStatsText, tStatsBounds = showMessage("Stats", 35, 125*xu, 130*yu, WHITE)
        surface.blit(tStatsText, tStatsBounds)
        TETRIS_RECT2 = pygame.Rect((340*xu, 15*yu, 129, 85))
        surface.blit(TETRIS_LOGO,TETRIS_RECT2)
        
        tLevelText, tLevelBounds = showMessage("Level: " + str(tLevel), 23, 95*xu, 157*yu, WHITE)
        surface.blit(tLevelText, tLevelBounds)
        
        tNumRowsUntilNextLevelText1, tNumRowsUntilNextLevelBounds1 = showMessage("Number of", 23, 105*xu, 185*yu, WHITE)
        surface.blit(tNumRowsUntilNextLevelText1, tNumRowsUntilNextLevelBounds1)
        
        tNumRowsUntilNextLevelText2, tNumRowsUntilNextLevelBounds2 = showMessage("Rows to Clear: " + str(tNumRowsUntilNextLevel), 23, 130*xu, 203*yu, WHITE)
        surface.blit(tNumRowsUntilNextLevelText2, tNumRowsUntilNextLevelBounds2)        
        
        # the different colored boxes are drawn based on their values in the 2D list stored in the variable tetrisBoard
        x,y = 0, 0 
        for r in range(15):
            for c in range(9):  
                if tetrisBoard[r][c] == 1: 
                    pygame.draw.rect(surface, RED,( 260*xu + x, 110*yu + y, 30*xu, 30*yu), 0)
                elif tetrisBoard[r][c] == 2:
                    pygame.draw.rect(surface, ORANGE,( 260*xu + x, 110*yu + y, 30*xu, 30*yu), 0)
                elif tetrisBoard[r][c] == 3:
                    pygame.draw.rect(surface, GREEN,( 260*xu + x, 110*yu + y, 30*xu, 30*yu), 0)
                elif tetrisBoard[r][c] == 4:
                    pygame.draw.rect(surface, BLUE,( 260*xu + x, 110*yu + y, 30*xu, 30*yu), 0)  
                elif tetrisBoard[r][c] == 5:
                    pygame.draw.rect(surface, PURPLE,( 260*xu + x, 110*yu + y, 30*xu, 30*yu), 0) 

                x += 30*xu
            x = 0
            y += 30*yu  
            
        if tGameOver == False and tStartGame == True: # the next block will be displayed in the next block box
            x,y = 0, 0
            for r in range(len(tNextBlock)):
                for c in range(len(tNextBlock[r])):
                    if tNextBlock[r][c] == 1:
                        pygame.draw.rect(surface, RED,( 630*xu + x, 170*yu + y, 30*xu, 30*yu), 0)
                    elif tNextBlock[r][c] == 2:
                        pygame.draw.rect(surface, ORANGE,( 630*xu + x, 170*yu + y, 30*xu, 30*yu), 0)
                    elif tNextBlock[r][c] == 3:
                        pygame.draw.rect(surface, GREEN,( 630*xu + x, 170*yu + y, 30*xu, 30*yu), 0)   
                    elif tNextBlock[r][c] == 4:
                        pygame.draw.rect(surface, BLUE,( 630*xu + x, 170*yu + y, 30*xu, 30*yu), 0)  
                    elif tNextBlock[r][c] == 5:
                        pygame.draw.rect(surface, PURPLE,( 630*xu + x, 170*yu + y, 30*xu, 30*yu), 0)           
                    x += 30*xu
                x = 0
                y += 30*yu                  
                
        if tReadInstructions == False: #instructions for Tetris are displayed on the screen at the beginning of the game
            pygame.draw.rect(surface, WHITE,( 100*xu, 110*yu, 602*xu, 422*yu), 0)
            tWelcomeText, tWelcomeBounds = showMessage("Welcome to the game of Tetris!", 40, w/2, 140*yu, BLACK)
            surface.blit(tWelcomeText, tWelcomeBounds)
            tTextLine1, tTextBounds1 = showMessage("Here are some instructions to help you understand how the game works.",20, w/2, 170*yu, BLACK)
            surface.blit(tTextLine1, tTextBounds1)
            tTextLine2, tTextBounds2 = showMessage("Tetris is a one player tile-matching game. The game pieces, or blocks, are", 20, w/2, 190*yu, BLACK)
            surface.blit(tTextLine2, tTextBounds2)
            textLine3, textBounds3 = showMessage("geometric shapes composed of four blocks each. A random sequence of blocks", 20, w/2, 210*yu, BLACK)
            surface.blit(textLine3, textBounds3)   
            textLine4, textBounds4 = showMessage("will fall down. The objective of the game is to moves the blocks right, left, or", 20, w/2, 230*yu, BLACK)
            surface.blit(textLine4, textBounds4)    
            textLine5, textBounds5 = showMessage("even rotate them to form a horizontal line that is filled entirely with blocks.", 20, w/2, 250*yu, BLACK)
            surface.blit(textLine5, textBounds5)
            textLine6, textBounds6 = showMessage("When this happens, all of the blocks in that line disappear and the blocks above", 20, w/2, 270*yu, BLACK)
            surface.blit(textLine6, textBounds6)
            textLine7, textBounds7 = showMessage("all down to fill in the space. If the number of lines you clear equals your current", 20, w/2, 290*yu, BLACK)
            surface.blit(textLine7, textBounds7)        
            textLine8, textBounds8 = showMessage("level, you will move onto the next level. If the game pieces reach the top of the", 20, w/2, 310*yu, BLACK)
            surface.blit(textLine8, textBounds8)
            textLine9, textBounds9 = showMessage("board, the game will end and the player can choose to play again and start over at", 20, w/2, 330*yu, BLACK)
            surface.blit(textLine9, textBounds9)        
            textLine10, textBounds10 = showMessage("level one or go back to the arcade. You may return to the arcade at any time but", 20, w/2, 350*yu, BLACK)
            surface.blit(textLine10, textBounds10)
            textLine11, textBounds11 = showMessage("you can only play again once the game has ended. In order to move your block", 20, w/2, 370*yu, BLACK)
            surface.blit(textLine11, textBounds11)        
            textLine12, textBounds12 = showMessage("right, left, rotate it, or return to the arcade, you must lock at the help", 20, w/2, 390*yu, BLACK)
            surface.blit(textLine12, textBounds12)
            textLine13, textBounds13 = showMessage("box which indicates the key you need to press. The key that you need to press", 20, w/2, 410*yu, BLACK)
            surface.blit(textLine13, textBounds13)        
            textLine14, textBounds14 = showMessage("to play again will show up in the help box once the game is over. Also, feel", 20, w/2, 430*yu, BLACK)
            surface.blit(textLine14, textBounds14) 
            textLine15, textBounds15 = showMessage("free to check out the leaderboard once the game has ended. Finally, keep in", 20, w/2, 450*yu, BLACK)
            surface.blit(textLine15, textBounds15)
            textLine16, textBounds16 = showMessage("mind that your data will NOT be saved if you decide to return to the arcade.", 20, w/2, 470*yu, BLACK)
            surface.blit(textLine16, textBounds16)    
            pygame.draw.rect(surface, BLACK,( 335*xu, 485*yu, 130*xu, 30*yu), 0) # read instructions box
            textLine17,textBounds17 = showMessage("I understand", 25, w/2, 500*yu, WHITE)
            surface.blit(textLine17, textBounds17)
            
        elif tReadInstructions==True: # message will be displayed when the game has ended
            if tGameOver == True:
                tGameOverText, tGameOverBounds = showMessage("Game Over", 40, w/2, 300*yu, RED, BLACK)
                surface.blit(tGameOverText, tGameOverBounds)                        
                tFinalScoreText, tFinalScoreBounds = showMessage("You got to level "+str(tLevel), 30, w/2, 360*yu, WHITE, BLACK)
                surface.blit(tFinalScoreText, tFinalScoreBounds)
        
    elif gameChosen == "Break Out":
        breakOutNewRect = pygame.Rect(320*xu, 5*yu, 120, 39) # bounding box for logo image
        surface.blit(BREAKOUT_LOGO,breakOutNewRect)
        
        for brick in bBricks: # draws bricks and outlines of the bricks
            pygame.draw.rect(surface, YELLOW, brick, 0)
            pygame.draw.rect(surface, WHITE, brick, 2)
            
        pygame.draw.rect(surface, WHITE,( 0, 60*yu, w, 540*yu), 3) # game board outline
        pygame.draw.ellipse(surface, WHITE, bBall, 0)
        pygame.draw.ellipse(surface, YELLOW, bBall, 2)
        pygame.draw.rect(surface, YELLOW, bPaddle, 0)
        pygame.draw.rect(surface, WHITE, bPaddle, 2)
        
        x = 0
        for i in range(bNumLives): # draws hearts
            heartList = [(645*xu + x, 40*yu), (658*xu + x, 22.5*yu), (632*xu + x, 22.5*yu)]
            pygame.draw.polygon(surface, RED, heartList, 0)
            pygame.draw.ellipse(surface, RED,( 632*xu + x, 14*yu, 14*xu, 17*yu), 0)
            pygame.draw.ellipse(surface, RED,( 645*xu + x, 14*yu, 14*xu, 17*yu), 0)
            x += 40*xu            
            
        bScoreText, bScoreBounds = showMessage(str(bScore), 40, 3.4*w/5, 30*yu, WHITE) # displays player's score
        surface.blit(bScoreText, bScoreBounds)
        
        if bReadInstructions == False: # Break Out instructions
            pygame.draw.rect(surface, WHITE,( 100*xu, 110*yu, 602*xu, 422*yu), 0)
            bWelcomeText, bWelcomeBounds = showMessage("Welcome to the game Break Out!", 40, w/2, 140*yu, BLACK)
            surface.blit(bWelcomeText, bWelcomeBounds)
            bTextLine1, bTextBounds1 = showMessage("Here are some instructions to help you understand how the game works.",20, w/2, 170*yu, BLACK)
            surface.blit(bTextLine1, bTextBounds1)
            bTextLine2, bTextBounds2 = showMessage("Break Out is a single player game. As you will notice shortly, there is one block", 20, w/2, 190*yu, BLACK)
            surface.blit(bTextLine2, bTextBounds2)
            bTextLine3, bTextBounds3 = showMessage("near the bottom of the screen. The game will begin once you read the instructions", 20, w/2, 210*yu, BLACK)
            surface.blit(bTextLine3, bTextBounds3)   
            bTextLine4, bTextBounds4 = showMessage("and press the space key. The ball will start moving in a certain direction. The goal", 20, w/2, 230*yu, BLACK)
            surface.blit(bTextLine4, bTextBounds4)    
            bTextLine5, bTextBounds5 = showMessage("of the game is to hit the ball and not allow it to get past your block. To hit", 20, w/2, 250*yu, BLACK)
            surface.blit(bTextLine5, bTextBounds5)
            bTextLine6, bTextBounds6 = showMessage("the ball, you must move your block. To move your block right, press the 'RIGHT'", 20, w/2, 270*yu, BLACK)
            surface.blit(bTextLine6, bTextBounds6)
            bTextLine7, bTextBounds7 = showMessage("arrow key. To move your block left, press the 'LEFT' arrow key. If you miss", 20, w/2, 290*yu, BLACK)
            surface.blit(bTextLine7, bTextBounds7)        
            bTextLine8, bTextBounds8 = showMessage("the ball and it passes your block, you will lose a life. You get three lives", 20, w/2, 310*yu, BLACK)
            surface.blit(bTextLine8, bTextBounds8)
            bTextLine9, bTextBounds9 = showMessage("that will be displayed as hearts near the top of the screen. You will also get", 20, w/2, 330*yu, BLACK)
            surface.blit(bTextLine9, bTextBounds9)        
            bTextLine10, bTextBounds10 = showMessage("five points for each block you break.  If you manage to break all of the blocks", 20, w/2, 350*yu, BLACK)
            surface.blit(bTextLine10, bTextBounds10)
            bTextLine11, bTextBounds11 = showMessage("before you lose all of your lives, you win! Additionally, you may notice a", 20, w/2, 370*yu, BLACK)
            surface.blit(bTextLine11, bTextBounds11)        
            bTextLine12, bTextBounds12 = showMessage("button in the upper left-hand corner. This button allows you to return to the", 20, w/2, 390*yu, BLACK)
            surface.blit(bTextLine12, bTextBounds12)
            bTextLine13, bTextBounds13 = showMessage("arcade at anytime. Keep in mind that your data from Break Out will NOT be saved", 20, w/2, 410*yu, BLACK)
            surface.blit(bTextLine13, bTextBounds13)        
            bTextLine14, bTextBounds14 = showMessage("if you decide to leave. A second button will also appear after you have won or", 20, w/2, 430*yu, BLACK)
            surface.blit(bTextLine14, bTextBounds14) 
            bTextLine15, bTextBounds15 = showMessage("lost all three of your lives and the game is over. This button allows you to play", 20, w/2, 450*yu, BLACK)
            surface.blit(bTextLine15, bTextBounds15)
            bTextLine16, bTextBounds16 = showMessage("Break Out again. The number of lives you have will be reset to three.", 20, w/2, 470*yu, BLACK)
            surface.blit(bTextLine16, bTextBounds16)    
            pygame.draw.rect(surface, BLACK,( 335*xu, 485*yu, 130*xu, 30*yu), 0) # read instructions box
            bTextLine17,bTextBounds17 = showMessage("I understand", 25, w/2, 500*yu, WHITE)
            surface.blit(bTextLine17, bTextBounds17)
        
        elif bReadInstructions==True:
            if bNameEntered == False: # player's username is displayed on the screen
                bUserNameText, bUserNameBounds = showMessage("Please enter a username that contains letters and/or numbers", 30, 400*xu, 250*yu, WHITE, BLACK)
                surface.blit(bUserNameText, bUserNameBounds)
                bEnteredNameText, bEnteredNameBounds = showMessage(bUserName, 30, 400*xu, 300*yu, WHITE, BLACK)
                surface.blit(bEnteredNameText, bEnteredNameBounds)
                pygame.draw.rect(surface, WHITE, (360*xu, 360*yu, 80*xu, 40*yu), 0)
                bDoneText, bDoneBounds = showMessage("Done", 30, 400*xu, 380*yu, BLACK) # box that player presses once they have entered a username
                surface.blit(bDoneText, bDoneBounds)
                
            elif bNameEntered == True: # player needs to press space to start after entering their username
                startText, startBounds = showMessage("Click space to start "+bUserName, 30, 400*xu, 300*yu, WHITE, BLACK)
                if bStartGame == False:
                    surface.blit(startText, startBounds)
                else:
                    if bGameOver == True:
                        if bNumLives != 0 and len(bBricks) == 0: # all blocks have been hit
                            bGameOverText, bGameOverBounds = showMessage("You Win!", 40, w/2, 300*yu, GREEN, BLACK)
                        else:
                            bGameOverText, bGameOverBounds = showMessage("Game Over", 40, w/2, 300*yu, RED, BLACK)
                        surface.blit(bGameOverText, bGameOverBounds)                        
                        bFinalScoreText, bFinalScoreBounds = showMessage("Your final score was " + str(bScore), 30, w/2, 360*yu, WHITE, BLACK)
                        surface.blit(bFinalScoreText, bFinalScoreBounds)
                        
                        # draws play again box
                        pygame.draw.rect(surface, BLACK,( 100*xu, 10*yu, 40*xu, 40*yu), 0)
                        pygame.draw.rect(surface, WHITE,( 100*xu, 10*yu, 40*xu, 40*yu), 2)
                        pygame.draw.arc(surface, WHITE,( 110*xu, 21*yu, 20*xu, 20*yu), math.pi, math.pi/2, 3)
                        triList2 = [(113*xu, 22*yu),(120*xu, 18*yu),(120*xu, 26*yu)]
                        pygame.draw.polygon(surface, WHITE, triList2, 0)        
                        
                        # draws leader board box
                        pygame.draw.rect(surface, WHITE,( 160*xu, 10*yu, 40*xu, 40*yu), 2)
                        surface.blit(BREAKOUT_TROPHY, BTROPHY_RECT)
                        
                        # draws the leader board if the user has pressed the leader board box
                        x, y = 0, 0 
                        if bCheckLeaderBoard == True:
                            pygame.draw.rect(surface, WHITE,( 100*xu, 110*yu, 602*xu, 422*yu), 0)
                            bLeaderText, bLeaderBounds = showMessage(" Leader Board ", 40, 400*xu, 150*yu, WHITE, BLACK) 
                            surface.blit(bLeaderText, bLeaderBounds)                            
                            for i in range(len(bLeaderBoard)): # displays scores and corresponding usernames
                                bNameText, bNameBounds = showMessage(str(bLeaderBoard[i][1]), 30, 360*xu, 185*yu + y, BLACK) 
                                surface.blit(bNameText, bNameBounds)                                                     
                                bPointsText, bPointsBounds = showMessage(str(bLeaderBoard[i][0]), 30, 460*xu, 185*yu + y, BLACK) 
                                surface.blit(bPointsText, bPointsBounds)           
                                y += 30*yu
                            
        # draws the box that the user must press to return to the arcade
        pygame.draw.rect(surface, BLACK,( w/20, 10*yu, 40*xu, 40*yu), 0)
        pygame.draw.rect(surface, WHITE,( w/20, 10*yu, 40*xu, 40*yu), 2)
        pygame.draw.rect(surface ,WHITE,( 53*xu, 27*yu, 21*xu, 7*yu), 0)
        triList1 = [(45*xu, 30*yu),(52*xu, 23*yu),(52*xu, 37*yu)]
        pygame.draw.polygon(surface, WHITE, triList1, 0)        
            
            
#-------------------------------Pong Functions----------------------------
'''
The movePongBall function adds the sum of the value of the ball and the direction the ball is suppose to go to the pNewBallRow and pNewBallCol variables.  
This function technically makes the ball longer but it is shortened with the shortenPongBall function. This function also controls the direction that the ball goes
after it hits the top or bottom wall and the player's blocks.  Additionally, it controls whether or not the game is over; If the ball is in the first or last
column, the variable pGameOver is True and is sent to main as well as the drawScreen function.
'''
def movePongBall(pongBoard, pMoveBallRow, pMoveBallCol, pBallRow, pBallCol, pBallVal, pMoveBlockR, pMoveBlockL, pRightHitLast, pGameOver, pLeftPlayerPoints, pRightPlayerPoints):
    pNewBallRow, pNewBallCol = 0, 0
    pBallRow, pBallCol, pBallVal = findPongBall(pongBoard) # locates the ball that has a value of one in the pongBoard list
    pBallRow += pMoveBallRow
    pBallCol += pMoveBallCol
    pNewBallRow, pNewBallCol = pBallRow, pBallCol
    
    if pNewBallCol == 38 or pNewBallCol == -1: # ball hits the right or left wall
        pGameOver = True
        if pNewBallCol == 38: # hits right wall
            pLeftPlayerPoints += 1
        elif pNewBallCol == -1: # hits left wall
            pRightPlayerPoints += 1
            
    elif (pNewBallRow == pNumRows or pNewBallRow == 0) and (pNewBallCol > 36 or pNewBallCol < 1): # ball hits the top or bottom wall in the same row as the paddle or past it but not the right or left wall
        pGameOver = True
        if pNewBallCol > 36: # right side
            pLeftPlayerPoints += 1
        elif pNewBallCol < 1: # left side
            pRightPlayerPoints += 1
    else:
        pGameOver = False
      
    if pGameOver == False:
        if pNewBallRow >= 0 and pNewBallCol >= 0 and pNewBallRow < pNumRows and pNewBallCol < pNumCols and pNewBallCol != 35 and pNewBallCol != 2 and pGameOver == False:
            pongBoard[pNewBallRow][pNewBallCol] = pBallVal + 1 # moves the ball
        elif pNewBallCol == 35: # column before right paddle
            if pongBoard[pNewBallRow][35] !=- 1 and (pNewBallRow != 26 and pongBoard[pNewBallRow+1][35] != -1):
                pongBoard[pNewBallRow][pNewBallCol] = pBallVal + 1 # moves the ball
            elif pNewBallRow == 26 and pongBoard[pNewBallRow+1][35] != -1:
                pongBoard[pNewBallRow][pNewBallCol] = pBallVal + 1 # moves the ball
        elif pNewBallCol == 2: # column after left paddle
            if pongBoard[pNewBallRow][2] != -1 and (pNewBallRow != 26 and pongBoard[pNewBallRow+1][2] != -1) and pongBoard[pNewBallRow-1][2] != -1:
                pongBoard[pNewBallRow][pNewBallCol] = pBallVal + 1 # moves the ball
            elif pNewBallRow == 26 and pongBoard[pNewBallRow+1][2] != -1:
                pongBoard[pNewBallRow][pNewBallCol] = pBallVal + 1 # moves the ball
            elif pNewBallRow != 26 and pongBoard[pNewBallRow][2] != -1 and pongBoard[pNewBallRow+1][2] == -1 and pongBoard[pNewBallRow-1][2] != -1:
                pongBoard[pNewBallRow][pNewBallCol] = pBallVal + 1 # moves the ball
   
    for r in range(pNumRows):
        for c in range(pNumCols):
            if pongBoard[r][c] == -1: # paddle
                if r == pNewBallRow + 1 and c == pNewBallCol and pNewBallCol == 35: # ball hits the paddle on the right
                    if pNewBallRow == 9 + pMoveBlockR: # ball hits the top of the paddle
                        pMoveBallCol = -1
                        pMoveBallRow = -1

                    elif pNewBallRow == 10 + pMoveBlockR: # if ball hits the middle of the paddle, it goes up if the ball is in the lower-half of the board or down if the ball is in the upper-half of the board
                        if pNewBallRow >= int(pNumRows/2): # ball is in the lower-half of the board
                            pMoveBallCol = -1
                            pMoveBallRow = -1
                        else: # ball is in the upper-half of the board
                            pMoveBallCol = -1
                            pMoveBallRow = 1

                    elif pNewBallRow == 11 + pMoveBlockR: # ball hits the bottom of the paddle
                        pMoveBallCol = -1
                        pMoveBallRow = 1

                elif r == pNewBallRow and c == pNewBallCol and pNewBallCol == 35: # ball can bounce off right block bottom corner of the paddle
                    if pNewBallRow == 12 + pMoveBlockR:
                        pMoveBallCol = -1
                        pMoveBallRow = 1                    

                elif r == pNewBallRow - 1 and c == pNewBallCol and pNewBallCol == 2: # ball hits the top of the left paddle
                    if pNewBallRow == 11 + pMoveBlockL:
                        pMoveBallCol = 1
                        pMoveBallRow = -1

                    elif pNewBallRow == 12 + pMoveBlockL: # ball hits the middle of the left paddle and goes up if the ball is in the lower-half of the board or down if the ball is in the upper-half of the board
                        if pNewBallRow >= int(pNumRows/2):
                            pMoveBallCol = 1
                            pMoveBallRow = -1
                        else:
                            pMoveBallCol = 1
                            pMoveBallRow = 1

                    elif pNewBallRow == 13 + pMoveBlockL: # ball hits bottom of the left paddle
                        pMoveBallCol = 1
                        pMoveBallRow = 1

                elif pNewBallCol == 2 and r == pNewBallRow and c == pNewBallCol: # the ball can bounce off the bottom corner of left paddle              
                    if pNewBallRow == 10 + pMoveBlockL:
                        pMoveBallCol = 1
                        pMoveBallRow = -1
    
    # which player hit last
    if pNewBallCol == 35:
        pRightHitLast.append(True)
    if pNewBallCol == 2:
        pRightHitLast.append(False)
    if pRightHitLast[-1] == True:
        pRightHitLast = True  
        leftHitLast = False    
    else:
        pRightHitLast = False
        leftHitLast = True

    # ball hits bottom of rectangle
    if pBallRow == pNumRows and pGameOver != True:
        if pRightHitLast == True:
            pMoveBallCol = -1
            pMoveBallRow = -1
        elif pRightHitLast == False:
            pMoveBallCol = 1
            pMoveBallRow = -1        

    # ball hits top of rectangle     
    elif pBallRow == 0 and pGameOver != True:
        if pRightHitLast == True:
            pMoveBallCol = -1
            pMoveBallRow = 1
        elif pRightHitLast == False:
            pMoveBallCol = 1
            pMoveBallRow = 1

    return pBallRow, pBallCol, pNewBallRow, pNewBallCol, pMoveBallRow, pMoveBallCol, pGameOver, pLeftPlayerPoints, pRightPlayerPoints

'''
The findPongBall function iterates through the values in the pongBoard.  It trys to find the greatest value 1, which is the ball,
and storesthe row and column that the ball was found in.
'''
def findPongBall(pongBoard):
    pBallRow, pBallCol = 0, 0
    for r in range(pNumRows):
        for c in range(pNumCols):
            if pongBoard[r][c] == 1: # the ball
                pBallRow, pBallCol = r, c
    pBallVal = pongBoard[pBallRow][pBallCol]
    return pBallRow, pBallCol, pBallVal

'''
The shortBall function makes the ball go back to its original size which was extended due to the movePongBall function.
The removeTail function makes the snake go back to its original size which was extended because of the
moveSnake function.  The removeTail function does this by subtracting 1 from each of the positive values and essentially removing the tail.
'''
def shortenPongBall(pongBoard):
    for r in range(pNumRows):
        for c in range(pNumCols):
            if pongBoard[r][c] > 0:
                pongBoard[r][c] -= 1
    return pongBoard
'''
The makePongBoard function creates a 2D list filled with zeros meaning they are not part of the ball or player's blocks.  One value will be 1 which is the ball.  
'''
def makePongBoard():
    pongBoard = []
    for i in range(pNumRows):
        pongBoard.append([0]*pNumCols)
    pongBoard[int(pNumRows/3)][int(pNumCols/3)] = 1 # where the ball starts
    return pongBoard 

'''
The makePongBlocks function sets 3 values on either side of the area in which the game is placed equal to -1.  Because they have a value
of -1, the drawScreen function will display a white rectangle in the row and column in which the value equals zero.  The values of the blocks
will not change but they will be able to be moved in the main function.
'''
def makePongBlocks(pMoveBlockR, pMoveBlockL, pongBoard, pStartGame):
    for r in range(pNumRows):
        for c in range(pNumCols):
            if (c == 2 or c == pNumCols-3) and pongBoard[r][c] != 1: # clears the cols the blocks are in
                pongBoard[r][c] = 0
    if pStartGame == True:
        for i in range(10+pMoveBlockL, 13+pMoveBlockL):
            if pongBoard[i][2] != 1:
                pongBoard[i][2] = -1
        for i in range(10+pMoveBlockR, 13+pMoveBlockR):
            if pongBoard[i][pNumCols-3] != 1:
                pongBoard[i][pNumCols-3] = -1  
    else:
        for i in range(10, 13):
            pongBoard[i][2] = -1
            pongBoard[i][pNumCols-3] = -1          
    return pongBoard

#--------------Break Out Functions-----------------
'''
The function makeBreakOutBricks creates a list of 100 rectangles that will be displayed as the bricks in the drawScreen function.
'''
def makeBreakOutBricks():
    bBricks = []
    x, y = 0, 0
    for r in range(5):
        for c in range(20):
            bBricks.append(pygame.Rect(x, 60*yu+y, 40*xu, 25*yu))
            x += 40*xu
        x = 0
        y += 25*yu
    return bBricks

'''
The moveBreakOutBall function moves the bounding box of the ball that is displayed in the drawScreen function.
'''
def moveBreakOutBall(bBall, bBallRow, bBallCol, bLoseLife):
    bBall.right += bBallCol
    bBall.top += bBallRow
    if bBall.right <= 20 * xu: # ball hits left wall
        bBall.right = 20 * xu
        bBallCol *= -1
    elif bBall.right > 800 * xu: # ball hits right wall
        bBall.right = 800 * xu
        bBallCol *= -1
    if bBall.top <= 60 * xu: # ball hits top of the board
        bBall.top = 60 * xu
        bBallRow *= -1
    elif bBall.top > 580 * yu: # ball hits the bottom of the board
        bBall.top = 580 * yu
        bBall.right -= bBallCol # stops the ball from moving an extra space
        bBallCol = 0
        bLoseLife = True
    return bBall, bBallRow, bBallCol, bLoseLife

'''
The breakOutBallCollides function controls move the bounding box of the ball that is displayed in the drawScreen function
after it collides with a brick or the paddle.
'''
def breakOutBallCollides(bBricks, bBall, bBallRow, bBallCol, bPaddle, bScore):
    for brick in bBricks:
        if bBall.colliderect(brick):
            bScore += 5
            bBallRow *= -1
            bBricks.remove(brick) # removes the rectangle of the brick that was hit from the list of bricks
            break
    if bBall.colliderect(bPaddle):
        bBall.top = 560 * xu # ball can't go through brick
        bBallRow *= -1
    return bBricks, bBallRow, bBallCol, bBall, bScore

'''
The makeBreakOutLeaderBoard adds scores and usernames to a variable called bLeaderBoard in which the information is
stored as a 2D list. The list is sorted and then reverse so the higher scores come first in the list and will be displayed
at the top of the leader board in the drawScreen function.
'''
def makeBreakOutLeaderboard(bScore, bUserName, bLeaderBoard):
    bLeaderBoard.append([bScore, bUserName])
    bLeaderBoard.sort() # ascending order
    bLeaderBoard.reverse() # descending order
    bAddedToLeaderBoard = True
    if len(bLeaderBoard) > 10: # only the top 10 scores will be displayed on the screen in the drawScreen function
        del bLeaderBoard[-1]
    return bLeaderBoard, bAddedToLeaderBoard

#--------------Tetris Functions-----------------
'''
The makeTetrisBoard function creates a 2D list which is stored in the variable tetrisBoard. If a new block is being dropped, the old board
is stored in the tetrisBoard variable. This keeps the already fallen blocks in the 2D list rather than clearing it.
'''
def makeTetrisBoard(tOldBoard):
    if len(tOldBoard) == 0:
        tetrisBoard = []
        for i in range(15):
            tetrisBoard.append([0]*10)
    else:
        tetrisBoard = tOldBoard
    return tetrisBoard    
            
'''
The makeTetrisBlocks function has variables that store 2D lists which represet the different blocks.
'''
def makeTetrisBlocks():
    tRedBlock = [( 1, 1, 0), ( 0, 1, 1)]
    tOrangeBlock = [( 0, 0, 2), ( 2, 2, 2)]
    tGreenBlock = [( 0, 3, 3), ( 3, 3, 0)]
    tBlueBlock = [(4, 0, 0), (4, 4, 4)]
    tPurpleBlock = [( 0, 5, 0), ( 5, 5, 5)]
    return tRedBlock, tOrangeBlock, tGreenBlock, tBlueBlock, tPurpleBlock
    
'''
Each time the chooseTetrisBlock function is called, a random block within the list of blocks is returned.  It is called
when a block needs to be dropped and when the next block needs to be chosen.
'''
def chooseTetrisBlock():
    tRedBlock, tOrangeBlock, tGreenBlock, tBlueBlock, tPurpleBlock = makeTetrisBlocks()
    tBlocksList = [tRedBlock, tOrangeBlock, tGreenBlock, tBlueBlock, tPurpleBlock]
    tBlock = random.choice(tBlocksList)
    return tBlock

'''
The moveTetrisBlockDown function alters the variable tetrisBoard so the blocks can move down rows as well as right and left. It also deletes
the old blocks as the blocks fall so no pieces are left behind.
'''
def moveTetrisBlockDown(tBlock, tetrisBoard, tStartGame, tMoveBlockRow, tMoveBlockCol, tRotateBlock, tOldBoard, tPieceDoneMoving, keys, tGameOver):
    tBoardRows, tBoardCols = 15, 9
    
    if len(tRotateBlock) > 0: # player has pressed the 'r' key to rotate the block
        if tRotateBlock[-1] == True:
            tBlock = rotateTetrisBlock(tRotateBlock, tBlock) # calls function that will change the block to make it seem rotated when displayed    

    for r in range(len(tBlock)):
        for c in range(len(tBlock[r])):
            if len(tBlock) > 2: # move rotated (odd number of rotations) block  
                tetrisBoard[tMoveBlockRow - 3][int(tBoardCols/2.5 + c) + tMoveBlockCol] = 0 # removes old pieces
                tetrisBoard[tMoveBlockRow - 2][int(tBoardCols/2.5 + c) + tMoveBlockCol] = 0 # removes old pieces
                tetrisBoard[tMoveBlockRow - 1][int(tBoardCols/2.5 + c) + tMoveBlockCol] = tBlock[r-2][c]
                tetrisBoard[tMoveBlockRow][int(tBoardCols/2.5 + c) + tMoveBlockCol] = tBlock[r-1][c]                
                tetrisBoard[tMoveBlockRow + 1][int(tBoardCols/2.5 + c) + tMoveBlockCol] = tBlock[r][c]
            elif len(tBlock) <= 2: # move normal block or rotated (even number of rotations) block
                tetrisBoard[tMoveBlockRow - 2][tMoveBlockCol + int(tBoardCols/2.5 + c)] = 0 # removes old pieces                
                tetrisBoard[tMoveBlockRow - 1][tMoveBlockCol + int(tBoardCols/2.5 + c)] = 0 # removes old pieces
                tetrisBoard[tMoveBlockRow][tMoveBlockCol + int(tBoardCols/2.5 + c)] = tBlock[r-1][c]
                tetrisBoard[tMoveBlockRow + 1][tMoveBlockCol + int(tBoardCols/2.5 + c)] = tBlock[r][c]   
    return tetrisBoard

'''
The rotateTetrisBlock function changed the 2D list stored in the variable tBlock so the block appears to be rotated when displayed in the
drawScreen function.
'''
def rotateTetrisBlock(tRotateBlock, tBlock):
    tRedBlock, tOrangeBlock, tGreenBlock, tBlueBlock, tPurpleBlock = makeTetrisBlocks()  
    tNewBlock = []
    if tBlock == tRedBlock or tBlock == tGreenBlock: # S-shaped and L-shaped blocks only have two rotations
        if len(tRotateBlock) % 2 == 1: # odd number rotation
            for i in range(len(tBlock[0])):
                tNewBlock.append((tBlock[0][i],tBlock[1][i]))
        else: # returns to original shape
            tNewBlock.append(tBlock[1])
            tNewBlock.append(tBlock[0])
            
    elif tBlock == tOrangeBlock or tBlock == tBlueBlock or tBlock == tPurpleBlock: # blocks have four rotations
        if len(tRotateBlock) % 2 == 1: # odd rotation
            if len(tRotateBlock) % 3 == 0: # third rotation
                for i in range(len(tBlock[0])):
                    tNewBlock.append((tBlock[0][i],tBlock[1][i]))

            else: # first rotation
                for i in range(len(tBlock[0])):
                    tNewBlock.append((tBlock[1][i],tBlock[0][i]))

        elif len(tRotateBlock) % 2 == 0: # even rotation
            if len(tRotateBlock) % 4 == 0: # fourth rotation which is back to the original shape
                tNewBlock.append(tBlock[0])
                tNewBlock.append(tBlock[1])         

            else: # second rotation
                tNewBlock.append(tBlock[1])
                tNewBlock.append(tBlock[0])
    tBlock = tNewBlock # the new block is stored in the tBlock variable
    return tBlock    

#---------- Main Program Loop ----------
def main():
    hasChosen = False # player hasn't picked a game yet
    gameChosen = None # no game chosen
    pongScreen =  pygame.Rect(110*xu, 175*yu, 112*xu, 80*yu) # if player presses this rectangle, they will play Pong
    tetrisScreen = pygame.Rect(340*xu, 175*yu, 112*xu, 80*yu) # if player presses this rectangle, they will play Tetris
    blackoutScreen = pygame.Rect(570*xu, 175*yu, 112*xu, 80*yu) # if player presses this rectangle, they will play Break Out
    
    #if the game chosen is "Pong"
    pReadInstructionsBox = pygame.Rect(335*xu, 485*yu, 130*xu, 30*yu) # player presses to make pReadInstructions = True
    pReadInstructions = False # player hasn't read instuctions yet
    pReturnBox = pygame.Rect(w/20, 10*yu, 40*xu, 40*yu) # rectangle the player can press at any time to return to the arcade
    pPlayAgainBox = pygame.Rect(100*xu, 10*yu, 40*xu, 40*yu) # rectangle the player can press once the game is over to play again
    pGameOver = False # game isn't over
    pStartGame = False # becomes True when player presses the space key
    pRightHitLast = [False] # variable used to determine who earns a point
    pRightPlayerPoints, pLeftPlayerPoints = 0, 0 # number of points starts at zero
    pMoveBlockR, pMoveBlockL = 0, 0 # paddles haven't been moves
    pMoveBallRow, pMoveBallCol = 1, 1 # ball starts moving once the player starts the game
    pongBoard = makePongBoard() # makes the 2D list
    pBallRow, pBallCol, pBallVal = findPongBall(pongBoard) # locates the ball or the value 1 in the 2D list stored in the variable pongBoard
    pRightWins, pLeftWins = False, False # used to determine what messages will be displayed with the drawScreen function once the game has ended
    
    #if the game chosen is "Break Out"
    bReadInstructionsBox = pygame.Rect(335*xu, 485*yu, 130*xu, 30*yu) # player presses to make bReadInstructions = True
    bReturnBox = pygame.Rect(w/20, 10*yu, 40*xu, 40*yu) # rectangle the player can press at any time to return to the arcade
    bPlayAgainBox = pygame.Rect(100*xu, 10*yu, 40*xu, 40*yu) # rectangle the player can press once the game is over to play again
    bReadInstructions = False # player hasn't read instructions
    bStartGame = False # game hasn't started
    bBricks = makeBreakOutBricks() # makes the list of rectangles
    bPaddle = pygame.Rect(360*xu, 580*yu, 80*xu, 25*yu) # starting positions of the ball and paddle
    bBall = pygame.Rect(390*xu, 560*yu, 20*xu, 20*yu)
    bBallRow, bBallCol = -15*xu, 15*xu # ball starts moving once the player starts the game
    bNumLives = 3 # player starts with 3 lives
    bLoseLife = False # player hasn't lost any lives yet
    bGameOver = False # the game hasn't ended
    bScore = 0 # the player has zero points
    bLeaderBoard = [] # the leader board is an empty list
    bNameEntered = False # the player hasn't entered a name yet
    bUserName = "" # the player starts with no username
    bDoneBox = pygame.Rect(360*xu, 360*yu, 80*xu, 40*yu) # player clicks this rectangle after entering a name 
    bCheckLeaderBoard = False # player hasn't pressed the leader board box
    bAddedToLeaderBoard = False # score and username have not yet been added to the leader board
    
    #if the game chosen is "Tetris":
    tReadInstructionsBox = pygame.Rect(335*xu, 485*yu, 130*xu, 30*yu) # player presses to make tReadInstructions = True
    tReadInstructions = False # player hasn't read instructions
    tGameOver = False # game isn't over
    tStartGame = False # game hasn't started 
    tOldBoard = [] # the old board starts as an empty list
    tetrisBoard = makeTetrisBoard(tOldBoard) # makes a 2D list full of zeroes
    tBlock = chooseTetrisBlock() # chooses a random block
    tNextBlock = chooseTetrisBlock() # chooses another random block
    tMoveBlockRow, tMoveBlockCol = 0, 0 # block hasn't moved left or right yet
    tRotateBlock = [] # if player presses the 'r' key, the boolean True will be appended to this list. The length of this list determines which rotation the block should appear to be in when displayed in the drawScreen function
    tPieceDoneMoving = False # block hasn't stopped moving
    tBoardRows, tBoardCols = 15, 9 # length of tetrisBoard and length of the lists in tetrisBoard
    tLevel = 1 # player starts at level one
    tNumRowsUntilNextLevel = 1 # play needs to clear as many rows as the level they are on to move onto the next level
   
    while(True):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if (event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
                
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and hasChosen == False:
                if pongScreen.collidepoint(pygame.mouse.get_pos()): # player presses Pong screen
                    gameChosen = "Pong"
                    hasChosen = True
                elif tetrisScreen.collidepoint(pygame.mouse.get_pos()): # player presses Tetris screen
                    gameChosen = "Tetris"
                    hasChosen = True
                elif blackoutScreen.collidepoint(pygame.mouse.get_pos()): # player presses Black Out screen
                    gameChosen = "Break Out"
                    hasChosen = True
                    
            if gameChosen == "Pong":  
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    if pReadInstructionsBox.collidepoint(pygame.mouse.get_pos()): # player presses the read instructions box
                        pReadInstructions = True
                        
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    if pReturnBox.collidepoint(pygame.mouse.get_pos()):  # if player clicks button to return to arcade at any time the variables are reset
                        pReadInstructions = False
                        pGameOver= False
                        pStartGame = False
                        pRightHitLast = [False]
                        pRightPlayerPoints, pLeftPlayerPoints = 0, 0
                        pMoveBlockR, pMoveBlockL = 0, 0
                        pMoveBallRow, pMoveBallCol = 1, 1
                        pongBoard = makePongBoard()
                        pBallRow, pBallCol, pBallVal = findPongBall(pongBoard)
                        pRightWins, pLeftWins = False, False
                        hasChosen = False # player will be back in the arcade
                        gameChosen = None      
                        
                    elif pPlayAgainBox.collidepoint(pygame.mouse.get_pos()): # if player clicks button to play again once the game is over, the variables reset
                        pGameOver= False
                        pStartGame = False
                        pRightHitLast = [False]
                        pRightPlayerPoints, pLeftPlayerPoints = 0, 0
                        pMoveBlockR, pMoveBlockL = 0, 0
                        pMoveBallRow, pMoveBallCol = 1, 1
                        pongBoard = makePongBoard()
                        pBallRow, pBallCol, pBallVal = findPongBall(pongBoard)
                        pRightWins, pLeftWins = False, False   
                        
                if event.type==pygame.KEYDOWN and event.key == pygame.K_UP and pMoveBlockR-1 != -11: # moves right block up
                    pMoveBlockR -= 1
                    
                elif event.type==pygame.KEYDOWN and event.key == pygame.K_DOWN and pMoveBlockR+1 != 14: # moves right block down
                    pMoveBlockR += 1
                    
                if event.type==pygame.KEYDOWN and event.key == pygame.K_w and pMoveBlockL - 1 != -11: # moves left block up
                    pMoveBlockL -= 1
                    
                elif event.type==pygame.KEYDOWN and event.key == pygame.K_s and pMoveBlockL + 1 != 14: # moves left block down               
                    pMoveBlockL += 1
                    
                if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE and pReadInstructions == True: # player has read instructions and clicked the space key
                    pStartGame = True

                if pGameOver == True and pRightPlayerPoints != 11 and pLeftPlayerPoints != 11: # if the game has ended and no one has won, certain variables are reset so the game can continue
                    pGameOver = False
                    pRightHitLast = [False]
                    pMoveBallRow,pMoveBallCol = 1, 1
                    pongBoard = makePongBoard()
                    pBallRow,pBallCol, pBallVal = findPongBall(pongBoard) 
                    
                elif pGameOver == True or (pRightPlayerPoints != 11 and pLeftPlayerPoints != 11): # whoever reaches eleven points first wins
                    if pRightPlayerPoints == 11:
                        pRightWins = True
                    elif pLeftPlayerPoints == 11:
                        pLeftWins = True
                        
            elif gameChosen == "Tetris":
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    if tReadInstructionsBox.collidepoint(pygame.mouse.get_pos()): # player presses the read instructions box
                        tReadInstructions = True
                        
                if event.type==pygame.KEYDOWN and event.key == pygame.K_s and tReadInstructions == True: # player has pressed space key
                    tStartGame = True
                
                if tStartGame == True:
                    if event.type==pygame.KEYDOWN and event.key == pygame.K_RIGHT and ((tMoveBlockCol < 3 and len(tRotateBlock) % 2 != 1) or (tMoveBlockCol < 4 and len(tRotateBlock) % 2 == 1)) and tGameOver == False: # block can't keep moving right after hittin the right wall
                        for r in range(len(tBlock)):
                            for c in range(len(tBlock[r])):
                                if (tMoveBlockCol < 4 and len(tRotateBlock) % 2 == 1):
                                    tetrisBoard[tMoveBlockRow - 2][tMoveBlockCol + int(tBoardCols/2.5 - c)] = 0
                                if tetrisBoard[tMoveBlockRow][tMoveBlockCol + int(tBoardCols/2.5 - c)] == tBlock[r][c]:
                                    tetrisBoard[tMoveBlockRow][tMoveBlockCol + int(tBoardCols/2.5 - c)] = 0 # removes old pieces
                                if tetrisBoard[tMoveBlockRow - 1][tMoveBlockCol + int(tBoardCols/2.5 - c)] == tBlock[r][c]:
                                    tetrisBoard[tMoveBlockRow - 1][tMoveBlockCol + int(tBoardCols/2.5 - c)] = 0 # removes old pieces                                
                        tMoveBlockCol += 1 # block moves right
                    
                    elif event.type==pygame.KEYDOWN and event.key == pygame.K_LEFT and tMoveBlockCol > -3 and tGameOver == False: # block can't keep moving left after hitting the left wall
                        for r in range(len(tBlock)):
                            for c in range(len(tBlock[r])):
                                if (tMoveBlockCol > -2 and len(tRotateBlock) % 2 == 1):
                                    tetrisBoard[tMoveBlockRow - 2][tMoveBlockCol + int(tBoardCols/2.5 - c)] = 0                                
                                if tetrisBoard[tMoveBlockRow - 1][tMoveBlockCol + int(tBoardCols/2.5 + c + 1)] == tBlock[r][c]:
                                    tetrisBoard[tMoveBlockRow - 1][tMoveBlockCol + int(tBoardCols/2.5 + c + 1)] = 0 # removes old pieces
                                if tetrisBoard[tMoveBlockRow][tMoveBlockCol + int(tBoardCols/2.5 + c + 1)] == tBlock[r][c]:
                                    tetrisBoard[tMoveBlockRow][tMoveBlockCol + int(tBoardCols/2.5 + c + 1)] = 0 # removes old pieces
                        tMoveBlockCol -= 1 # block moves left
                            
                    if event.type==pygame.KEYDOWN and event.key == pygame.K_UP and tGameOver == False: # rotates block
                        for r in range(len(tBlock)):
                            for c in range(len(tBlock[r])):
                                tetrisBoard[tMoveBlockRow - 1][tMoveBlockCol + int(tBoardCols/2.5 + c + 1)] = 0 # removes old pieces
                                tetrisBoard[tMoveBlockRow][tMoveBlockCol + int(tBoardCols/2.5 + c + 1)] = 0 # removes old pieces  
                        tRotateBlock.append(True)
                                
                if tGameOver == True and event.type==pygame.KEYDOWN and event.key == pygame.K_p: # if player clicks the 'p' button to play again once the game is over, the variables reset
                    tGameOver = False
                    tStartGame = False
                    tOldBoard = []
                    tetrisBoard = makeTetrisBoard(tOldBoard)
                    tBlock = chooseTetrisBlock()
                    tNextBlock = chooseTetrisBlock()
                    tMoveBlockRow, tMoveBlockCol = 0, 0
                    tRotateBlock = []
                    tLevel = 1
                    tNumRowsUntilNextLevel = 1                    
                    tPieceDoneMoving = False                    
                    
                if event.type==pygame.KEYDOWN and event.key == pygame.K_q: # if player clicks the 'q' button to return to arcade at any time the variables are reset
                    tReadInstructionsBox = pygame.Rect(335*xu, 485*yu, 130*xu, 30*yu)
                    tReadInstructions = False
                    tGameOver = False
                    tStartGame = False
                    tOldBoard = []
                    tetrisBoard = makeTetrisBoard(tOldBoard)
                    tBlock = chooseTetrisBlock()
                    tNextBlock = chooseTetrisBlock()
                    tMoveBlockRow, tMoveBlockCol = 0, 0
                    tRotateBlock = []
                    tPieceDoneMoving = False
                    tLevel = 1
                    tNumRowsUntilNextLevel = 1                 
                    hasChosen = False
                    gameChosen = None 
                    
            elif gameChosen == "Break Out":
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    if bReadInstructionsBox.collidepoint(pygame.mouse.get_pos()): # player presses the read instructions box
                        bReadInstructions = True

                    # if player returns to the arcade or plays again, the data on the leader board is not removed
                    if bReturnBox.collidepoint(pygame.mouse.get_pos()): # if player clicks button to return to arcade at any time the variables are reset
                        bReadInstructionsBox = pygame.Rect(335*xu, 485*yu, 130*xu, 30*yu)
                        bReturnBox = pygame.Rect(w/20, 10*yu, 40*xu, 40*yu)
                        bPlayAgainBox = pygame.Rect(100*xu, 10*yu, 40*xu, 40*yu)
                        bReadInstructions = False
                        bStartGame = False
                        bBricks = makeBreakOutBricks()
                        bPaddle = pygame.Rect(360*xu, 580*yu, 80*xu, 25*yu)
                        bBall = pygame.Rect(390*xu, 560*yu, 20*xu, 20*yu)
                        bBallRow, bBallCol = -15*xu, 15*xu
                        bNumLives = 3
                        bLoseLife = False
                        bGameOver = False
                        bScore = 0
                        bNameEntered = False # if the player returns to the arcade and comes back to Break Out, they will have to enter a username again
                        bUserName = "" 
                        bDoneBox = pygame.Rect(360*xu, 360*yu, 80*xu, 40*yu)
                        bCheckLeaderBoard = False
                        bAddedToLeaderBoard = False
                        hasChosen = False # player will be back in the arcade
                        gameChosen = None                
                        
                if bNameEntered == False: # player hasn't entered name
                    if event.type==pygame.KEYDOWN and str(event.key).isalnum() and len(bUserName) < 9 and event.key != pygame.K_BACKSPACE and event.key != pygame.K_SPACE: # player can only have letters and numbers in their nine character-long username
                        bUserName += event.unicode.lower() # concatonates the keys the play pressed
                        
                    if event.type==pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and len(bUserName) > 0: # player can press backspace to remove characters from their username
                        bUserName = bUserName[0:len(bUserName) - 1]
                        
                    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and bDoneBox.collidepoint(pygame.mouse.get_pos()) and len(bUserName) < 10 and len(bUserName) > 0: # player has entered a good username and pressed the 'Done' rectangle
                        bNameEntered = True
                
                else:
                    if event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE and bReadInstructions == True: # player has entered name and clicked the space key
                        bStartGame = True   
                        
                    if bStartGame == True:
                        if keys[pygame.K_LEFT]:
                            bPaddle.right -= 25*xu
                            if bPaddle.left < 0: # paddle cannot move left after hitting the left wall
                                bPaddle.left = 0
                            
                        if keys[pygame.K_RIGHT]:
                            bPaddle.right += 25*xu
                            if bPaddle.right > 800*xu: # paddle cannot move right after hitting the right wall
                                bPaddle.right = 800*xu  
                                
                        if bNumLives == 0 or (bNumLives != 0 and len(bBricks) == 0): # game is over
                            bPaddle = pygame.Rect(360*xu, 580*yu, 80*xu, 25*yu)
                            bBall = pygame.Rect(390*xu, 560*yu, 20*xu, 20*yu)                        
                            bGameOver = True          
                            if bAddedToLeaderBoard == False:
                                bLeaderBoard, bAddedToLeaderBoard = makeBreakOutLeaderboard(bScore, bUserName, bLeaderBoard) # adds score and user name to leader board                       
                                
                        if bLoseLife == True and bNumLives != 0: # player loses a life but still has more than zero
                            bReturnBox = pygame.Rect(w/20, 10*yu, 40*xu, 40*yu)
                            bPaddle = pygame.Rect(360*xu, 580*yu, 80*xu, 25*yu)
                            bBall = pygame.Rect(390*xu, 560*yu, 20*xu, 20*yu)
                            bBallRow, bBallCol = -15*xu, 15*xu
                            bNumLives -= 1
                            bLoseLife = False
                            bGameOver = False
                            
                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and bPlayAgainBox.collidepoint(pygame.mouse.get_pos()) and bGameOver == True: # if player clicks button to play again once the game is over, the variables reset. Additionally, they will not have to choose another username.
                            bReturnBox = pygame.Rect(w/20, 10*yu, 40*xu, 40*yu)
                            bPlayAgainBox = pygame.Rect(100*xu, 10*yu, 40*xu, 40*yu)
                            bStartGame = False
                            bBricks = makeBreakOutBricks()
                            bPaddle = pygame.Rect(360*xu, 580*yu, 80*xu, 25*yu)
                            bBall = pygame.Rect(390*xu, 560*yu, 20*xu, 20*yu)
                            bBallRow, bBallCol = -15*xu, 15*xu
                            bNumLives = 3
                            bLoseLife = False
                            bGameOver = False
                            bScore = 0
                            bCheckLeaderBoard = False
                            bAddedToLeaderBoard = False

                        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and BTROPHY_RECT.collidepoint(pygame.mouse.get_pos()) and bGameOver == True: # player pressed key to check leader board
                            bCheckLeaderBoard = True                    

        # game logic goes here
        if pGameOver == False:
            blocks = makePongBlocks(pMoveBlockR, pMoveBlockL, pongBoard, pStartGame) # makes paddles
            if pStartGame == True:
                pBallRow, pBallCol, pNewBallRow, pNewBallCol, pMoveBallRow, pMoveBallCol, pGameOver, pLeftPlayerPoints, pRightPlayerPoints = movePongBall(pongBoard, pMoveBallRow, pMoveBallCol, pBallRow, pBallCol, pBallVal, pMoveBlockR, pMoveBlockL, pRightHitLast, pGameOver, pLeftPlayerPoints, pRightPlayerPoints)
                if pNewBallRow >= 0 and pNewBallCol >= 0 and pNewBallRow < pNumRows and pNewBallCol < pNumCols:
                    if pNewBallRow >= 0 and pNewBallCol >= 0 and pNewBallRow < pNumRows and pNewBallCol < pNumCols and pNewBallCol != 35 and pNewBallCol != 2 and pGameOver == False:
                        pongBoard = shortenPongBall(pongBoard)
                    elif pNewBallCol == 35: # ball in column that's before the column with the right paddle
                        if pongBoard[pNewBallRow][35] != -1 and (pNewBallRow != 26 and pongBoard[pNewBallRow+1][35] != -1):
                            pongBoard = shortenPongBall(pongBoard)
                        elif pNewBallRow == 26 and pongBoard[pNewBallRow+1][35] != -1:
                            pongBoard = shortenPongBall(pongBoard)
                    elif pNewBallCol == 2: # ball in column that's after the column with the left paddle
                        if pongBoard[pNewBallRow][2] != -1 and (pNewBallRow != 26 and pongBoard[pNewBallRow+1][2] != -1) and pongBoard[pNewBallRow-1][2] != -1:
                            pongBoard = shortenPongBall(pongBoard)
                        elif pNewBallRow == 26 and pongBoard[pNewBallRow+1][2] != -1:
                            pongBoard = shortenPongBall(pongBoard)
                        elif pNewBallRow != 26 and pongBoard[pNewBallRow][2] != -1 and pongBoard[pNewBallRow+1][2] == -1 and pongBoard[pNewBallRow-1][2] != -1:
                            pongBoard = shortenPongBall(pongBoard)
                
        if tStartGame == True:
            if tPieceDoneMoving == False:
                tetrisBoard = moveTetrisBlockDown(tBlock, tetrisBoard, tStartGame, tMoveBlockRow, tMoveBlockCol, tRotateBlock, tOldBoard, tPieceDoneMoving, keys, tGameOver)
            if tMoveBlockRow >= 13: # blocks hits bottom
                tPieceDoneMoving = True            
             
            for c in range(len(tBlock[-1])):
                if tMoveBlockRow < 13:    
                    if (tetrisBoard[tMoveBlockRow + 2][tMoveBlockCol + int(tBoardCols/2.5 + c)] > 0 or tetrisBoard[tMoveBlockRow + 2][tMoveBlockCol + int(tBoardCols/2.5 + 1)] > 0) and tetrisBoard[tMoveBlockRow + 1][tMoveBlockCol + int(tBoardCols/2.5 + c)] != 0: # block hits another block
                        tPieceDoneMoving = True
                    
                if (tMoveBlockRow == 1) and tetrisBoard[tMoveBlockRow + 2][tMoveBlockCol + int(tBoardCols/2.5 + c)] > 0: # block can't move down without hitting a block
                    tPieceDoneMoving = True
                    tGameOver = True # game is over
            
            if tPieceDoneMoving == True and tGameOver == False:
                tOldBoard = tetrisBoard # does not reset the tetrisBoard variable
                tetrisBoard = makeTetrisBoard(tOldBoard)                        
                tGameOver = False
                tBlock = tNextBlock # next block becomes the current block
                tNextBlock = chooseTetrisBlock() # randomly picks a new next block
                tMoveBlockRow, tMoveBlockCol = 0, 0
                tRotateBlock = []
                tPieceDoneMoving = False
                
            if tPieceDoneMoving == False: 
                tMoveBlockRow += 1  
                
            for r in range(len(tetrisBoard)):           
                if tetrisBoard[r].count(0) == 0: # if the row is filled with blocks
                    tNumRowsUntilNextLevel -= 1 # player needs to clear one less row to move up a leve l                 
                    del r # deletes the filled row
                    tetrisBoard.insert(0,tBoardCols*[0]) # adds a new row empty row
                    
            if tNumRowsUntilNextLevel == 0: # if the number of rows that player needs to clear equals zero, the player goes up a level
                tLevel += 1 # player moves up a level
                tNumRowsUntilNextLevel = tLevel # the number of rows the player needs to clear to move up a level equals their new level
                        
        if bGameOver == False: 
            if bStartGame == True:
                bBall, bBallRow, bBallCol, bLoseLife = moveBreakOutBall(bBall, bBallRow, bBallCol, bLoseLife)
                bBricks, bBallRow, bBallCol, bBall, bScore = breakOutBallCollides(bBricks, bBall, bBallRow, bBallCol, bPaddle, bScore) # checks for collisions 
                
        # drawing code goes here
        drawScreen(pReadInstructions, pongBoard, gameChosen, hasChosen, pMoveBlockR, pMoveBlockL, pStartGame, pLeftPlayerPoints, pRightPlayerPoints, pRightWins, pLeftWins, pGameOver, bStartGame, bReadInstructions, bBricks, bBall, bPaddle, bGameOver, bNumLives, bScore, bNameEntered, bUserName, bCheckLeaderBoard, bLeaderBoard, tStartGame, tReadInstructions, tBlock, tetrisBoard, tMoveBlockRow, tMoveBlockCol, tRotateBlock, tNextBlock, tGameOver, tLevel, tNumRowsUntilNextLevel)
        
        pygame.display.update()
        if gameChosen == "Pong" or gameChosen == "Break Out": # balls move fast
            clock.tick(12)
        elif gameChosen == "Tetris": # blocks move fairly slowly
            clock.tick(6)
            
main()