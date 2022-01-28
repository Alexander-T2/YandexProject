import pygame
from settings import settings
from settings.support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.import_character_assets()
        self.status = 'idle'
        self.facing_right = True
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos)

        self.import_run_particles()
        self.dust_frame_index = 0
        self.run_dust_animation_speed = 0.15
        self.display_surface = surface

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 6
        self.gravity = 1
        self.jump_height = -22
        self.on_ground = False
        self.start_x = 900
        self.start_y = 66

    def import_character_assets(self):
        character_path = 'graphics/character/'

        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def import_run_particles(self):
        path = 'graphics/character/dust_particles/run'
        self.dust_run_particles = import_folder(path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        self.image.set_colorkey((255, 255, 255))

    def run_dust_animation(self):
        if self.status == 'run' and self.on_ground:
            self.dust_frame_index += self.run_dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(46, 37)
                dust_particle.set_colorkey((255, 255, 255))
                self.display_surface.blit(dust_particle, pos)
            else:
                pos = self.rect.bottomleft - pygame.math.Vector2(-30, 35)
                flipped_particle = pygame.transform.flip(dust_particle, True, False)
                flipped_particle.set_colorkey((255, 255, 255))
                self.display_surface.blit(flipped_particle, pos)

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > self.gravity:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def get_input(self):
        if settings.menu_state != 1:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and self.on_ground:
                self.jump()
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.facing_right = True
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.facing_right = False
            else:
                self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_height

    def update(self, tile_sprites, door_sprites, spikes_sprites, key_sprites, button_sprites, lock_sprites):
        self.get_input()
        self.get_status()
        self.animate()
        self.run_dust_animation()
        self.horizontal_movement_collision(tile_sprites, lock_sprites)
        self.vertical_movement_collision(tile_sprites, lock_sprites)
        self.spike_touched(spikes_sprites)
        self.door_touched(door_sprites)
        self.key_acquired(key_sprites)
        self.button_pressed(button_sprites, lock_sprites)

    def horizontal_movement_collision(self, tile_sprites, lock_sprites):
        if 0 < self.rect.centerx < 1800 - 50:
            self.rect.x += self.direction.x * self.speed

        for sprite in tile_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                elif self.direction.x > 0:
                    self.rect.right = sprite.rect.left

        for sprite in lock_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                elif self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_movement_collision(self, tile_sprites, lock_sprites):
        self.apply_gravity()
        for sprite in tile_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_ground = True
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        for sprite in lock_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_ground = True
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        if self.on_ground and self.direction.y < 0 or self.direction.y > 1:
            self.on_ground = False

    def spike_touched(self, spikes_sprites):
        for sprite in spikes_sprites:
            if sprite.rect.colliderect(self.rect):
                if settings.current_level != 3:
                    settings.dead_state = 1
                else:
                    if sprite.killable:
                        sprite.image = pygame.image.load(r'graphics/spikes/spikes2.png').convert_alpha()
                        sprite.image.set_colorkey((255, 255, 255))
                        sprite.killable = 0
                        self.rect.centerx = self.start_x
                        self.rect.centery = self.start_y

                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                        self.direction.y = 0
                        self.on_ground = True
                    elif self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y = 0
                    else:
                        if self.direction.x < 0:
                            self.rect.left = sprite.rect.right
                        elif self.direction.x > 0:
                            self.rect.right = sprite.rect.left

    def button_pressed(self, button_sprites, lock_sprites):
        tmp = None
        for sprite in button_sprites:
            if sprite.rect.colliderect(self.rect):
                sprite.image = pygame.image.load(r'graphics/button/btnon.png').convert_alpha()
                sprite.image.set_colorkey((255, 255, 255))
                tmp = sprite
        if tmp:
            lock_sprites.empty()

    def key_acquired(self, key_sprites):
        key = None
        for sprite in key_sprites:
            if sprite.rect.colliderect(self.rect):
                settings.door_locked = 0
                key = sprite
        if key:
            key_sprites.empty()

    def door_touched(self, door_sprites):
        for sprite in door_sprites:
            if sprite.rect.colliderect(self.rect):
                if settings.door_locked != 1 or settings.current_level == 1:
                    settings.door_locked = 1
                    settings.current_level += 1
