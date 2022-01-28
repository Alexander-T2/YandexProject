import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.frame_index = 0  # for animation
        door_path = r'graphics/door/door.png'
        self.image = pygame.image.load(door_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
