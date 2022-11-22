import pygame
from config import *
from spritehandler import *


BLACK = ( 0, 0, 0)
# class Bullet
# this class represents the bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction, special,scale = 1, damage = 10):
        self._layer = BULLET_LAYER
        self.groups = game.all_sprites, game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.damage = damage
        if special == "nuke":
            self.image = spritesheet("assets/Objects/Effect0.png").image_at((112,352,16,16))
            self.image = pygame.transform.scale(self.image, (32*scale,32*scale))
            self.damage = 100
        else:
            self.image = spritesheet("assets/Objects/Effect0.png").image_at((96,353,16,16))
            self.image = pygame.transform.scale(self.image, (16*scale,16*scale))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4
        # direction is tuple (x, y)
        self.direction = direction

    def update(self):
        # update position according to direction and speed
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

        block_hit_list = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if block_hit_list:
            self.kill()

        # check if the bullet hits an enemy
        enemy_hit_list = pygame.sprite.spritecollide(self, self.game.enemies, False)
        for enemy in enemy_hit_list:
            enemy.health -= self.damage
            print(enemy.health)
            self.kill()

