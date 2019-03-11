

#WE first import pygame library
import pygame
import random
#initialiaze pygame
pygame.init()

#define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
#define screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

#define screen tittle
pygame.display.set_caption("Flappy Bird")

#boolean T/F to control game logic
done = False

#clock to control game refresh speed
clock = pygame.time.Clock()

x = 350
y = 250

#define global variable to control speed
x_speed = 0
y_speed = 0
ground = 477
roof = 0
yloc = 0
xloc = 450
xsize = 70
ysize = random.randint(0, 350)
space = 150
obspeed = 2.5

def obstacles(xloc, yloc, xsize, ysize):
    pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(screen,green, [xloc,int(yloc+ysize+space), xsize, ysize+500])

def ball(x,y):
    pygame.draw.circle(screen,black,(x,y),20)

def gameover():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Game Over ", True, red)
    screen.blit(text, [150, 250])

#While logic to keep game running
while not done:
    #Capture input events so we can act upon them
    for event in pygame.event.get():
        #if User select 'ESC' key or presses windows 'X' top right button
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -5
            if event.key == pygame.K_DOWN:
                y_speed = 5
            if event.key == pygame.K_LEFT:
                x_speed = -5
            if event.key == pygame.K_RIGHT:
                x_speed = 5
        if event.type == pygame.KEYUP:
            if event.type == pygame.KEYUP:
                y_speed = 1
          
    screen.fill(white)
    obstacles(xloc, yloc, xsize, ysize)
    #call function to draw the ball
    ball(x,y)
    #adjust vertical y position
    y+= y_speed
    x+= x_speed

    xloc -= obspeed

    if y > ground or y < roof:
        gameover()
        y_speed = 0
        obspeed = 0
    #define times per second this will happen via clock defined above
    pygame.display.flip()
    clock.tick(60)

#once logic loop end exit game
pygame.quit()