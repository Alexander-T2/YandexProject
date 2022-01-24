import pygame
from random import randint


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # self.image = pygame.Surface((size, size))
        self.sprites = {1: r'graphics/tiles/tile1.png', 2: r'graphics/tiles/tile2.png',
                        3: r'graphics/tiles/tile3.png', 4: r'graphics/tiles/tile4.png'}
        tile_path = self.sprites[randint(1, 4)]
        self.image = pygame.image.load(tile_path).convert_alpha()
        # self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
