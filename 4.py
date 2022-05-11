import pygame
pygame.init()
win=pygame.display.set_mode((800,600))
pygame.display.set_caption("4")
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
clock=pygame.time.Clock()
x=400
y=500
ht=30
wd=30
speed=10#v_x

jump=False
v_y=10

game=False
while game==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=True


    key=pygame.key.get_pressed()

    if key[pygame.K_LEFT]and x>speed:#####or x>0 same execution will be their
        x-=speed

    if key[pygame.K_RIGHT] and x<800-wd :
        x += speed
    if jump is False:#############To disable up and down while jump
        if key[pygame.K_UP]and y>speed:#####or y>0  since the top coordinate in the edge of display is origin ie (0,0)
            y -= speed

        if key[pygame.K_DOWN] and y<600-ht :
            y += speed

    if key[pygame.K_SPACE ]and jump==False :
        jump=True

    if jump==True:
        y-=v_y*4   #moving upward amd multiply by 4 for high jump
        v_y-=1  #moving ball dnwrd by 1unit untill jump is false
        if v_y<-10:# at the starting  point when the ball comes to its original posn and jump becomes false
            jump=False
            v_y=10 #setting to previous value

    win.fill(black)
    pygame.draw.rect(win, white, [x, y, ht, wd])
    pygame.time.delay(30)




    pygame.display.update()