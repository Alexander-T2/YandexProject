import pygame
import sys
from drawable.tiles import Tile
from drawable.door import Door
from settings.settings import tile_size, screen_width
from settings import settings
from player import Player
from drawable.menu import Menu


class Level:
    def __init__(self, level_data, surface):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.door = pygame.sprite.GroupSingle()
        self.menu = Menu()
        self.display_surface = surface
        self.setup_level(level_data)
        self.mc = (650, 150)
        self.ma = r"graphics\background"
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles.empty()
        self.player.empty()
        self.door.empty()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'D':
                    door = Door((x + 2, y - 22), tile_size)
                    self.door.add(door)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 6
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -6
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6

    def menu_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if settings.menu_state != 1:
                        settings.menu_state += 1
                    else:
                        settings.menu_state = 0
            if event.type == pygame.MOUSEBUTTONUP:
                print(event.pos)

    def run(self):
        if settings.menu_state == 0:
            self.tiles.update(self.world_shift)
            self.door.update(self.world_shift)
            self.player.update(self.tiles.sprites(), self.door.sprites())
            self.scroll_x()
        self.tiles.draw(self.display_surface)
        self.door.draw(self.display_surface)

        self.player.draw(self.display_surface)

        if settings.menu_state == 1:
            st = 100
            x = 125
            y = 80
            self.menu.open(self.display_surface, rf'{self.ma}\menu.png', (650, 150))
            self.menu.open(self.display_surface, rf'{self.ma}\continue_btn.png', (self.mc[0]+x, self.mc[1]+st))
            self.menu.open(self.display_surface, rf'{self.ma}\choose_btn.png', (self.mc[0]+x, self.mc[1]+2*y+st))
            self.menu.open(self.display_surface, rf'{self.ma}\exit_btn.png', (self.mc[0]+x, self.mc[1]+4*y+st))
        self.menu_check()
