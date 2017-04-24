import pygame
import math
import random
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

size = (700,500)
screen = pygame.display.set_mode(size)

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

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
    def update(self):
        self.calc_grav() #Gravity
    def jump(self):
        self.rect.y -= 40
        self.height += 40
    def fall(self):
        if self.height != 0:
            self.rect.y +=1
            self.height -=1






done = False
clock = pygame.time.Clock()
cac_list = pygame.sprite.Group()
all_stuff = pygame.sprite.Group()
for i in range(5):
    cac = Cactus(GREEN,20,20)
    cac.rect.x = random.randrange(660)
    cac.rect.y = 460
    cac_list.add(cac)
    all_stuff.add(cac)
dino = Dino(BLUE,20,20)
dino.rect.x = 0
dino.rect.y = 460
all_stuff.add(dino)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            continue
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dino.jump()
    dino.fall()


    screen.fill(WHITE)

    for cact in cac_list:
        pygame.draw.rect(screen,GREEN,[cac.rect.x,cac.rect.y,20,20])
        cac.rect.x -= 1
    pygame.draw.rect(screen,BLUE,[dino.rect.x,dino.rect.y,20,20])
    cac_hit_list = pygame.sprite.spritecollide(dino,cac_list,True)
    if len(cac_hit_list) > 0:
        print("YOU SUCK GAME OVER")
        done = True
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
