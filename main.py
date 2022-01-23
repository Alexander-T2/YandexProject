import pygame
from settings.settings import *
from settings import settings
from level import Level


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(levels[settings.current_level], screen)
back_ground = pygame.image.load('graphics/background/background.png')
actual_level = 1

while True:
    if settings.current_level != actual_level:
        actual_level = settings.current_level
        level.setup_level(levels[settings.current_level])
    screen.blit(back_ground, (0, 0))
    level.run()

    pygame.display.update()
    clock.tick(60)
