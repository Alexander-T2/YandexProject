import pygame
from settings.settings import *
from settings import settings
from engine.level import Level


pygame.init()
pygame.display.set_caption("Redemption ark")
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
actual_level = 1
level = Level(levels[actual_level], screen)
backgrounds = {0: r'graphics/background/background0.png',
               1: r'graphics/background/background1.png',
               2: r'graphics/background/background2.png',
               3: r'graphics/background/background3.png',
               4: r'graphics/background/background4.png'}
back_ground = pygame.image.load(backgrounds[settings.current_level])

while True:
    if settings.current_level != actual_level:
        if settings.current_level != 4:
            actual_level = settings.current_level
            level.setup_level(levels[settings.current_level])
        back_ground = pygame.image.load(backgrounds[settings.current_level])
    screen.blit(back_ground, (0, 0))
    level.run()
    if settings.dead_state == 1:
        settings.door_locked = 1
        settings.dead_state = 0
        level.setup_level(levels[settings.current_level])
    if settings.game_started == 0:
        screen.blit(pygame.image.load(backgrounds[0]), (0, 0))

    pygame.display.update()
    clock.tick(60)
