import pygame
pygame.init()
win=pygame.display.set_mode((800,600))
pygame.display.set_caption("5, loop bg")
white=(255,255,255)
width=800
bg_img=pygame.image.load("3-city-street-background-cartoon-clipart.jpg")
bg=pygame.transform.scale(bg_img,(800,600))
i=0
run=True
while run==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
    win.fill(white)
    win.blit(bg,(i,0))####by default i is 0 so coordinate img is (0,0),Then decreasiog i will allow img to push backward
    win.blit(bg,(width+i,0))##pasting img after the 1st img

    if i==-width:##if i reached the width value of prev img
        win.blit(bg, (width + i, 0))
        i = 0  ###setting i=0 so that each time  the  images are pasted when the 1st img is  at -800 otherwise it will not loop

    i -= 1####decreasing i at every single iteration
    #print(i) if not understandable run this cmd of prnt so that it can be undeerstandale
    pygame.display.update()
