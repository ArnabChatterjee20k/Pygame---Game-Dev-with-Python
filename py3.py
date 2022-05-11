import  pygame
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("3")
#colors
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
clock=pygame.time.Clock()
x=300
y=498
speed=1
jump=False
jump_speed=80
run=False

while run==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=True
    win.fill(black)
    pygame.draw.rect(win,white,[x,y,20,20])

    key=pygame.key.get_pressed()
    if key[pygame.K_SPACE] and jump==False:
        jump=True
    if jump==True:
        y-=jump_speed
        jump_speed-=30

        print(jump_speed,y)

    if jump_speed<=-80:


        jump=False
        jump_speed=80

    clock.tick(20)
    pygame.display.update()
pygame.quit()
quit()



