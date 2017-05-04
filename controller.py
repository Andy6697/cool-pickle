import pygame
import math
import random
from model import *
pygame.init()

#All colors listed to be used for drawing
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,200,0)
RED = (200,0,0)
BLUE = (0,0,255)
BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0,255,0)

#Sets up the screen
SPEED_FACTOR = 1.1
display_width = 1280
display_height = 809
size = (display_width, display_height)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)

clock = pygame.time.Clock()
font = pygame.font.SysFont('MV Boli', 50, True, False)
fontgameover = pygame.font.SysFont('Calibri', 50, True, False)
gameovertext = fontgameover.render("GAME OVER! PRESS LEFT TO RESTART OR DOWN TO QUIT",True,BLACK)
pygame.display.set_caption("Dino Dash")

intro = True
background_image = pygame.image.load("Mountain_desert.png")
screen.blit(background_image, [0,0])
text1 = font.render("Dino Dash", True, WHITE)
screen.blit(text1, [401, 40])

pygame.mixer.music.load('gameoverzelda.midi')
pygame.mixer.music.play(-1)
jumpsound = pygame.mixer.Sound("jump05.wav")

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    """displays whatever message is written to the screen"""
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)   #it pauses the game for 2 seconds

    rungame()

def button(msg,x,y,w,h,ic,ac,action=None):
    """creates the button's functionality, and keeps track of the mouse position and click, to react like its an actual button"""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))       
    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))

    if click[0] == 1 and (x+w > mouse[0] > x and y+h > mouse[1] > y) and action != None:
        action()


    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg,smallText)
    textRect.center = ( x+(w/2)), (y+(h/2))
    screen.blit(textSurf, textRect)

def quitgame():
    """quits game"""
    pygame.quit()
    quit()

def end_intro():
    """exits the menu display"""
    global intro
    intro = False

def game_intro():
    """this game intro is the menu itself,creating the button graphics, and show the change in darker ver. of color if hover it
    also enters into the game itself, and exit menu screen as well as a quit button to exit pygame completely"""
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Dino Dash", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)


        button("GO!",450,550,100,50,GREEN,BRIGHT_GREEN,end_intro)
        button("QUIT",700,550,100,50,RED,BRIGHT_RED,quitgame)


        pygame.display.update()
        clock.tick(15)

#Sets up a group to control all cacti. Cac_list has all of the cacti in it.
cac_list = pygame.sprite.Group()
def makecactusgroup():
    """Creates 5 cacti with the Cactus class and adds them to the Cac_list"""
    for i in range(5):
        xval = 1280 + random.randrange(700)
        cac = Cactus(100, 160, xval, 460)
        cac_list.add(cac)
#Creates a dinosaur with the Dino class and sets its initial positions
dino = Dino(90, 84, 0, 460)


def rungame():
    """This will be looped within the main function to have the game run."""
#Prepares scores, cac_list, time, speed, etc every time game restarts
    highscoreread = open("highscore.txt","r")
    highscore = int(highscoreread.read())
    highscoreread.close()
    initialtime = pygame.time.get_ticks()
    pygame.sprite.Group.empty(cac_list)
    makecactusgroup()
    speed = 12
    level = 1
    score = 0
    done = False
    cacxval = []
    for cac in cac_list:
        cacxval.append(cac.rect.x)
    cacxval.sort()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #Allows the loop to end and returns True to main() if the player clicks the X
                done = True
                return True
            elif event.type == pygame.KEYDOWN:  #Allows the player to jump if they press up and if they are on the ground
                if event.key == pygame.K_UP and dino.rect.y == 460:
                    dino.reach = False
                    jumpsound.play()
        dino.jump()
        dino.fall()
        screen.fill(WHITE)
        screen.blit(background_image, [0,0])
        screen.blit(text1, [401, 40])

        for cac in cac_list:
            cacxval.remove(cac.rect.x)
            if cac.rect.x < -20:
                cac.rect.x = cacxval[-1] + (25 * speed) + random.randrange(100)
            for xval in cacxval:
                    while abs(cac.rect.x - xval) <= (25 * speed) and cac.rect.x > 1280 :
                            cac.rect.x += 100 + (25 * speed)  
            cac.rect.x -= speed
            cac.image.set_colorkey(WHITE)
            screen.blit(cac.image, [cac.rect.x, cac.rect.y])
            cacxval.append(cac.rect.x)
            cacxval.sort()
        dino.image.set_colorkey(WHITE)  #displays the dino image based on its current position
        screen.blit(dino.image, [dino.rect.x, dino.rect.y])
        cac_hit_list = pygame.sprite.spritecollide(dino,cac_list,True)

        if len(cac_hit_list) > 0:   #Checks if there is a collision and if the high score was beat and updates accordingly. Then exits the while loop.
            if score > highscore:
                highscorewrite = open("highscore.txt","w")
                highscorewrite.write(str(score))
                highscorewrite.close()
            done = True
            continue
        score = (pygame.time.get_ticks()-initialtime)//100    #Makes a score based on time
        if level < (score / 50): #Increases speed of cacti every time the score goes up 25
            speed += 1
            level += 1
        text = font.render("Score: " + str(score),True,BLACK)
        highscoretext = font.render("High Score: " + str(highscore),True, BLACK)
        screen.blit(text, [840, 40])
        screen.blit(highscoretext, [800,80])
        pygame.display.flip()
        clock.tick(30)

def main():
    game_intro()
    closegame = False
    while closegame == False: #Loops through the rungame function until closegame == True
        choicemade = False
        if rungame() == True: #Doesn't go into the choicemade while loop if rungame() returns True (if someone clicks the X in rungame).  
            choicemade = True
            closegame = True
        while choicemade == False: #Displays a game over screen until a choice is made (left, right, or the red X is pressed).
            screen.blit(gameovertext,[50,200])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Red X clicked, leave the choicemade (AKA game over screen) loop. Also leave the closegame loop to end game.
                    closegame = True
                    choicemade = True
                if event.type == pygame.KEYDOWN: #Same as clicking Red X.
                    if event.key == pygame.K_DOWN:
                        closegame = True
                        choicemade = True
                    elif event.key == pygame.K_LEFT: #Restarts the game. Leaves choicemade loop. Does not leave closegame loop so rungame() called again.
                        choicemade = True
    pygame.quit()
main()
