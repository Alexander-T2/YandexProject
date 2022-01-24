import pygame
from settings import settings
from settings.support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0  # for animation
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.jump_counter = 1
        self.dead_state = 0

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 6
        self.gravity = 1
        self.jump_height = -25

    def import_character_assets(self):
        character_path = 'graphics/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.get_status()]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 0:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def get_input(self):
        if settings.menu_state != 1:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and self.jump_counter > 0:
                self.jump()
                self.jump_counter -= 1
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
            else:
                self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_height

    def update(self, tile_sprites, door_sprites):
        self.get_input()  # Menu work starts here
        self.horizontal_movement_collision(tile_sprites)
        self.vertical_movement_collision(tile_sprites)
        self.door_touched(door_sprites)

    def horizontal_movement_collision(self, tile_sprites):
        self.rect.x += self.direction.x * self.speed

        for sprite in tile_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                elif self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_movement_collision(self, tile_sprites):
        self.apply_gravity()
        for sprite in tile_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.jump_counter = 1
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

    def door_touched(self, door_sprites):
        for sprite in door_sprites:
            if sprite.rect.colliderect(self.rect):
                settings.current_level += 1
