import pygame
from random import randint
from settings import settings


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.sprites = {
                        1: r'graphics/tiles/tile1.png', 2: r'graphics/tiles/tile2.png',
                        3: r'graphics/tiles/tile3.png', 4: r'graphics/tiles/tile4.png',
                        5: r'graphics/tiles/tile5.png', 6: r'graphics/tiles/tile6.png',
                        7: r'graphics/tiles/tile7.png', 8: r'graphics/tiles/tile8.png',
                        9: r'graphics/tiles/tile9.png', 10: r'graphics/tiles/tile10.png',
                        11: r'graphics/tiles/tile11.png', 12: r'graphics/tiles/tile12.png'
                        }
        tile_path = self.sprites[randint(1, 4) + 4 * (settings.current_level - 1)]
        self.image = pygame.image.load(tile_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
