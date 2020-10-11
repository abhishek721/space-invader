import pygame
import random
import math
from pygame import mixer
pygame.init()

#background music
mixer.music.load('background.wav')
mixer.music.play(-1)# music play infintely in background

#laser sound on bullet hitting

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("space Invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#player cordinates
playerImg = pygame.image.load('hitter.png')
px=400
py=480
px_change=0
def player(x,y):
    screen.blit(playerImg, (px,py))

#multiple enemy 
enemyImg=[]
ex=[]
ey=[]
ex_change=[]
ey_change=[]
no_of_enemy=4

#enemy cordinates
for i in range(no_of_enemy):
    enemyImg.append(pygame.image.load('enemy.png'))
    ex.append(random.randint(0,736))
    ey.append(random.randint(0,420))
    ex_change.append(3)
    ey_change.append(20)
    
def enemy(ex,ey,i):
        screen.blit(enemyImg[i], (ex,ey))
#background
background = pygame.image.load('background.png')

#bullet
b_state= "ready"
bullet = pygame.image.load('bullet.png')
bx=0
by=480
by_change=5
def b_fire(px,py):
    global b_state
    b_state = "fire"
    screen.blit(bullet,(px+13,py+10))

#collision
def iscollision(p,q,r,s):
    distance = math.sqrt((math.pow((p-r),2)) + (math.pow((q-s),2)))
    if distance<27:
        return True
    else:
        return False
#score
tx=10
ty=10
score_val=0
#font of score
font = pygame.font.Font('freesansbold.ttf',32)
def show_score(x,y):
    score = font.render("score : " + str(score_val), True, (255,255,255))
    screen.blit(score,(x,y))

#game over text
gx=200
gy=300
font_over= pygame.font.Font('freesansbold.ttf',60)
def show_over(x,y):
    over= font_over.render('GAME OVER', True, (255,255,255))
    screen.blit(over,(x,y))

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                px_change= 2
            if event.key == pygame.K_LEFT:
                px_change = -2
            if event.key == pygame.K_SPACE:
                if b_state is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play() 
                    bx=px
                    b_fire(bx,by)
                

                
                
                
    #player
    px += px_change
    if px<=0:
        px=0
    elif px>=736:
        px=736
    #enemy
    for i in range(no_of_enemy):

        if ey[i] > 420:
            for j in range(no_of_enemy):
                ey[j]=2000
            show_over(gx,gy)
            break
        ex[i] += ex_change[i]
        if ex[i]<=0:
            ex_change[i]=5
            ey[i] += ey_change[i]
        elif ex[i]>=736:
            ex_change[i]=-5
            ey[i] += ey_change[i]
        enemy(ex[i],ey[i],i)
        #collision
        collision = iscollision(ex[i],ey[i],bx,by)
        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            by=480
            by_state= "ready"
            score_val += 1
            
            ex[i]= random.randint(0,800)
            ey[i]= random.randint(0,420)
    #bullet
    if b_state is "fire":
        
        b_fire(bx,by)
        by -= by_change
    if by<=0:
        by=480
        b_state="ready"
   
    
        
    player(px,py)
    show_score(tx,ty)
    
    pygame.display.update()