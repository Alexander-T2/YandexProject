import pygame


class Spikes(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        spikes_path = r'graphics/spikes/spikes1.png'
        self.image = pygame.image.load(spikes_path).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos)
        self.killable = 1

    def update(self, x_shift):
        self.rect.x += x_shift
