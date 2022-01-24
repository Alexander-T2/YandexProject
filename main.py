import pygame
from settings.settings import *
from settings import settings
from level import Level


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(levels[settings.current_level], screen)
back_ground = pygame.image.load('graphics/background/background2.png')
actual_level = 1

while True:
    if settings.current_level != actual_level:
        if settings.current_level != 4:
            actual_level = settings.current_level
            level.setup_level(levels[settings.current_level])
        else:
            settings.current_level = 0
    screen.blit(back_ground, (0, 0))
    level.run()
    if settings.dead_state == 1:
        settings.dead_state = 0
        level.setup_level(levels[settings.current_level])

    pygame.display.update()
    clock.tick(60)
