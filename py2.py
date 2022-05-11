import pygame
pygame.init()
gd=pygame.display.set_mode((1000,1000))
clock=pygame.time.Clock()
pygame.display.set_caption("2nd")

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
color=(255,0,255)

def msg():
    font=pygame.font.SysFont("Arial",32)
    render=font.render("start",True,blue)
    gd.blit(render,(500,500))
    pygame.display.update()

msg()
clock.tick(1)
def gameloop():
    x=300
    y=300
    a=400

    x_change=0
    y_change=0
    a_change = 0
    game=False
    while game==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change+=10
                    a_change -= 10
                elif event.key==pygame.K_RIGHT:
                    x_change-=10
                    a_change += 10
                elif event.key==pygame.K_UP:
                    y_change+=10
                    a_change -= 10
                elif event.key==pygame.K_DOWN:
                    y_change-=10
                    a_change += 10
                elif event.key==pygame.K_s or event.key==pygame.K_a or event.key==pygame.K_a or event.key==pygame.K_d or event.key==pygame.K_f:
                    event.type==pygame.quit()
                    quit()

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_DOWN or event.key==pygame.K_UP:
                    x_change=0
                    y_change=0
                    a_change=0
        gd.fill(black)


        pygame.draw.circle(gd,color,[x,y],20,10)

        pygame.draw.circle(gd, color, [a, a], 20, 10)
        x1=x

        x=x-x_change
        y=y-y_change
        a=a-a_change
        clock.tick(50)
        pygame.draw.rect(gd, white, [0, 0, 100, 100])
        for i in range(0,x1):
            pygame.draw.rect(gd,white,[i,i,100,100])


        pygame.display.update()


gameloop()

pygame.quit()
quit()

