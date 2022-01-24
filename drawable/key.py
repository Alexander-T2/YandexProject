import pygame


class Key(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        key_path = r'graphics/background/key.png'
        self.image = pygame.image.load(key_path).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift