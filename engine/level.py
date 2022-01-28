import pygame
import sys
from drawable.tiles import Tile
from drawable.door import Door
from drawable.spikes import Spikes
from drawable.key import Key
from settings.settings import tile_size, screen_width
from settings import settings
from engine.player import Player
from drawable.menu import Menu
from drawable.button import Button
from drawable.lock import Lock


class Level:
    def __init__(self, level_data, surface):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.door = pygame.sprite.GroupSingle()
        self.spikes = pygame.sprite.Group()
        self.key = pygame.sprite.GroupSingle()
        self.button = pygame.sprite.GroupSingle()
        self.lock = pygame.sprite.Group()
        self.menu = Menu()
        self.start_pos = (0, 0)
        self.display_surface = surface
        self.setup_level(level_data)
        self.mc = (650, 150)
        self.ma = r"graphics\menu"
        self.world_shift = 0
        self.tmp = ()

    def setup_level(self, layout):
        self.tiles.empty()
        self.player.empty()
        self.door.empty()
        self.spikes.empty()
        self.key.empty()
        self.button.empty()
        self.lock.empty()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x, y))
                    self.tiles.add(tile)
                elif cell == 'S':
                    spike = Spikes((x + 1, y + 27))
                    self.spikes.add(spike)
                elif cell == 'D':
                    door = Door((x + 2, y - 11))
                    self.door.add(door)
                elif cell == 'K':
                    key = Key((x + 12, y + 15))
                    self.key.add(key)
                elif cell == 'B':
                    button = Button((x, y))
                    self.button.add(button)
                elif cell == 'L':
                    lock = Lock((x, y))
                    self.lock.add(lock)
                elif cell == 'P':
                    player_sprite = Player((x, y), self.display_surface)
                    self.player.add(player_sprite)
                    self.start_pos = (x, y)

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
                if event.key == pygame.K_f:
                    settings.game_started = 1
                if event.key == pygame.K_ESCAPE:
                    if settings.menu_state != 1:
                        settings.menu_state += 1
                    else:
                        if settings.menu_choose == 0:
                            settings.menu_state = 0
                        else:
                            settings.menu_choose = 0
            if event.type == pygame.MOUSEBUTTONUP:
                if settings.menu_choose != 1:
                    st = event.pos
                    nd = self.mc
                    if (st[0] >= nd[0]+125) and (st[0] <= nd[0] + 375) and (st[1] >= 250) and (st[1] <= 330):
                        settings.menu_state = 0
                    elif (st[0] >= nd[0]+125) and (st[0] <= nd[0] + 375) and (st[1] >= 410) and (st[1] <= 490):
                        settings.menu_choose = 1
                    elif (st[0] >= nd[0]+125) and (st[0] <= nd[0] + 375) and (st[1] >= 570) and (st[1] <= 650):
                        sys.exit()
                else:
                    st = event.pos
                    nd = self.mc
                    if (st[0] >= nd[0] + 125) and (st[0] <= nd[0] + 375) and (st[1] >= 250) and (st[1] <= 330):
                        settings.current_level = 1
                    elif (st[0] >= nd[0] + 125) and (st[0] <= nd[0] + 375) and (st[1] >= 410) and (st[1] <= 490):
                        settings.current_level = 2
                    elif (st[0] >= nd[0] + 125) and (st[0] <= nd[0] + 375) and (st[1] >= 570) and (st[1] <= 650):
                        settings.current_level = 3

    def run(self):
        if settings.current_level != 4:
            if settings.menu_state == 0:
                self.tiles.update(self.world_shift)
                self.door.update(self.world_shift)
                self.key.update(self.world_shift)
                self.spikes.update(self.world_shift)
                self.player.update(self.tiles.sprites(), self.door.sprites(), self.spikes.sprites(), self.key,
                                   self.button, self.lock)
                self.button.update(self.world_shift)
                self.lock.update(self.world_shift)
                self.scroll_x()
            self.lock.draw(self.display_surface)
            self.button.draw(self.display_surface)
            self.spikes.draw(self.display_surface)
            self.tiles.draw(self.display_surface)
            self.door.draw(self.display_surface)
            self.key.draw(self.display_surface)

            self.player.draw(self.display_surface)

        if settings.menu_state == 1:
            st = 100
            x = 125
            y = 80
            self.menu.open(self.display_surface, rf'{self.ma}\menu.png', (650, 150))
            if settings.menu_choose == 1:
                self.menu.open(self.display_surface, rf'{self.ma}\lvl1.png',
                               (self.mc[0] + x, self.mc[1] + st))
                self.menu.open(self.display_surface, rf'{self.ma}\lvl2.png',
                               (self.mc[0] + x, self.mc[1] + 2 * y + st))
                self.menu.open(self.display_surface, rf'{self.ma}\lvl3.png',
                               (self.mc[0] + x, self.mc[1] + 4 * y + st))

            else:
                self.menu.open(self.display_surface, rf'{self.ma}\continue_btn.png',
                               (self.mc[0] + x, self.mc[1] + st))
                self.menu.open(self.display_surface, rf'{self.ma}\choose_btn.png',
                               (self.mc[0] + x, self.mc[1] + 2 * y + st))
                self.menu.open(self.display_surface, rf'{self.ma}\exit_btn.png',
                               (self.mc[0] + x, self.mc[1] + 4 * y + st))

        self.menu_check()
