import pygame
import os
pygame.init()
win= pygame.display.set_mode((800,600))
pygame.display.set_caption("Jogging Hustle")
#####images
right=[None]*9
for i in range(1,10):
    right[i-1]=pygame.transform.scale((pygame.image.load(os.path.join("img","right"+str(i)+".png"))),(70,80))


d1_img=pygame.image.load(os.path.join("img","d1.png"))
d1=pygame.transform.scale(d1_img,(50,50))

d2_img=pygame.image.load(os.path.join("img","d2.png"))
d2=pygame.transform.scale(d2_img,(50,50))

c1_img=pygame.image.load(os.path.join("img","car1.png"))
c1=pygame.transform.scale(c1_img,(500,100))
bg_img=pygame.image.load(os.path.join("img","back.jpg"))
bg=pygame.transform.scale(bg_img,(800,600))
#variables
run=False
##bg cord
a=0
##obs cord
q=500
e=500##for dustbin
w=500
##delay var to increase speed of bg with time
clock=pygame.time.Clock()
t=20


###char
####key=pygame.key.get_pressed() should be specified inside loop. As the function is inside loop so it is done at the loop.
step=0
x=10
y=470
jumpheight=5


def draw():
    global q
    global step
    global y
    global jumpheight
    jump = False
    win.blit(d1, (q,e))
    win.blit(d2, (800+q,w))
    if q<-860:
        q=800#### so that the img appear outside the canvas and it will seem as coming.
    q -= 1
    ###for motion of character:
    win.blit(right[step//10],(x,y))
    step+=1
    if step>=90:
        step=0
    k = pygame.key.get_pressed()
    if jump==False and k[pygame.K_SPACE]:
        jump=True
    if jump==True:
        y-=jumpheight*4
        jumpheight-=1
    if jumpheight<-5:
        jump=False
        jumpheight=5


def bg_loop():
    global a
    win.blit(bg, (a, 0))
    win.blit(bg,((800+a),0))#####8000 width of disp
    if a==-800:
        win.blit(bg,((800+a),0))
        a=0
    a-=1






while run==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=True
    bg_loop()
    draw()
    #clock.tick(t)
    pygame.time.delay(4)
   # t+=2


    #print(t)
    print(y)
    pygame.display.update()