import pygame
from spritehandler import *
from config import *

class Player(pygame.sprite.Sprite):
    # this class represents the player
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.layer = PLAYER_LAYER
        self.speed = 5
        self.health = 50
        self.sprite = spritesheet("assets/Characters/animated.png")
        self.image = self.sprite.image_at((64,0,16,16))
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.step = 0
        self.direction = 1
        self.imagerow = None
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
            print("hit wall, dead.")
            self.game.playing = False