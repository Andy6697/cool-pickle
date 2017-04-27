import pygame
import math
import random
import cactus
import dino
pygame.init()

SIZE_OF_OBJECTS = 20
#size used for the dino and cactus objects
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
#colors used for the objects and the screen

def declare_cactus():
    #establishes the cactus object
    cac_list = pygame.sprite.Group()
    all_stuff = pygame.sprite.Group()
    #list definition
    cac = cactus(GREEN, 20, 20)
    cac.rect.x = random.randrange(660)
    cac.rect.y = 460
    cac_list.add(cac)
    all_stuff.add(cac)


def declare_dino():
    #establishes the dino object
    dino = Dino(BLUE, 20, 20)
    dino.rect.x = 0
    dino.rect.y = 460


def screen_set():
    #sets the colors for the screen and characters and the screen size
    size = (700,500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("DINO DASH")
    screen.fill(WHITE)

def play_game():
    #defines the event loop for the duration of the game
    for i in range(5):
        declare_cactus()
    declare_dino()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                continue
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dino.jump()
        dino.fall()
        pygame.display.flip()
        clock.tick(30)

def end_game():
    #sets the parameters for which the game can use to end
    for cact in cac_list:
        pygame.draw.rect(screen,GREEN,[cac.rect.x,cac.rect.y,20,20])
        cac.rect.x -= 1
    pygame.draw.rect(screen,BLUE,[dino.rect.x,dino.rect.y,20,20])
    cac_hit_list = pygame.sprite.spritecollide(dino,cac_list,True)
    if len(cac_hit_list) > 0:
        print("YOU SUCK GAME OVER")
        done = True
    pygame.quit()

def main():
    done = False
    clock = pygame.time.Clock()
    screen_set()
    play_game()
    end_game()
main()
