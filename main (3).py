# the following code will always put the screen in the top corner
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
import random
from pygame import * 
mixer.init()
init()
size = width, height = 1000, 700
screen = display.set_mode(size)
button = 0
# defining colours
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW=(255,255,0)
flashyellow=(255,251,5)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
mouse1=1
mouse2=1
cccc=2
yyyy=0
time1=0
speed1=0
speed2=0
pagec=0
hightestscore=0
mylist=[]
reccords=[]
files="in0.dat"
dd=  mixer.Sound('dead.mp3')
ouch =  mixer.Sound('song22.mp3')
sz= mixer.Sound('soundz2.mp3')
def falshsound():
    mixer.Sound.play(ouch)
       

def historys():
    global score,num,reccords,numFile,text
    numFile = open(files, "r")
    reccords=[]
    while True:
        text = numFile.readline()
        #rstrip removes the newline character read at the end of the line
        text = text.rstrip("\n")     
        if text=="": 
            break
        reccords.append(int(text))
        
        
    # Writing to a file
    numFile = open (files, "w")
    num = score 
    reccords.append(num) #\n forces the input onto another line
    reccords.sort()
    for i in reccords:
      numFile.write(str(i) + "\n")
    # Reading from a file
    numFile = open(files, "r")
    while True:
        text = numFile.readline()
        #rstrip removes the newline character read at the end of the line
        text = text.rstrip("\n")     
        if text=="": 
            break
        reccords.sort()
        
    numFile.close()    

random1=random.randint(0,950)
random2=random.randint(0,950)
random3=random.randint(0,650)
random4=random.randint(0,650)
while abs(random1-random2)<50 or abs(random3-random4)<50:
    random1=random.randint(0,950)
    random2=random.randint(0,950)    
    random3=random.randint(0,650)
    random4=random.randint(0,650)
countkey=0
score=0
flashcd=400
flashx=flashy=0
missilespeed=speed1
missilespeed2=speed2
startpage=True
menupage=False
game=False
endpage=False
menub=image.load("menu2.png") 
backgroundPic = image.load("8359905.webp")
# scale the image
backgroundPic = transform.scale(backgroundPic, (width, height))
endpage1=image.load("teemo.webp")
startpage1=image.load("hhh2.jpg")
def BACKGROUND(screen, button, backx):
    # left side
    screen.blit(backgroundPic, Rect(backx,0,width,height))    #draw the picture
    # right side
    screen.blit(backgroundPic, Rect(backx + width, 0, width, height))
    
  
# movement key booleans
PRESS_RIGHT = False
PRESS_LEFT = False
PRESS_UP = False
PRESS_DOWN = False
PRESS_SPACE = False


