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
pygame.display.set_caption("Rand Hasan's Slots")

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
def drawScene(userCredits,userBet,icon1,icon2,icon3,winnings,gamesPlayed):
    surface.fill(WHITE)
    surface.blit(slot_machine, [0, 0])
    userCreditsText, userCreditBounds = showMessage(" Credits: "+ str(userCredits)+" ",25,15*w/20,h/10,WHITE,BLACK)
    userBetText, userBetBounds = showMessage(" Bet: "+ str(userBet)+" ",25, 5*w/10, 8.75*h/10,WHITE,BLACK)
    userBetDirectionsText, userBetDirectionsBounds = showMessage(" Use up and down arrows to change bet ",15,5*w/10,9.5*h/10,WHITE,BLACK)
    userEnterDirectionsText, userEnterDirectionsBounds = showMessage(" Press enter to play! ",25,5*w/10,5*h/10,WHITE,BLACK)        
    #blit all messages to the screen
    surface.blit(userCreditsText, userCreditBounds)
    surface.blit(userBetText, userBetBounds)
    surface.blit(userBetDirectionsText, userBetDirectionsBounds)
    surface.blit(userEnterDirectionsText, userEnterDirectionsBounds)
    displayIcons(icon1,icon2,icon3)
    gamesPlayedText,gamesPlayedBounds = showMessage(" Games Played: "+ str(gamesPlayed) + " ", 18, 2*w/9, h/10, WHITE,BLACK) #a message that displays the # of games the user has played
    surface.blit(gamesPlayedText,gamesPlayedBounds)
    if userCredits==0 or userCredits<0:
        #blits game over message
        gameOverText, gameOverTextBounds = showMessage(" Game Over ",50,5*w/10,5*h/10,RED,BLACK)        
        surface.blit(gameOverText, gameOverTextBounds)
        buyCredsText,buyCredsBounds = showMessage(" Buy Credits ", 20,8*w/10, 8.75*h/10,BLUE,BLACK)
        surface.blit(buyCredsText,buyCredsBounds)
    if winnings>0:
        surface.blit(coin_image,[145,253])
        
def showMessage(message,size,x,y,color,bg=None):
    font = pygame.font.SysFont("Arial",size,True,False)
    text = font.render(message,True,color,bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text,textBounds

def spinMachine():
    iconsList =  [seven_icon,banana_icon,banana_icon,banana_icon,banana_icon,bar_icon,bell_icon,cherry_icon,grape_icon,lemon_icon,orange_icon,watermelon_icon,watermelon_icon,watermelon_icon]
    #banana and watermelon icons are more likely to appear than other icons
    icon1 = random.choice(iconsList)
    icon2 = random.choice(iconsList)
    icon3 = random.choice(iconsList)
    return icon1,icon2,icon3
    
def displayIcons(icon1,icon2,icon3):  
    surface.blit(icon1,[37,124])
    surface.blit(icon2,[145,124])
    surface.blit(icon3,[254,124])
    
def userBet(userCredits,event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        if userCredits-userBet>1 or userCredits-userBet==1:
            userBet+=1
                
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        if (userBet>1 or userBet==1) and (userCredits-userBet)!=0:
            userBet-=1
    
def getWinnings(userBet,icon1,icon2,icon3):
    if (icon1==icon2==icon3 and icon1 == cherry_icon) or (icon1==icon2==icon3 and icon1 == grape_icon):
        return (userBet*3)+5 #user gets an extra bonus of 5 credits if the three icons are all grapes or all cherries
    
    elif icon1==icon2==icon3:
        return userBet*3
    
    elif (icon1 == icon2 and icon1 == cherry_icon) or (icon2==icon3 and icon2 == cherry_icon) or (icon3==icon1 and icon3 == cherry_icon):
        return (userBet*2)+5 #user gets an extra bonus of 5 credits if two of the icons are cherries
    
    elif (icon1 == icon2 and icon1 == grape_icon) or (icon2==icon3 and icon2 == grape_icon) or (icon3==icon1 and icon3 == grape_icon):
        return (userBet*2)+5 #user gets an extra bonus of 5 credits if two of the icons are grapes
    
    elif (icon1 == icon2 or icon2==icon3 or icon1 == icon3):
        return userBet*2
    
    else:
        return userBet*(-1)
    
def gamesPlayed():
    gamesPlayed = 0
#----------------main program loop----------------
def main():
    userCredits = 10
    userBet = 1    
    #data initializations (model)
    spin = False
    icon1 = placeholder_image
    icon2 = placeholder_image
    icon3 = placeholder_image
    winnings = 0
    buyCredsText,buyCredsBounds = showMessage(" Buy Credits ", 25,4*w/4.8, 8.75*h/10,BLUE,BLACK)
    gamesPlayed = 0
    gamesPlayedText,gamesPlayedBounds = showMessage(" Games Played: "+ str(gamesPlayed) + " ", 20, w/5, h/9, WHITE,BLACK)
    
    #main program loop
    while(True):
        #controller code
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                print("exit")
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                winnings = 0
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if not userCredits == 0 or userCredits<0:
                    icon1,icon2,icon3 = spinMachine()
                    displayIcons(icon1,icon2,icon3)
                    winnings = getWinnings(userBet,icon1,icon2,icon3)
                    userCredits += winnings
                if userBet > userCredits:
                    userBet = 1
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if userCredits-userBet>1 or userCredits-userBet==1:
                    userBet+=1
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if (userCredits-userBet>0 or userCredits-userBet==0) and userBet>1:
                    userBet-=1
                if userCredits < userBet:
                    userBet =1
                    
        
        #user can buy 10 credits when game is over       
            if userCredits == 0 or userCredits < 0:
                gameOver = True
                userBet = 0
                mouseOver = False
                if gameOver == True:
                    if buyCredsBounds.collidepoint(pygame.mouse.get_pos()):
                        mouseOver = True
                        if(event.type==pygame.MOUSEBUTTONDOWN and event.button==1):
                            gamesPlayed+=1
                            userCredits = 10
                            userBet = 1    
                            #resets data
                            spin = False
                            icon1 = placeholder_image
                            icon2 = placeholder_image
                            icon3 = placeholder_image
                            winnings = 0                                

        #draw the view
        drawScene(userCredits,userBet,icon1,icon2,icon3,winnings,gamesPlayed)
        #updates screen
        pygame.display.update()
main()