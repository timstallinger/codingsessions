import pygame
from spritehandler import *
from config import *
from items import *

class Player(pygame.sprite.Sprite):
    # this class represents the player
    def __init__(self, game, x, y, spritesh = "assets/Characters/animated.png", imx = 64, imy = 0, scale = 1, enemy = False):
        self.enemy = enemy
        if self.enemy:
            self._layer = ENEMY_LAYER
            self.groups = game.all_sprites, game.enemies
        else:
            self._layer = PLAYER_LAYER
            self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.speed = 5
        self.health = 50
        self.sprite = spritesheet(spritesh)
        self.image = self.sprite.image_at((imx,imy,16,16))
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.step = 0
        self.direction = 1
        self.imagerow = [self.image for i in range(4)]
        self.special = None
        self.moving = False

    # never called?
    def update(self):
        if self.moving:
            self.step += 1
            self.image = self.imagerow[self.direction*3 + int(self.step/6) % 3]
            self.image = pygame.transform.scale(self.image, (32,32))
        else:
            self.image = self.imagerow[self.direction*3]
            self.image = pygame.transform.scale(self.image, (32,32))
        # check if the player hits a wall
        block_hit_list = pygame.sprite.spritecollide(self, self.game.blocks, False)
        for block in block_hit_list:
            self.game.playing = False
        if self.health <= 0 and self.enemy:
            self.image = pygame.transform.rotate(self.image, 90)
            Item(self.game, "health", self.rect.x+10, self.rect.y+10, "assets/Items/Potion.png", 0, 0)