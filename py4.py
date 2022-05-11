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
jump_speed=10
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
        if jump_speed>0:
            neg=1
            y -= (jump_speed ** 2) / 2 * neg
        if jump_speed < 0:
            neg =-1
            y -= (jump_speed ** 2) / 2 * neg
        print(jump_speed)

        if y<=498:
            jump_speed=False
            jump_speed=10

    clock.tick(20)
    pygame.display.update()
pygame.quit()
quit()



