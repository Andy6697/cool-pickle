import pygame
import math
import random
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

SPEED_FACTOR = 1.1
size = (700,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont('Calibri', 25, True, False)
gameovertext = font.render("GAME OVER! PRESS LEFT TO RESTART OR DOWN TO QUIT",True,BLACK)
pygame.display.set_caption("DINO DASH")



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
        #self.imagae = pygame.image.load("<name of image file>").convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.height = 0
        self.reach = True
        self.change_x = 0
        self.change_y = 0
    def calc_grav(self):
        if self.change_y == 0:
             self.change_y = 1
        else:
             self.change_y += 5

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
    def update(self):
        self.calc_grav() #Gravity
    def jump(self):
        if not self.reach:
            if self.height != 50:
                self.rect.y -= 5
                self.height += 5
            else: self.reach = True
    def fall(self):
        if self.reach:
            if self.height != 0:
                self.rect.y +=5
                self.height -=5

cac_list = pygame.sprite.Group()
all_stuff = pygame.sprite.Group()
def makecactusgroup():
    for i in range(5):
        cac = Cactus(GREEN,20,20)
        cac.rect.x = 700 + random.randrange(700)
        cac.rect.y = 460
        cac_list.add(cac)
dino = Dino(BLUE,20,20)
dino.rect.x = 0
dino.rect.y = 460

def run():
    highscoreread = open("highscore.txt","r")
    highscore = int(highscoreread.read())
    highscoreread.close()
    initialtime = pygame.time.get_ticks()
    pygame.sprite.Group.empty(cac_list)
    makecactusgroup()
    print(cac_list)
    done = False
    cacxval = []
    speed = 6
    level = 1
    score = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dino.rect.y == 460:
                    dino.reach = False
        dino.jump()
        dino.fall()
        screen.fill(WHITE)
        for cac in cac_list:
            pygame.draw.rect(screen,GREEN,[cac.rect.x,cac.rect.y,20,20])
            for xval in cacxval:
                while abs(cac.rect.x - xval) <= 150:
                    cac.rect.x += 25
            cacxval += [cac.rect.x]
            cac.rect.x -= speed
            if cac.rect.x < -20:
                cac.rect.x = 700 + random.randrange(700)
        cacxval = []
        pygame.draw.rect(screen,BLUE,[dino.rect.x,dino.rect.y,20,20])
        cac_hit_list = pygame.sprite.spritecollide(dino,cac_list,True)
        if len(cac_hit_list) > 0:
            if score > highscore:
                highscorewrite = open("highscore.txt","w")
                highscorewrite.write(str(score))
                highscorewrite.close()
            print("YOU SUCK GAME OVER")
            done = True
            screen.fill(WHITE)
        score = (pygame.time.get_ticks()-initialtime)//100
        if level < (score / 50):
            speed*=SPEED_FACTOR
            level += 1
        text = font.render("Score: " + str(score),True,BLACK)
        highscoretext = font.render("High Score: " + str(highscore),True, BLACK)
        screen.blit(text, [550, 0])
        screen.blit(highscoretext, [530,20])
        pygame.display.flip()
        clock.tick(30)

def main():
    close = False
    while close == False:
        decision = False
        if run() == True:
            decision = True
            close = True
        while decision == False:
            screen.blit(gameovertext,[50,200])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                    decision = True
                if event.type ==pygame.KEYDOWN:
                    if event.key ==pygame.K_DOWN:
                        close = True
                        decision = True
                    elif event.key ==pygame.K_LEFT:
                        decision = True
                    
    pygame.quit()
main()

