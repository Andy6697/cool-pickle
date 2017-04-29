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
