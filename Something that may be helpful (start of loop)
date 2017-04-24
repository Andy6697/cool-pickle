#Snake game
import os
import pygame
from pygame.locals import *

#we import the ibrarires and warn user if font or sound things not available
if not pygame. font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

#create class this class handles the main initialization and creating of the game
class PyManMain:
    def __init__(self, width=640, height=480):
        print("Initialize")
        """Initialize Pygame"""
        pygame.init()
        """Set the window size"""
        self.width = width
        self.height = height
        """Create Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        #the init function takes two optional parameteres height and width
        #init basically initializes pygame (pygame.init()) and then creates
        #main screen using pygame.display.set_mode function

    def mainloop(self):
        """The main loop of game"""
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif: event.type == KEYDOWN:
                    if((event.key == K_SPACE)
                    or (event.key == L_DOWN)):
                        self.dino.move(event.key)

                if __name__ == "__main__":
                    MainWindow = PyManMain()
                    MainWindow.mainloop()
class Dino(pygame.sprite.Sprite):
    #This is our dinosaur
    def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image, self.rect = load_image('dinosaur.png', -1)
    self.distance_walked = 0 #pellets were used here for number pellets eaten
    #we can use for number of cacti jumped

    def move(self, key):
        #will move in either "jump" by pressing space or "duck" for down
        xMove = 0
        yMove = 0

        if (key == K_SPACE):
            xMove = self.x_dist


    """Check for Collision"""
    firstCol = pygame.sprite.spritecollide(self.dino, self.cactus_sprites, True)
