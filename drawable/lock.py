import pygame


class Lock(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        lock_path = r'graphics/lock/lock.png'
        self.image = pygame.image.load(lock_path).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
