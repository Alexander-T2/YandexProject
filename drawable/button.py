import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, spis=[]):
        super().__init__()
        self.spis = spis
        btn_path = r'graphics/button/btnoff.png'
        self.image = pygame.image.load(btn_path).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
