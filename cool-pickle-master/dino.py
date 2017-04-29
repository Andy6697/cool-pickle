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
