import pygame
import random
import os
if not os.path.exists("highscore.txt"):
    with open("highscore.txt","w") as f:
        f.write("0")
pygame.init()
pygame.mixer.init()
width=900
height=500
disp=pygame.display.set_mode((width,height))

##color
g=random.randint(0,100)
b=random.randint(0,200)
r=random.randint(0,255)

####disp
bg=pygame.image.load(os.path.join("snake xenia req","s.jpg"))
bg=pygame.transform.scale(bg,(width,height)).convert_alpha()

clock=pygame.time.Clock()

initial_size=30

def text(msg,size,x,y):
    """Displays the txt in the  screen"""
    font = pygame.font.SysFont(None, size)
    color = (r, g, b)
    mes=font.render(msg,True,color)
    disp.blit(mes,(x,y))

def plot_snake(snk,x,y):
    """snake plotting"""
    for x,y in snk:
        pygame.draw.rect(disp,(r,g,b),[x,y,initial_size,initial_size])

def welcome():
   pygame.mixer.music.load(os.path.join("snake xenia req", "shape.mp3"))
   pygame.mixer.music.play()


   run=False
   while run==False:
       disp.blit(bg,(0,0))
       text("Press enter!",40,250,240)
       text("p=pause music | r=resume music", 40, 240, 280)
       for event in pygame.event.get():
           if event.type==pygame.QUIT:
               pygame.quit()### otherwise gameover scr left open
               quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_p:
                   pygame.mixer.music.pause()

               elif event.key == pygame.K_r:
                   pygame.mixer.music.unpause()
               elif event.key==pygame.K_RETURN:
                   pygame.mixer.music.stop()
                   gameloop()
       pygame.display.update()
       clock.tick(60)

def gameloop():



    ###snake variables:

    snk=[]### for increasing  the length of snake

    snake_lenghth=1 ## for increasing the length of snake

    x_posn=50
    y_posn =50
    v_x=0
    v_y=0

    score=0

    #food
    food_x = random.randint(20, width - 30)
    food_y = random.randint(20, height - 30)

    ##main loop:
    a=pygame.mixer.Sound(os.path.join("snake xenia req","bg.mp3"))#### this can be store inside variable but music cant be  stored
    a.play()
    with open("highscore.txt", "r") as f: ### must be used here otherwise if used in loop it will read  highscore  always 0
        highscore=f.read()
    run=False
    over=False

    while run==False:
        if over==True:
            a.stop()
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            disp.fill((0,0,0))
            text("Game over!",55,250,150)
            text("Score= "+str(score),60,265,210)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            pygame.display.update()




        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        v_x=10
                        v_y=0
                    if event.key==pygame.K_LEFT:
                        v_x=-10
                        v_y=0
                    if event.key==pygame.K_UP:
                        v_y=-10
                        v_x=0
                    if event.key==pygame.K_DOWN:
                        v_y=10
                        v_x=0

            x_posn+=v_x
            y_posn+=v_y


            ### game play:
            disp.fill((220,220,220))

            pygame.draw.rect(disp,(0,120,230),[food_x,food_y,initial_size,initial_size])

            plot_snake(snk, x_posn, y_posn)###  after food otherwise it will look bad



            text(f"Score= {score}  Highscore={highscore}" ,20,5,5)


            head = []### must be at this at this posn
            head.append(x_posn)
            head.append(y_posn)
            snk.append(head)



            if len(snk)>snake_lenghth:
                del snk[0]

                ####detection of collision
                ###score
                if abs(x_posn - food_x) < 10 and abs(y_posn - food_y) < 10:


                    pygame.mixer.music.load(os.path.join("snake xenia req", "eat.mp3"))
                    pygame.mixer.music.play()

                    food_x = random.randint(20, width - 30)
                    food_y = random.randint(20, height - 30)
                    snake_lenghth += 5
                    score+=10
                    if score>int(highscore):
                        highscore=score

                ###for game over
                if x_posn < 0 or x_posn > width or y_posn < 0 or y_posn > height-10 or head in snk[ :-1]:  ### except the current elemnent

                    pygame.mixer.music.load(os.path.join("snake xenia req","Bang.mp3"))
                    pygame.mixer.music.play()
                    over = True

            pygame.display.update()
            clock.tick(60)###fps=60

    pygame.quit()
    quit()
welcome()
