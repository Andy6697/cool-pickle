import pygame
import math
import random
pygame.init()

#All colors listed to be used for drawing
BLACK = (0,0,0)
white = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)
#Sets up the screen
SPEED_FACTOR = 1.1
display_width = 1280
display_height = 809
size = (display_width, display_height)
screen = pygame.display.set_mode(size)
screen.fill(white)
#Sets up the clock for the tick rate and for the score
clock = pygame.time.Clock()
#Sets up an initial score and it's font to prepare for its display on screen
score = 0
font = pygame.font.SysFont('MV Boli', 50, True, False)
fontgameover = pygame.font.SysFont('Calibri', 50, True, False)
gameovertext = fontgameover.render("GAME OVER! PRESS LEFT TO RESTART OR DOWN TO QUIT",True,BLACK)
pygame.display.set_caption("Dino Dash")

background_image = pygame.image.load("Mountain_desert.png")
screen.blit(background_image, [0,0])
text1 = font.render("Dino Dash", True, white)
screen.blit(text1, [401, 40])
#pygame.display.flip()

pygame.mixer.music.load('gameoverzelda.midi')
pygame.mixer.music.play(-1)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    #it pauses the game for 2 seconds

    rungame()

def button(msg,x,y,w,h,ic,ac,action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
    if click[0] == 1 and action != None:
        action()

    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg,smallText)
    textRect.center = ( x+(w/2)), (y+(h/2))
    screen.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Dino Dash", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)


        button("GO!",150,550,100,50,GREEN,bright_green,rungame)
        button("QUIT",550,550,100,50,RED,bright_red,quitgame)


        pygame.display.update()
        clock.tick(15)

class Cactus(pygame.sprite.Sprite):
    def __init__ (self,width,height, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([width,height])
        #self.image.fill(color)
        self.x = x
        self.y = y
        self.image = pygame.image.load("cactus.png").convert()
        self.rect = pygame.Rect(self.x, self.y, 117, 160)

        self.image.set_colorkey(white)
        screen.blit(self.image, [x, y])
        #pygame.display.flip()

        #self.rect = self.image.get_rect()
class Dino(pygame.sprite.Sprite):
    def  __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([width,height])
        #self.image.fill(color)

        self.image = pygame.image.load("Hankk_the_dino.png").convert()
        self.x = x
        self.y = y
#self.rect determines the location stored for the computer to know where you are
        self.rect = pygame.Rect(self.x, self.y, 80, 84)
        self.height = 0
        self.reach = True

        self.image.set_colorkey(white)
        screen.blit(self.image, [x, y])

    def jump(self):
        if not self.reach:
            if self.height != 250:
                self.rect.y -= 25
                self.height += 25
            else: self.reach = True
    def fall(self):
        if self.reach:
            if self.height != 0:
                self.rect.y += 25
                self.height -= 25

#Sets up a group to control all cacti. Cac_list has all of the cacti in it.
cac_list = pygame.sprite.Group()
#Creates 5 cacti with the Cactus class and adds them to the Cac_list for collision detection
def makecactusgroup():
    for i in range(5):
        xval = 1280 + random.randrange(700)
        cac = Cactus(100, 160, xval, 420)
    #    Cactus(117, 160, cac.rect.x, cac.rect.y)

        cac_list.add(cac)
#Creates a dinosaur with the Dino class and sets its initial positions
dino = Dino(90, 84, 0, 460)


def rungame():
    highscoreread = open("highscore.txt","r")
    highscore = int(highscoreread.read())
    highscoreread.close()
    initialtime = pygame.time.get_ticks()
    pygame.sprite.Group.empty(cac_list)
    makecactusgroup()
#While done is False, the game contines to run
    done = False
#Sets up an empty list which will be used to record the x values of the cacti
    cacxval = []
    speed = 15
    level = 1
    score = 0
    while not done:
#Allows the game to close if the player clicks the X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return True
#Allows the player to jump if they press up and if they are on the ground
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dino.rect.y == 460:
                    dino.reach = False
        dino.jump()
        dino.fall()
#Resets the screen so that it can be updated with the drawings for every loop
        screen.fill(white)
        background_image = pygame.image.load("Mountain_desert.png")

        screen.blit(background_image, [0,0])
        text1 = font.render("Dino Dash", True, white)
        screen.blit(text1, [401, 40])
        pygame.display.flip()
#Draws a green, 20x20 cactus in its previously determined x and y position for every cactus in cac_list
        for cac in cac_list:
            #pygame.draw.rect(screen,GREEN,[cac.rect.x,cac.rect.y,20,20])
            Cactus(10, 100, cac.rect.x, cac.rect.y)

#Prevents cacti from being too close together. Each cactus goes through
#the cacxval list and compares its x coordinate with the others to see if they are
#too close. If it is within 150 pixels of another, the cactus's x value is added to until it isn't.
            for xval in cacxval:
                while abs(cac.rect.x - xval) <=350:
                    cac.rect.x += 25
#The new xvalue of the cactus is added to the list of cacti xvalues for the next cacti to compare with.
            cacxval += [cac.rect.x]
#Moves the cacti towards the dino.
            cac.rect.x -= speed
#When the cacti goes to the end of the screen, reset its position to
#the end plus a random extra value to have more randomized pattern of cacti appearance.
            if cac.rect.x < -100:
                cac.rect.x = 1280 + random.randrange(700)
#empties the cacxval list so that old cacti that have been reset are not considered
        cacxval = []
#draws the dinosaur
        #pygame.draw.rect(screen,BLUE,[dino.rect.x,dino.rect.y,20,20])
        Dino(90, 84, dino.rect.x, dino.rect.y)
#makes a list that is added to everytime the dino collides with a cactus
        cac_hit_list = pygame.sprite.spritecollide(dino,cac_list,True)
#if the collision list has something in it, (thus there was a collision),
#a game over message prints and the game loop is ended.
        if len(cac_hit_list) > 0:
            if score > highscore:
                highscorewrite = open("highscore.txt","w")
                highscorewrite.write(str(score))
                highscorewrite.close()
            done = True
#Makes a variable for the score, constantly updating with the time
        score = (pygame.time.get_ticks()-initialtime)//100
#Displays the score
        if level < (score / 25):
            speed *= SPEED_FACTOR
            level += 1
        text = font.render("Score: " + str(score),True,BLACK)
        highscoretext = font.render("High Score: " + str(highscore),True, BLACK)
        screen.blit(text, [840, 40])
        screen.blit(highscoretext, [800,80])
#Displays all of the changes made for the dino and cacti every loop
        pygame.display.flip()
#Loops 30 times a second
        clock.tick(30)
#closes the game if done = True

def main():
    game_intro()
    close = False
    while close == False:
        decision = False
        if rungame() == True:
            decision = True
            close = True
        while decision == False:
            screen.blit(gameovertext,[50,200])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    decision = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        close = True
                        decision = True
                    elif event.key == pygame.K_LEFT:
                        decision = True

    pygame.quit()
main()
