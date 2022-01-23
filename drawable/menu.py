import pygame


class Menu:
    def __init__(self):
        self.width = 500
        self.height = 610

    def open(self, surface, adress, pos):
        surface.blit(pygame.image.load(adress), pos)
