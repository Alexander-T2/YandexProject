import pygame, sys
from settings import *
from level import Level


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map1, screen)
back_ground = pygame.image.load('graphics/background/background.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(back_ground, (0, 0))
    level.run()

    pygame.display.update()
    clock.tick(60)
