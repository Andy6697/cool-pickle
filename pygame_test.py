import pygame

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT
			done = True
	#game logic/code
	pygame.display.flip()
	clock.tick(60)
pygame.quit()
