'''
Rand Hasan
HCP 11
Pygame Emoji Adventure Story Program
In this program, the user will go through an interactive adventure story and travel a path to get to their Grandma's house.
Credits: Luke Szfranski, Mrs. Klosky for starter template code.
Note: all images must be saved to same directory as this python file.
'''

import pygame, sys, math,random
#Initializing game engine
pygame.init()

#Set up drawing surface
w = 640
h = 550
size = (w,h)
surface = pygame.display.set_mode(size)

#Set window title bar
pygame.display.set_caption("Rand Hasan's Adventure Story")

#Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARKGREEN = (25, 109, 0)

#Set Rectangle bounds of where Left and right decision images will be located- use pygame.RECT
LEFT= pygame.Rect(w/8,3*h/8,250,250)
RIGHT= pygame.Rect(5.5*w/8,3*h/8,250,250)
MIDDLE=pygame.Rect(3.25*w/8,h/8,250,250)

'''
draws boxes & border around the drawing surface for the game
function written by Luke Szfranski
'''
def drawBorder():
    pygame.draw.rect(surface,DARKGREEN,(0,2*h/3,w,h/3),0)
    pygame.draw.rect(surface,BLACK,(0,0,w,20),0)
    pygame.draw.rect(surface,BLACK,(0,0,20,h),0)
    pygame.draw.rect(surface,BLACK,(0,h-20,w,20),0)
    pygame.draw.rect(surface,BLACK,(w-20,0,20,h),0)
    pygame.draw.rect(surface,BLACK,(0,2*h/3,w,20),0)

'''
displays text left aligned at the line location specified. words display in specified size
  words- the text to display
  line- either UPPERLINE, MIDDLELINE, LOWERLINE
  size- integer value of text size
'''
def displayText(words,line,size):
    font = pygame.font.SysFont('Arial',size,1,0)
    text = font.render(words,1,WHITE)
    bounds = text.get_rect()
    bounds.topleft = line
    surface.blit(text,bounds)
    
'''
displays an image file picture at the location specified
   location- tuple of x,y values of where to place the picture
   picture- image filename 
'''
def displayPicture(picture,location):
    surface.blit(pygame.image.load(picture).convert_alpha(),location)
    
'''
returns 3-picture tuple of the main image and two choices for the next level (level below current level)
   levelcode- next level of game to be played
'''
def getPictures(levelCode):
    
    if levelCode=="1":
        return ("runner.png","grandma.png","biker.png")
    if levelCode=="2A":
        return ("creek.png","thirsty.png","gas-station.png")
    if levelCode=="2B":
        return ("back.png","lost.png","map.png")
    if levelCode=="2C":
        return ("hammer.png","chains.png","walker.png")
    if levelCode=="2D":
        return ("go.png","rain.png","building.png")
    if levelCode=="3A":
        return ("shirt.png","throwing-up.png","stink.png")
    if levelCode=="3B":
        return ("mad.png","purchase.png","gift.png")
    if levelCode=="3C":
        return ("fire-department.png","fire.png","fire-extinguisher.png")
    if levelCode=="3D":
        return ("go.png","astonished.png","back.png")
    if levelCode=="3E":
        return ("phone.png","house.png","magnifying-glass.png")
    if levelCode=="3F":
        return ("home.png","tired.png","thumb.png")
    if levelCode=="3G":
        return ("ambulence.png","foot.png","baby-crawl.png")
    if levelCode=="3H":
        return ("talk.png","surprised.png","looking.png")
    if levelCode=="4A":
        return ("end.png","freeze.png","end.png")
    if levelCode=="4B":
        return ("end.png","raccoon.png","end.png")
    if levelCode=="4C":
        return ("end.png","water.png","end.png")
    if levelCode=="4D":
        return ("end.png","chocolates.png","end.png")
    if levelCode=="4E":
        return ("end.png","fire-fighter.png","end.png")
    if levelCode=="4F":
        return ("end.png","burnt-house.png","end.png")
    if levelCode=="4G":
        return ("end.png","dream.png","end.png")
    if levelCode=="4H":
        return ("end.png","turkey.png","end.png")
    if levelCode=="4I":
        return ("end.png","police.png","end.png")
    if levelCode=="4J":
        return ("end.png","mount-fuji.png","end.png")
    if levelCode=="4K":
        return ("end.png","sad.png","end.png")
    if levelCode=="4L":
        return ("end.png","alien.png","end.png")
    if levelCode=="4M":
        return ("end.png","hospital.png","end.png") 
    if levelCode=="4N":
        return ("end.png","woods.png","end.png")
    if levelCode=="4O":
        return ("end.png","night.png","end.png")
    if levelCode=="4P":
        return ("end.png","employee.png","end.png")  

    return (leftPic,middlePic, rightPic)
 
