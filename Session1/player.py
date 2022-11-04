import pygame
import math
import random

class Player(pygame.sprite.Sprite):
    # this class represents the player
    def __init__(self, x, y, color, ):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.health = 50


    def update(self):
        # move up and down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # check if the player hits a wall
        block_hit_list = pygame.sprite.spritecollide(self, wall_list, False)
        for block in block_hit_list:
            if self.speed > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
