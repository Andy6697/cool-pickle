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
    screen.fill(WHITE)

    for cac in cac_list:
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