myFont = font.SysFont("Times New Roman",30)
# load image
shipPic = image.load("heimer3.png")
shipPic = transform.scale(shipPic, (shipPic.get_width()//25, shipPic.get_height()//25))
flash = image.load("flash.png.png")
flash = transform.scale(flash, (flash.get_width()//7, flash.get_height()//7))

def displayt(s,x,y,c,te):  #make a function to show the text in the pygame output screen
  myFont2 = font.SysFont("Times New Roman",s)
  string =te
  text = myFont2.render(string, 1, c)
  size = myFont2.size(string)
  screen.blit(text, (x,y, size[0], size[1]))
  
def flashcheck():
    global flashx,flashy,shipX,shipY
    flashx=int(shipX)
    flashy=int(shipY)
    return flashx and flashy
def flash1():
    draw.circle(screen,flashyellow,(random.randint(flashx+40,flashx+60),random.randint(flashy+40,flashy+60)),1)
    draw.circle(screen,flashyellow,(random.randint(flashx+40,flashx+60),random.randint(flashy+40,flashy+60)),1)
    draw.circle(screen,flashyellow,(random.randint(flashx+40,flashx+60),random.randint(flashy+40,flashy+60)),1)
    draw.circle(screen,flashyellow,(random.randint(flashx+40,flashx+60),random.randint(flashy+40,flashy+60)),1)
    draw.circle(screen,flashyellow,(random.randint(flashx+40,flashx+60),random.randint(flashy+40,flashy+60)),1)
    draw.circle(screen,flashyellow,(random.randint(flashx+40,flashx+60),random.randint(flashy+40,flashy+60)),1)   
    draw.circle(screen,flashyellow,(random.randint(flashx+40,flashx+60),random.randint(flashy+40,flashy+60)),1)
    draw.circle(screen,flashyellow,(random.randint(flashx+40,flashx+60),random.randint(flashy+40,flashy+60)),1)     
    draw.circle(screen,flashyellow,(random.randint(flashx+30,flashx+70),random.randint(flashy+30,flashy+70)),1)    
    draw.circle(screen,flashyellow,(random.randint(flashx+30,flashx+70),random.randint(flashy+30,flashy+70)),1)
    draw.circle(screen,flashyellow,(random.randint(flashx+30,flashx+70),random.randint(flashy+30,flashy+70)),1)
    draw.circle(screen,flashyellow,(random.randint(flashx+30,flashx+70),random.randint(flashy+30,flashy+70)),1)
    draw.circle(screen,flashyellow,(random.randint(flashx+30,flashx+70),random.randint(flashy+30,flashy+70)),1)
    draw.circle(screen,flashyellow,(random.randint(flashx+30,flashx+70),random.randint(flashy+30,flashy+70)),1)    
    
    
def drawScene(screen, button, shipx, shipy):
    global missileList, missileList2, shotTimer, score, flashcd,shipX,shipY,flashx,flashy,shipPic,random1,random2,random3,random4,endpage,game,hightestscore,speed1,speed2,time1
    missilespeed=speed1
    missilespeed2=speed2    
    BACKGROUND(screen, 0,0)
    if flashcd<=1:
      shipPic = image.load("heimer.png")
      shipPic = transform.scale(shipPic, (shipPic.get_width()//25, shipPic.get_height()//25))     
      flash1()
      flash1()
      flash1()
      flash1() 
      flash1()
      flash1() 
    if flashcd>1:
        shipPic = image.load("heimer3.png")
        shipPic = transform.scale(shipPic, (shipPic.get_width()//25, shipPic.get_height()//25))        
        
    score+=1
    if flashcd<=400:
      flashcd+=1
    draw.rect(screen,WHITE,(17,17,86,36),3)
    draw.rect(screen,YELLOW,(20,20,flashcd/5,30))
    displayt(30,485,50,WHITE,str(score))
    #draw shipPic
    
    shipRect = Rect(shipx, shipy, shipPic.get_width(), shipPic.get_height())
    screen.blit(shipPic, shipRect)
    flashRect = Rect(110, 17, flash.get_width(), flash.get_height())
    screen.blit(flash, flashRect)    
    rect1 = Rect(shipx + 20, shipy + 8, 35, 38) 
    rect2 = Rect(shipx + 28, shipy + 40, 25, 30)
    
    hitList = [rect1, rect2]
    
    
    # loop is for drawing
    for i in range (len(missileList)-1,-1, -1): # get each missile
        missiley = missileList[i]
        missiley2 = missileList[i]
        
        missileRect = Rect(random1, 700-missiley, 50, 5 )
        missileRect2 = Rect(random2, missiley2, 50, 5 )
        
        draw.rect(screen, GREEN, missileRect)  #draw the missile
        draw.rect(screen, RED, missileRect2)  #draw the missile
        
        
        missileList[i] -=missilespeed # move missile down 5
        
        if missileList[i] < 0: # if off screen
                         
            del missileList[i] # delete current missile
    display.flip()
    for i in range (len(missileList2)-1,-1, -1): # get each missile
        missiley3 = missileList2[i]
        missiley4 = missileList2[i]
        missileRect3 = Rect(missiley3,random3, 5, 50 )
       
        missileRect4 = Rect(1000-missiley4,random4, 5, 50 )
        draw.rect(screen, WHITE, missileRect3)  #draw the missile
        draw.rect(screen, BLUE, missileRect4)  #draw the missile
        missileList2[i] -=missilespeed2 # move missile down 5
        if missileList2[i] < 0: # if off screen
            del missileList2[i] # delete current missile
    display.flip()    
    
    # loop is for collision
    for i in range (len(missileList)-1, -1, -1): # get each missile vertical
        missiley = missileList[i]
        missiley2 = missileList[i]
        missileRect = Rect(random1, 700-missiley, 50, 5)  
        missileRect2 = Rect(random2, missiley2, 50, 5 )
        #print(missileRect.collidelist(hitList))
        if(missileRect.collidelist(hitList) != -1) or (missileRect2.collidelist(hitList) != -1)  or shipX<0 or shipX>940 or shipY<0 or shipY>630:
            
            shipX=400
            shipY=300            
            flashcd=400
            mylist.append(score)
            mylist.sort()
            mixer.Sound.play(dd)
            hightestscore=(mylist[-1])
            endpage=True
            game=False
            historys()
            del missileList[i] 
            del missileList2[i]
            break
            
    
    for i in range (len(missileList2)-1, -1, -1): # get each missile horizontal
        missiley3 = missileList2[i]
        missiley4 = missileList2[i]
        missileRect3 = Rect(missiley3,random3, 5, 50 )
        missileRect4 = Rect(1000-missiley4,random4, 5, 50 )
        #print(missileRect.collidelist(hitList))
        if(missileRect3.collidelist(hitList) != -1) or (missileRect4.collidelist(hitList) != -1) or shipX<0 or shipX>940 or shipY<0 or shipY>630:
           
            shipX=400
            shipY=300            
            flashcd=400
            mylist.append(score)
            mylist.sort()
            mixer.Sound.play(dd)
            hightestscore=(mylist[-1])
            endpage=True
            game=False
            historys()
            del missileList[i] 
            del missileList2[i]         
            break
            
        
    if time.get_ticks() - shotTimer >= time1: # 2 second difference
        random1=random.randint(0,950)
        random2=random.randint(0,950)   
        random3=random.randint(0,650)
        random4=random.randint(0,650)
        while abs(random1-random2)<50 or abs(random3-random4)<50:
            random1=random.randint(0,950)
            random2=random.randint(0,950)    
            random3=random.randint(0,650)
            random4=random.randint(0,650)
        missileList.append(700) # add new missile
        missileList2.append(1000)
        shotTimer = time.get_ticks() # reset timer
        
   
    
    return True

running = True
myClock = time.Clock()
shotTimer = time.get_ticks() # time of last shot
missileList = [700] # a list for missiles currently on the screen (y - values)
missileList2 = [1000]
shipX = 400
shipY = 300
moveRate = 4
# Game Loop
mixer.music.load("song3.mp3")
mixer.music.play(-1)
while running:
    if startpage==True:
        display.update()
        startpage1 = transform.scale(startpage1, (width, height))
        screen.blit(startpage1, Rect(0,0,width,height))    #draw the picture
        # right side
        draw.rect(screen,YELLOW,(600,200,250,100))
        displayt(60,660,220,BLACK,"Start")
        draw.rect(screen,YELLOW,(600,450,250,100))
        displayt(60,660,470,BLACK,"Quit")
        screen.blit(startpage1, Rect(0 + width, 0, width, height))    
        
        draw.rect(screen,BLACK,(600,200,250,100),mouse1)
        draw.rect(screen,BLACK,(600,450,250,100),mouse2)
        
        for evnt in event.get():  #finds events
            
            if evnt.type == MOUSEBUTTONDOWN:  #checks if the event was a mouse press
                mx, my = evnt.pos  #grabs the position of the mouse when pressed
                
                if mx >= 600 and mx <= 850 and my >= 200 and my <=300:
                    game=False
                    menupage=True
                    startpage=False
                    missileList.pop
                    missileList2.pop
                    mixer.music.stop()
                    mixer.music.load("songmenu.mp3")
                    mixer.music.play(-1)                     
                    shotTimer = time.get_ticks()
                    
                if mx >= 600 and mx <= 850 and my >= 450 and my <=550:
                    quit()
                    
            if evnt.type == MOUSEMOTION:
                
                mx, my = evnt.pos  #grabs the position of the mouse when pressed
                
                if mx >= 600 and mx <= 850 and my >= 200 and my <=300:
                    mouse1=3
                                       
                else:
                    mouse1=mouse2=1
                if mx >= 600 and mx <= 850 and my >= 450 and my <=550:
                    mouse2=3
                                 
                
    elif menupage==True:
                
        display.update()
        screen.blit(menub, Rect(0,0,width,height))
        draw.circle(screen,BLACK,(386,515),4)
        PRESS_RIGHT = False
        PRESS_LEFT = False
        PRESS_UP = False
        PRESS_DOWN = False
        PRESS_SPACE = False        
        if cccc==2:
            speed1=8
            speed2=11.4
            time1=3000        
            draw.circle(screen,WHITE,(386,444),4)
            files="in2.dat"
        if cccc==1:
            draw.circle(screen,WHITE,(386,480),4)
            speed1=10
            speed2=14.3
            time1=2500   
            files="in1.dat"
        if cccc==0:
            draw.circle(screen,WHITE,(386,515),4)
            speed1=12
            speed2=17
            time1=2000
            files="in0.dat"
    
        screen.blit(menub, Rect(0 + width, 0, width, height))
        for e in event.get():  
            if e.type == KEYDOWN:
                if e.key == K_UP: 
                    cccc+=1
                    mixer.Sound.play(sz)
                    if cccc>2:
                        cccc=2
                    
                if e.key == K_DOWN: 
                    cccc-=1
                    mixer.Sound.play(sz)
                    if cccc<0:
                        cccc=0                    
                   
                
                if e.key == K_RETURN:
                    mixer.music.load("songgame.mp3")
                    mixer.music.play(-1)                    
                    hotTimer = time.get_ticks()
                    game=True
                    menupage=False               
                    shotTimer = time.get_ticks()
                    if missilespeed!=speed1:
                        score=0
                        flashcd=400
        
                    
    elif game==True:
        display.update()
        for e in event.get():             # checks all events that happen
    
            if e.type == QUIT:
                running = False
    
            elif e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    PRESS_RIGHT = True
                if e.key == K_LEFT:
                    PRESS_LEFT = True 
                if e.key == K_UP:
                    PRESS_UP = True
                if e.key == K_DOWN:
                    PRESS_DOWN = True
                if e.key == K_SPACE:
                    PRESS_SPACE = True
                if e.key == K_ESCAPE:
                    mixer.music.load("songmenu.mp3")
                    mixer.music.play(-1)                    
                    
                    menupage=True
                    game=False
                    missilespeed=speed1
                if e.key == K_q:
                    running = False
            elif e.type == KEYUP:
                if e.key == K_RIGHT:
                    PRESS_RIGHT = False
                if e.key == K_LEFT:
                    PRESS_LEFT = False 
                if e.key == K_UP:
                    PRESS_UP = False
                if e.key == K_DOWN:
                    PRESS_DOWN = False   
                if e.key == K_SPACE:
                    PRESS_SPACE = False
        if running:
            running = drawScene(screen, button, shipX, shipY)
    
        myClock.tick(60)                     # waits long enough to have 60 fps
    
        countkey=0
    
        # for ship movement
        if PRESS_RIGHT == True and PRESS_UP == True:
            shipX -= moveRate 
            shipY += moveRate 
            shipX += 0.71*moveRate
            shipY -= 0.71*moveRate
            if PRESS_SPACE == True:
                if flashcd>=400:
                    flashcheck()
                    falshsound()
                    shipX+= 50*0.71
                    shipY-= 50*0.71
                    flashcd=0     
        if PRESS_RIGHT == True and PRESS_DOWN == True:
            shipX -= moveRate 
            shipY -= moveRate 
            shipX += 0.71*moveRate
            shipY += 0.71*moveRate
            if PRESS_SPACE == True:
                if flashcd>=400:
                    flashcheck()
                    falshsound()
                    shipX+= 50*0.71
                    shipY+= 50*0.71
                    flashcd=0 
        if PRESS_LEFT == True and PRESS_UP == True:
            shipX += moveRate 
            shipY += moveRate 
            shipX -= 0.71*moveRate
            shipY -= 0.71*moveRate
            if PRESS_SPACE == True:
                if flashcd>=400:
                    flashcheck()
                    falshsound()
                    shipX-= 50*0.71
                    shipY-= 50*0.71
                    flashcd=0     
        if PRESS_LEFT == True and PRESS_DOWN == True:
            shipX += moveRate 
            shipY -= moveRate 
            shipX -= 0.71*moveRate
            shipY += 0.71*moveRate
            if PRESS_SPACE == True:
                if flashcd>=400:
                    flashcheck()
                    falshsound()
                    shipX-= 50*0.71
                    shipY+= 50*0.71
                    flashcd=0     
        if PRESS_RIGHT == True:
            shipX += moveRate      
            if PRESS_SPACE == True:
                if flashcd>=400:
                    flashcheck()
                    falshsound()
                    shipX+= 50
                    flashcd=0
        if PRESS_LEFT == True:
            shipX -= moveRate  
            if PRESS_SPACE == True:
                if flashcd>=400:
                    falshsound()
                    flashcheck()
                    shipX-= 50
                    flashcd=0
    
        if PRESS_UP == True:
            shipY -= moveRate
            if PRESS_SPACE == True:
                if flashcd>=400:
                    falshsound()
                    flashcheck()
                    shipY-= 50
                    flashcd=0
    
        if PRESS_DOWN == True:
            shipY += moveRate    
            if PRESS_SPACE == True:
                if flashcd>=400:
                    falshsound()
                    flashcheck()
                    shipY+= 50
                    flashcd=0
    elif endpage==True:  
        display.update()
              
        endpage1 = transform.scale(endpage1, (width, height))
        screen.blit(endpage1, Rect(0,0,width,height))    #draw the picture
        # right side
        screen.blit(endpage1, Rect(0 + width, 0, width, height)) 
        
        displayt(50,130,520,WHITE,"Highest Score Ever:")
        displayt(70,270,570,WHITE,str(reccords[-1]))
        displayt(30,210,430,BLACK,"Your Best Score:")
        displayt(25,430,435,BLACK,str(hightestscore))
        displayt(70,50,100,BLACK,str(score))
        
        flashcd=400
        
        for e in event.get():             # checks all events that happen
    
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    mixer.music.load("songmenu.mp3")
                    mixer.music.play(-1)                    
                    menupage=True
                    endpage=False
                    missilespeed=speed1  
                    score=0
                    PRESS_RIGHT = False
                    PRESS_LEFT = False
                    PRESS_UP = False
                    PRESS_DOWN = False
                    PRESS_SPACE = False                    
                
                if e.key == K_RETURN:
                    
                    endpage=False
                    game=True
                    score=0
                    PRESS_RIGHT = False
                    PRESS_LEFT = False
                    PRESS_UP = False
                    PRESS_DOWN = False
                    PRESS_SPACE = False

                if e.key == K_q:
                    running = False
                    pygame.quit()
                    exit()
                                        
quit()
