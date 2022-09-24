'''
Rand Hasan
HCP 11
CAPTCHA Test
'''

import pygame, sys, math, random
import Hasan_Pac-Man.py

#initialize game engine
pygame.init()

#Set up drawing surface
w = 600
h = 300
size=(w,h)
surface = pygame.display.set_mode(size)

#set window title bar
pygame.display.set_caption("Rand's CAPTCHA Test")

#Color constants
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED =   (178,34,34)
GREEN = (  0,255,  0)
BLUE =  (  0,  0,255)
YELLOW = (255,215,0)


#Initiate Test Images
test1 = pygame.image.load("test1.png").convert_alpha()
test2 = pygame.image.load("test2.png").convert_alpha()
test3 = pygame.image.load("test3.png").convert_alpha()
test4 = pygame.image.load("test4.png").convert_alpha()
test5 = pygame.image.load("test5.png").convert_alpha()
test6 = pygame.image.load("test6.png").convert_alpha()
test7 = pygame.image.load("test7.png").convert_alpha()
test8 = pygame.image.load("test8.png").convert_alpha()
test9 = pygame.image.load("test9.png").convert_alpha()
test10 = pygame.image.load("test10.png").convert_alpha()
test11 = pygame.image.load("test11.png").convert_alpha()
test12 = pygame.image.load("test12.png").convert_alpha()
test13 = pygame.image.load("test13.png").convert_alpha()
test14 = pygame.image.load("test14.png").convert_alpha()
test15 = pygame.image.load("test15.png").convert_alpha()

def drawScreen(test,guess,userGuessed,userRight,userWrong,numWrong,answer):
    xu = w/600
    yu = h/300
    surface.fill(WHITE)
    pygame.draw.rect(surface,RED,(10*xu,10*yu,xu*580,yu*280),0)
    pygame.draw.rect(surface,BLACK,(10*xu,10*yu,xu*580,yu*280),3)
    pygame.draw.rect(surface,WHITE,(20*xu,20*yu,560*xu,140*yu),0)
    pygame.draw.rect(surface,BLACK,(20*xu,20*yu,560*xu,140*yu),3)
    pygame.draw.rect(surface,YELLOW,(20*xu,170*yu,340*xu,110*yu),0)
    pygame.draw.rect(surface,BLACK,(20*xu,170*yu,340*xu,110*yu),3)
    pygame.draw.rect(surface,WHITE,(30*xu,215*yu,320*xu,30*yu),0)
    pygame.draw.rect(surface,BLACK,(30*xu,215*yu,320*xu,30*yu),3)
    #take test
    takeTestText, takeTestBounds = showMessage("Type the word:",15, 100*xu, 200*yu,BLACK)
    displayGuessText, displayGuessBounds = showMessage(guess, 15, 80*xu, 230*yu,BLACK)
    surface.blit(displayGuessText, displayGuessBounds)
    surface.blit(takeTestText, takeTestBounds)    
    #check answer button
    pygame.draw.rect(surface,WHITE,(375*xu,210*yu,30*xu,30*yu),0)
    pygame.draw.rect(surface,BLACK,(375*xu,210*yu,30*xu,30*yu),3)
    finishedTestText, finishedTestBounds = showMessage("    ",20,390*xu,225*yu,WHITE)
    surface.blit(finishedTestText, finishedTestBounds)
    pointList1=([382*xu,226*yu],[388*xu,234*yu],[398*xu,216*yu])
    pygame.draw.lines(surface,BLACK,False,pointList1,3)
    #retake test button
    pygame.draw.rect(surface,WHITE,(375*xu,245*yu,30*xu,30*yu),0)
    pygame.draw.rect(surface,BLACK,(375*xu,245*yu,30*xu,30*yu),3)
    retakeTestText, retakeTestBounds = showMessage("    ",20,390*xu,260*yu,WHITE)
    surface.blit(retakeTestText, retakeTestBounds)    
    pygame.draw.arc(surface,BLACK,(380*xu,250*yu,20*xu,20*yu),math.pi/2,math.pi*2,3)
    pointList2=([388*xu,249*yu],[393*xu,252*yu],[388*xu,255*yu])
    pygame.draw.lines(surface,BLACK,False,pointList2,3)
    #display test images
    displayTest(test)
    #users guess was right
    if userGuessed == True:
        if userRight == True:
            userRightText,userRightBounds = showMessage("You passed the test!", 20,475*xu,190*yu,WHITE,BLACK)
            surface.blit(userRightText,userRightBounds)
        
        #users guess was wrong
        if userWrong == True and numWrong<3:
            userWrongText,userWrongBounds = showMessage("You failed the test!", 20,475*xu,190*yu,WHITE,BLACK)
            surface.blit(userWrongText,userWrongBounds)
            tryAgainText,tryAgainBounds = showMessage("Try Again!", 15,475*xu,220*yu,WHITE,BLACK)
            surface.blit(tryAgainText,tryAgainBounds)
            numWrongText,numWrongBounds = showMessage("Times failed: "+str(numWrong), 15,475*xu,265*yu,WHITE,BLACK)
            surface.blit(numWrongText,numWrongBounds)
        #user continues guessing wrong
        if numWrong==3:
            userWrongText,userWrongBounds = showMessage("You failed the test!", 20,475*xu,190*yu,WHITE,BLACK)
            surface.blit(userWrongText,userWrongBounds)  
            numWrongText,numWrongBounds = showMessage("Times failed: "+str(numWrong), 15,475*xu,265*yu,WHITE,BLACK)
            surface.blit(numWrongText,numWrongBounds)
            

