import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

size = (1280, 809)
screen = pygame.display.set_mode(size)

#Loop until close button-clicked
screen.fill(WHITE)

background_image = pygame.image.load("Mountain_desert.png")
screen.blit(background_image, [0,0])
pygame.display.set_caption("Dino Dash")
font = pygame.font.SysFont('Wide Latin', 50, True, False) #(font, size,bold,italics)

text = font.render("Dino Dash", True, WHITE)
screen.blit(text, [401, 40])

#text2 = font.render("Score: " + str(score), True, BLACK)
#screen.blit(text2, [700,40])

player_image = pygame.image.load("bunny1_ready.png").convert()
player_image.set_colorkey(WHITE)

screen.blit(player_image, [80, 600])


#for below: Would I put the additional player images here and then add the names (player_jump, player_walk1, 
#player_walk2, etc.), below in the loop or here?

#player_jump = pygame.image.load("bunny1_jump.png")
#player_jump.set_colorkey(WHITE)

#player_walk1 = pygame.image.load("bunny1_walk1.png")
#player_walk2 = pygame.image.load("bunny1_walk2.png")
#player_walk1.set_colorkey(WHITE)
#player_walk2.set_colorkey(WHITE)

#screen.blit(player_image, [80, 600])


pygame.display.flip()

done = False

clock = pygame.time.Clock()
#mainloop
while not done:
    #main event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            player_jump = pygame.image.load("bunny1_jump.png")
                player_jump.set_colorkey(WHITE)
                screen.blit(player_jump, [80, 470])
                
                
       #Should I incoroporate this would the sprite dino class? 
        #I also think I'd need help for loop for the walking images 
        # 
pygame.display.flip()


clock.tick(60)
#player_image =

pygame.quit()