'''
    returns the game text at the current level
       levelCode- current level
'''
def getLevelText(levelCode):
    if levelCode=="1":
        return "You're off to your grandma's house to see her before she leaves for vacation.How do you travel to her house that is deep in the woods?Do you run or bike?"
    if levelCode=="2A":
        return "After running for forever under the hot sun, you become dehydrated.You desperately need water but how are you going to get it?Drink water from a nearby creek or try to get water at a nearby gas station?"
    if levelCode=="2B":
        return "You're lost. What do you do?Go back and go the other way or check your phone and look at the map?"
    if levelCode=="2C":
        return "Your bike chains have jammed.What do you do?Attempt to fix the jam or walk your bike all the way to grandma's house?"
    if levelCode=="2D":
        return "It's pouring outside and might not be safe to bike.What will you do?Keep biking or bike to the nearest building?"
    if levelCode=="3A":
        return "You get sick because of the creek water and throw up all over your clothes.You really stink so what are you going to do?Do you take your jacket covered in throw up off or just keep it on and stink?"
    if levelCode=="3B":
        return "An employee says you must purchase something in order to get free water.Do you argue with the employee or buy grandma a gift in order to get free water?"
    if levelCode=="3C":
        return "You realize that you originally went the wrong way but fix your mistake.When you arrive, you see that grandma's house is on fire, what do you do?Call the fire department or try to take the fire out yourself?"
    if levelCode=="3D":
        return "You drop your phone and shatter the screen.Now it won't turn on!What will you do?Keep going straight or retrace your steps and go back?"
    if levelCode=="3E":
        return "Success, you've made it to grandma's house.Her door is wide-open but all of the lights are turned off, what will you do?Will you stay outside and call grandma or go inside and investigate?"
    if levelCode=="3F":
        return "You get really tired and just want to go home.Will you leave your bike and walk back home or hitchhike?"
    if levelCode=="3G":
        return "You slip less than a mile away from grandma's and hurt your foot.What will you do?Will you call the ambulance or crawl to grandma's?"
    if levelCode=="3H":
        return "The nearest building is a hotel and you go inside and wait for it to stop raining.When it stops, you go outside to get your bike but it's gone, what do you do?Tell an employee or look around the hotel for your missing bike?"
    if levelCode=="4A":
        return "You get really cold and are still pretty far from grandma's.You end up freezing."
    if levelCode=="4B":
        return "Your jacket on manages to keep you warm.Unfortunately the smell of throw up attracts a large group of hungry raccoons."
    if levelCode=="4C":
        return "Your argument leaves the employee flabberghasted an earns you free water.You are then back on your way to grandma's house."
    if levelCode=="4D":
        return "You buy your grandma some chocolates in order to get a free cup of water.  Unfortunately, you end up spending all of your months allowance."
    if levelCode=="4E":
        return "The fire department comes in a flash and saves the day.They also let you and grandma ride in the truck with them for the rest of the day."
    if levelCode=="4F":
        return "You try to take out the fire but can't so your grandma calls the fire department.They come and take out the fire but the house is badly burnt and collapses."
    if levelCode=="4G":
        return "You keep going until you wake up and realize that this was all a dream."
    if levelCode=="4H":
        return "You go back and meet a wild turkey which charges after you."
    if levelCode=="4I":
        return "You call your grandma who tells you that there are burglars in the house.You call the police and save the day."
    if levelCode=="4J":
        return "You go inside the house and see that there are burglars.They kidnap you and take you to Mount Fuji."
    if levelCode=="4K":
        return "Once you get home you ask your parents to pick up your bike.You are safe and sound but don't get to see grandma until next summer."
    if levelCode=="4L":
        return "An alien picks you up and abducts you.The alien takes you to their planet."
    if levelCode=="4M":
        return "You are taken to the hospital and your grandma visits you and brings cookies.You have a great time but forget about your bike and never see it again."
    if levelCode=="4N":
        return "By the time you get to grandma's, you see that she's already left for vacation.You are stuck all alone in the deep and dark woods."
    if levelCode=="4O":
        return "An employee checked the cameras but couldn't find any footage.You had to wait there until 10 PM which was too late to see grandma."
    if levelCode=="4P":
        return "You look around and see that an employee took your bike to the hotel's garage.You pick up your bike and are back on your way to grandma's."

