import pygame
pygame.init()
gd=pygame.display.set_mode((500,500))

pygame.display.set_caption("First")
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
x=300
y=300

gameover=False
while gameover==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameover=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x-=50
            elif event.key==pygame.K_RIGHT:
                x+=50
            elif event.key==pygame.K_UP:
                y-=50
            elif event.key==pygame.K_DOWN:
                y+=50
            elif event.key == pygame.K_s:
                pygame.quit()

                quit()

    gd.fill(white)
    pygame.draw.rect(gd,red,[x,y,100,100])

    pygame.display.update()


pygame.quit()
quit()
