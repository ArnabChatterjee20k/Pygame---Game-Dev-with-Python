import pygame
import os
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Char anime")
stand=pygame.image.load(os.path.join("Hero","Stand.png"))

left=[None]*9
right=[None]*9



for picindex in range(1,10):
    

    left[picindex-1]=pygame.image.load(os.path.join("Hero","left"+str(picindex)+".png"))

for picindex2 in range(1, 10):
    right[picindex2 - 1] = pygame.image.load(os.path.join("Hero", "right" + str(picindex2) + ".png"))
    picindex2+=1



up=[None]*6
for picindex in range(1,7):
    up[picindex-1]=pygame.image.load(os.path.join("Hero","u"+str(picindex)+".png"))

down=[None]*8
for picindex in range(1,9):
    down[picindex-1]=pygame.image.load(os.path.join("Hero","d"+str(picindex)+".png"))


game=False
jump=False
left_turn=False
right_turn=False
up_turn=False
down_turn=False

step=0

speed=10
x=250
y=250
jumpht=10

def draw():
    global step
    win.fill((255,255,255))

    if step>=36 and (left_turn==True or right_turn==True):
        step=0

    #elif step>=36 and right_turn==True:
     #   step=0

    elif step>=48 and (up_turn==True or down_turn==True):
        step=0

    #elif step >= 48 and down_turn == True:
     #   step = 0

    if left_turn==True:
        win.blit(left[step//4],(x,y))
        step+=1


    elif right_turn == True:
        win.blit(right[step//4], (x, y))
        step += 1

    elif up_turn==True:
        win.blit(up[step//8],(x,y))
        step+=1
    elif down_turn==True:
        win.blit(down[step//6],(x,y))
        step+=1



    else:
        win.blit(stand, (x, y))
    


while game==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=True
    draw()


    input=pygame.key.get_pressed()


    if input[pygame.K_UP] and y>0 and jump is False:
            y-=speed
            up_turn = True
            down_turn = False
            left_turn = False
            right_turn = False

    elif input[pygame.K_DOWN] and y<500-50 and jump is False :###height and width
            y+=speed
            up_turn = False
            down_turn = True
            left_turn = False
            right_turn = False

    elif input[pygame.K_RIGHT] and x<500-50:####50 is the width of the obj and x axis is 500 is the display in right and 0 at left
        x+=speed
        left_turn = False
        right_turn = True
        print(right_turn, jump)

    elif input[pygame.K_LEFT] and x>0:
        x-=speed
        left_turn=True
        right_turn=False
        print(left_turn,jump)


    else:
        left_turn = False
        right_turn = False
        up_turn = False
        down_turn = False
        step = 0


    if input[pygame.K_SPACE] and jump==False:
        jump=True
        left_turn = False
        right_turn = False
        up_turn = False
        down_turn = False
        step = 0


    if jump==True:

        y-=jumpht*4
        jumpht-=1
        if jumpht<-10:
            jump=False
            jumpht=10




    pygame.time.delay(30)
    pygame.display.update()