'''
returns the next game level based on the currentLevel and choice made
   choice- either 'left' or 'right'
'''
def getNextLevel(currentLevel, choice):
    if (currentLevel=="1" and choice=="left"):
        return random.choice(("2A","2B"))
    if (currentLevel=="1" and choice=="right"):
        return random.choice(("2C","2D"))
    if (currentLevel=="2A" and choice=="left"):
        return "3A"
    if (currentLevel=="2A" and choice=="right"):
        return "3B"
    if (currentLevel=="3A" and choice=="left"):
        return "4A"    
    if (currentLevel=="3A" and choice=="right"):
        return "4B"
    if (currentLevel=="3B" and choice=="left"):
        return "4C"
    if (currentLevel=="3B" and choice=="right"):
        return "4D"
    if (currentLevel=="2B" and choice=="left"):
        return "3C"
    if (currentLevel=="2B" and choice=="right"):
        return "3D"
    if (currentLevel=="3C" and choice=="left"):
        return "4E"
    if (currentLevel=="3C" and choice=="right"):
        return "4F"
    if (currentLevel=="3D" and choice=="left"):
        return "4G"
    if (currentLevel=="3D" and choice=="right"):
        return "4H"
    if (currentLevel=="1" and choice=="right"):
        return random.choice(("2C","2D"))
    if (currentLevel=="2C" and choice=="left"):
        return "3E"    
    if (currentLevel=="2C" and choice=="right"):
        return "3F"
    if (currentLevel=="2D" and choice=="left"):
        return "3G"
    if (currentLevel=="2D" and choice=="right"):
        return "3H"
    if (currentLevel=="3E" and choice=="left"):
        return "4I"
    if (currentLevel=="3E" and choice=="right"):
        return "4J"
    if (currentLevel=="3F" and choice=="left"):
        return "4K"
    if (currentLevel=="3F" and choice=="right"):
        return "4L"
    if (currentLevel=="3G" and choice=="left"):
        return "4M"
    if (currentLevel=="3G" and choice=="right"):
        return "4N"
    if (currentLevel=="3H" and choice=="left"):
        return "4O"
    if (currentLevel=="3H" and choice=="right"):
        return "4P"
    
        
'''
returns the 3 sentences of the text to display
pre: line must be at least 2 sentences long; 
     1st sentence must end in a period.  
     If 3 sentences, 2nd must end in a ?
     
post:  first sentence will end with a period 
       second sentence will end with a question mark (if not end of game)
       third sentence will contain any remaining text (if it exists)
'''
def splitText(line):
    period1=line.find('.')
    sentence1=line[0:period1+1]
    questionMark=line.find('?')
    if questionMark!=-1:  #found a ?
        sentence2=line[period1+1:questionMark+1]
        sentence3=line[questionMark +1:]
    else:
        sentence2=line[period1+1:]
        sentence3=""
    return sentence1,sentence2,sentence3
    
'''
draws all of the game screen
'''
def drawScreen(gameStage):
     #placement of 3 text labels
    UPPERLINE =  (w/20,35* h/48)
    MIDDLELINE = (w/20,77* h/96)
    LOWERLINE =  (w/20,42* h/48)
    
    drawBorder()
    
    #get level images and text to display
    gameText= getLevelText(gameStage)

    #split gametext to 3 lines for output using slices
    first, second, last = splitText(gameText)
    displayText(first,  UPPERLINE, 16)
    displayText(second, MIDDLELINE, 16)
    displayText(last,   LOWERLINE, 16)
    
    #returns tuple with 3 pix for that level (leftpicture, middlepicture, rightpicture)
    picsToDisplay=getPictures(gameStage) 
    displayPicture(picsToDisplay[0],LEFT) 
    displayPicture(picsToDisplay[1],MIDDLE)
    displayPicture(picsToDisplay[2],RIGHT)
     


#*------------------------------------------ MAIN PROGRAM LOOP----------------------------------*

#story starts at stage 1
stage = "1"

while(True):
    for event in pygame.event.get():
        if((event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            pygame.quit()
            sys.exit()
            
        #add code here for mouse click detection & collision check
        #code will check collision with the LEFT and RIGHT RECT objects and getNextLevel() of the game to execute
        
        if(event.type==pygame.MOUSEBUTTONDOWN and event.button==1):
            if LEFT.collidepoint(pygame.mouse.get_pos()):
                stage = getNextLevel(stage, "left")
            
        if(event.type==pygame.MOUSEBUTTONDOWN and event.button==1):
            if RIGHT.collidepoint(pygame.mouse.get_pos()):
                stage = getNextLevel(stage, "right")
            
        #was mouse clicked inside of LEFT or RIGHT Picture?
            
   
    #Set Background Fill
    surface.fill(WHITE)
    
    #Drawing code goes here
    drawScreen(stage) 
   
    pygame.display.update()
