import pygame
from support import import_folder


class Door(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.frame_index = 0  # for animation
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
    '''
        self.image = self.animations['close'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def import_character_assets(self):
        door_path = 'graphics/door/'
        self.animations = {'close': []}

        for animation in self.animations.keys():
            full_path = door_path + animation
            self.animations[animation] = import_folder(full_path)
    '''

    def update(self, x_shift):
        self.rect.x += x_shift
