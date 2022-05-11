import pygame
import os

pygame.init()
win = pygame.display.set_mode((500, 500))

# Load Images of the Character (there are two popular ways)
stationary = pygame.image.load(os.path.join("Hero", "Stand.png"))
# One way to do it - using the sprites that face left.
left =  [pygame.image.load(os.path.join("Hero", "left1.png")),
         pygame.image.load(os.path.join("Hero", "left2.png")),
         pygame.image.load(os.path.join("Hero", "left3.png")),
         pygame.image.load(os.path.join("Hero", "left4.png")),
         pygame.image.load(os.path.join("Hero", "left5.png")),
         pygame.image.load(os.path.join("Hero", "left6.png")),
         pygame.image.load(os.path.join("Hero", "left7.png")),
         pygame.image.load(os.path.join("Hero", "left8.png")),
         pygame.image.load(os.path.join("Hero", "left9.png"))]

# Another (faster) way to do it - using the sprites that face right.
right = [None]*10
for picIndex in range(1,10):
    right[picIndex-1] = pygame.image.load(os.path.join("Hero", "right" + str(picIndex) + ".png"))
    picIndex+=1


x = 250
y = 250
vel = 10
move_left = False
move_right = False
stepIndex = 0

# Draw the Game
def draw_game():
    global stepIndex
    win.fill((0, 0, 0))
    if stepIndex >= 36:
        stepIndex = 0
    if move_left==True:
        win.blit(left[stepIndex//4], (x, y))
        stepIndex += 1
    elif move_right==True:
        win.blit(right[stepIndex//4], (x,y))
        stepIndex += 1
    else:
        win.blit(stationary, (x,y))


# Main Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_game()

    # Movement
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT]:
        x -= vel
        move_left = True
        move_right = False
    elif userInput[pygame.K_RIGHT]:
        x += vel
        move_left = False
        move_right = True
    else:
        move_left = False
        move_right = False
        stepIndex = 0

    pygame.time.delay(30)
    pygame.display.update()