def chooseTest():
    testList = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11,test12,test13,test14,test15]
    test = random.choice(testList)
    return test

def displayTest(test):
    surface.blit(test,[200,45])
    
def displayGuess(guess):
    guess = " ".join(guess)
    return guess
       
def showMessage(message,size,x,y,color,bg=None):
    font = pygame.font.SysFont("Arial",size,True,False)
    text = font.render(message,True,color,bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text,textBounds

def findAnswer(test,answer,userGuessed):
    if userGuessed == True:
        if test == test1:
            answer = "cralsist"
        if test == test2:
            answer = "flirc"
        if test == test3:
            answer = "vedsho"
        if test == test4:
            answer = "trapperb"
        if test == test5:
            answer = "wrans"
        if test == test6:
            answer = "unnedou"
        if test == test7:
            answer = "unrexc"
        if test == test8:
            answer = "ejujle"
        if test == test9:
            answer = "tegunt"
        if test == test10:
            answer = "plicrom"
        if test == test11:
            answer = "valite"
        if test == test12:
            answer = "unbachar"
        if test == test13:
            answer = "aphxleci"
        if test == test14:
            answer = "dultne"
        if test == test15:
            answer = "sonated"
        return answer
    
    
def main():
    xu = w/600
    yu = h/300  
    #initialize variables
    guess  = ""
    answer = ""
    userGuessed = False
    test = chooseTest()
    userRight = False
    userWrong = False
    numWrong = 0    
    list1 = []
    #text bounds
    takeTestText, takeTestBounds = showMessage("Type the word:",15, 100*xu, 200*yu,BLACK)
    displayGuessText, displayGuessBounds = showMessage(guess, 15, 80*xu, 230*yu,BLACK)    
    finishedTestText, finishedTestBounds = showMessage("    ",20,390*xu,225*yu,WHITE)
    retakeTestText, retakeTestBounds = showMessage("    ",20,390*xu,260*yu,WHITE)
    userRightText,userRightBounds = showMessage("You passed the test!", 20,475*xu,190*yu,WHITE,BLACK)
    userWrongText,userWrongBounds = showMessage("You failed the test!", 20,475*xu,190*yu,WHITE,BLACK)
    tryAgainText,tryAgainBounds = showMessage("Try Again!", 15,475*xu,220*yu,WHITE,BLACK)
    numWrongText,numWrongBounds = showMessage("Times failed: "+str(numWrong), 15,475*xu,265*yu,WHITE,BLACK)
    
    while(True):
        for event in pygame.event.get():
            if( event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()     
                
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if retakeTestBounds.collidepoint(pygame.mouse.get_pos()) and numWrong<3 and guess!="" and userGuessed==True:                
                    test = chooseTest()
                    displayTest(test)
                    if userRight == True:
                        guess  = ""
                        answer = ""
                        userGuessed = False
                        userWrong = False
                        numWrong = 0    
                        list1 = [] 
                        userRight = False
                    if userWrong == True:
                        guess  = ""
                        answer = ""
                        userGuessed = False  
                        list1 = [] 
                        userRight = False
                        userWrong = False
                
            if event.type==pygame.KEYDOWN and event.key >= pygame.K_a and event.key<= pygame.K_z and len(list1)<9 and userGuessed == False and numWrong<3:
                guess += event.unicode.lower()
                list1.append(event.unicode.lower())
                
            if event.type==pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and guess!="" and userGuessed == False and numWrong<3:
                del list1[-1]
                guess = "".join(list1)
                
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if finishedTestBounds.collidepoint(pygame.mouse.get_pos()) and numWrong<3 and guess!="":
                    userGuessed = True
                    answer = findAnswer(test,answer,userGuessed)
                    if answer == guess:
                        userRight = True
                    else:
                        userWrong = True
                        numWrong+=1
                        
        # drawing code goes here
        drawScreen(test,guess,userGuessed,userRight,userWrong,numWrong,answer)
        pygame.display.update()
main()