#WE first import pygame library
import pygame
import random
#initialiaze pygame
pygame.init()

imageUp = pygame.image.load('flappyUp.png')
imageUp = pygame.transform.scale(imageUp, (80,40))

imageDown = pygame.image.load('flappyDown.png')
imageDown = pygame.transform.scale(imageDown, (80,40))

imageDead = pygame.image.load('ghost.jpg')
imageDead = pygame.transform.scale(imageDead, (28,3))

my_image = pygame.image.load('background.png')

sun = pygame.image.load('sun.png')
sun = pygame.transform.scale(imageUp, (40,40))


#define colors
black = (200, 50, 50)
background= (30, 30, 30)
green = (0, 255, 0)
red = (255, 0, 0)

skyBlue = (0, 191, 255)
orange =(255, 215, 0)
gray = (112, 138, 144)

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
xloc =700
xsize = 70
ysize = random.randint(0, 350)
space = 150
obspeed = 2
score = 0

screen.blit(my_image, (500,500)) 
def obstacles(xloc, yloc, xsize, ysize):
    imgTop = pygame.image.load('flame.jpg')
    imgTop = pygame.transform.rotate(imgTop, 180)
    imgTop = pygame.transform.scale(imgTop, (xsize, ysize))
    imgBottom = pygame.image.load('flame.jpg')
    imgBottom = pygame.transform.scale(imgBottom, (xsize, 500 - ysize))
    screen.blit(imgTop, (xloc, yloc))
    screen.blit(imgBottom, (xloc, int(yloc + ysize + space)
                            ))
    #pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
    #pygame.draw.rect(screen,green, [xloc,int(yloc+ysize+space), xsize, ysize+500])

def ball(x,y, image):
    #pygame.draw.circle(screen,black,(x,y),20)
    screen.blit(image, (x, y))

def gameover():
    font = pygame.font.SysFont(None, 75)
    text = font.render("Game Over ", True, red)
    screen.blit(text, [150, 250])
    

def Score(score):
    font = pygame.font.SysFont(None, 75)
    text = font.render("Score "+str(score), True, black)
    screen.blit(text, [0,0])





#-------------End Function -----------------------------------------------------------------|

#Global image object
image = imageUp
pygame.mixer.music.load('intro.mp3')
pygame.mixer.music.play(-1)
ghost = imageDead

#While logic to keep game running
while not done:
    
    #Capture input events so we can act upon them
    for event in pygame.event.get():
        #if User select 'ESC' key or presses windows 'X' top right button
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
               image = imageUp
               y_speed = -5
            if event.key == pygame.K_DOWN:
               
               y_speed = 5
            #if event.key == pygame.K_LEFT:
             #   x_speed = -5
            #if event.key == pygame.K_RIGHT:
             #   x_speed = 5
        if event.type == pygame.KEYUP:
            if event.type == pygame.KEYUP:
                image = imageDown
                y_speed = 1
  
    
    screen.blit(my_image, [0,0])
    obstacles(xloc, yloc, xsize, ysize)
    #call function to draw the ball
    ball(x,y, image)
    Score(score)
    #adjust vertical y position
    y+= y_speed
    #x+= x_speed
    
    xloc -= obspeed

    if y > ground or y < roof:
        gameover()
        y_speed = 30
        obspeed = 0
        if y >= ground:
            y_speed = 0
    #If we hit obstacle in the top block
    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 30
        if y >= ground:
            y_speed = 0
     #If we hit obstacle in the top block
    if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 30
        if y >= ground:
            y_speed = 0
    #If obstacle location X is
    if xloc < -80:
        xloc = 700
        ysize = random.randint(0,350)
        if y >= ground:
            y_speed = 0
    if x > xloc and x < xloc+3:
        score = (score + 1)
        #pygame.mixer.music.load('points.mp3')
        #pygame.mixer.music.play(0)
    
    #define times per second this will happen via clock defined above
    pygame.display.flip()
    clock.tick(60)

#once logic loop end exit game
pygame.quit()
