import pygame
import math
import random
pygame.init()

#All colors listed to be used for drawing
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
#Sets up the screen 
size = (700,500)
screen = pygame.display.set_mode(size)
#Sets up the clock for the tick rate and for the score
clock = pygame.time.Clock()
#Sets up an initial score and it's font to prepare for its display on screen
score = 0
font = pygame.font.SysFont('Calibri', 25, True, False)
pygame.display.set_caption("DINO DASH")



pygame.mixer.music.load('gameoverzelda.midi')
pygame.mixer.music.play(-1)




class Cactus(pygame.sprite.Sprite):
    def __init__ (self,color,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
class Dino(pygame.sprite.Sprite):
    def  __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.height = 0
        self.change_x = 0
        self.change_y = 0
    def calc_grav(self):
        if self.change_y == 0:
             self.change_y = 1
        else:
             self.change_y += 5


    def update(self):
        self.calc_grav() #Gravity
    def jump(self):
        self.rect.y -= 50
        self.height += 50
    def fall(self):
        if self.height != 0:
            self.rect.y +=2
            self.height -=2
#Sets up a group to control all cacti. Cac_list has all of the cacti in it.
cac_list = pygame.sprite.Group()
#Creates 5 cacti with the Cactus class and adds them to the Cac_list for collision detection
def makethings():
    for i in range(5):
        cac = Cactus(GREEN,20,20)
        cac.rect.x = 700 + random.randrange(700)
        cac.rect.y = 460
        cac_list.add(cac)
#Creates a dinosaur with the Dino class and sets its initial positions
dino = Dino(BLUE,20,20)
dino.rect.x = 0
dino.rect.y = 460

def run():
    makethings()
#While done is False, the game contines to run
    done = False
#Sets up an empty list which will be used to record the x values of the cacti
    cacxval = []
    while not done:
#Allows the game to close if the player clicks the X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
#Allows the player to jump if they press up and if they are on the ground
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dino.rect.y == 460:
                    dino.jump()
        dino.fall()
#Resets the screen so that it can be updated with the drawings for every loop
        screen.fill(WHITE)
#Draws a green, 20x20 cactus in its previously determined x and y position for every cactus in cac_list
        for cac in cac_list:
            pygame.draw.rect(screen,GREEN,[cac.rect.x,cac.rect.y,20,20])
#Prevents cacti from being too close together. Each cactus goes through
#the cacxval list and compares its x coordinate with the others to see if they are
#too close. If it is within 150 pixels of another, the cactus's x value is added to until it isn't.
            for xval in cacxval:
                while abs(cac.rect.x - xval) <=150:
                    cac.rect.x += 25
#The new xvalue of the cactus is added to the list of cacti xvalues for the next cacti to compare with.
            cacxval += [cac.rect.x]
#Moves the cacti towards the dino. 
            cac.rect.x -= 6
#When the cacti goes to the end of the screen, reset its position to
#the end plus a random extra value to have more randomized pattern of cacti appearance.
            if cac.rect.x < -20:
                cac.rect.x = 700 + random.randrange(700)
#empties the cacxval list so that old cacti that have been reset are not considered
        cacxval = []
#draws the dinosaur
        pygame.draw.rect(screen,BLUE,[dino.rect.x,dino.rect.y,20,20])
#makes a list that is added to everytime the dino collides with a cactus
        cac_hit_list = pygame.sprite.spritecollide(dino,cac_list,True)
#if the collision list has something in it, (thus there was a collision),
#a game over message prints and the game loop is ended.
        if len(cac_hit_list) > 0:
            print("YOU SUCK GAME OVER")
            done = True
#Makes a variable for the score, constantly updating with the time
        score = pygame.time.get_ticks()//100
#Displays the score
        text = font.render("Score: " + str(score),True,BLACK)        
        screen.blit(text, [550, 0])
#Displays all of the changes made for the dino and cacti every loop
        pygame.display.flip()
#Loops 30 times a second
        clock.tick(30)
#closes the game if done = True
    pygame.quit()
def main():
    run()
main()
