import pygame

class Cactus(pygame.sprite.Sprite):
    def __init__ (self,width,height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("cactus.png").convert()
        self.rect = pygame.Rect(self.x, self.y, 60, 84)

class Dino(pygame.sprite.Sprite):
    def  __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Hankk_the_dino.png").convert()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 60, 84)
        self.height = 0
        self.reach = True

    def jump(self):
        if not self.reach:
            if self.height != 180:
                self.rect.y -= 15
                self.height += 15
            else: self.reach = True
    def fall(self):
        if self.reach:
            if self.height != 0:
                self.rect.y += 15
                self.height -= 15
