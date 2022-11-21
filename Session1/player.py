import pygame
from spritehandler import *

class Player(pygame.sprite.Sprite):
    # this class represents the player
    def __init__(self, x, y, sprite, im_x, im_y):
        super().__init__()
        self.speed = 5
        self.health = 50
        self.sprite = spritesheet(sprite)
        self.image = self.sprite.image_at((im_x,im_y,16,16))
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.step = 0
        self.direction = 1
        self.imagerow = None

    # never called?
    def update(self, wall_list):
        if self.moving:
            self.step += 1
            self.image = self.imagerow[int(self.step/6) % 3]
            self.image = pygame.transform.scale(self.image, (32,32))
            self.image = pygame.transform.rotate(self.image, 90*self.direction)
        else:
            self.image = self.imagerow[0]
            self.image = pygame.transform.scale(self.image, (32,32))
            self.image = pygame.transform.rotate(self.image, 90*self.direction)
        # check if the player hits a wall
        block_hit_list = pygame.sprite.spritecollide(self, wall_list, False)
        for block in block_hit_list:
            print("hit wall, dead.")
            self.kill()
            return True