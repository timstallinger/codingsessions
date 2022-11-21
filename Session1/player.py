import pygame
from spritehandler import *

class Player(pygame.sprite.Sprite):
    # this class represents the player
    def __init__(self, x, y, sprite ):
        super().__init__()
        self.speed = 5
        self.health = 50
        self.sprite = spritesheet(sprite)
        self.image = self.sprite.image_at((0,0,16,16))
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.step = 0
        self.moving=False

    # never called?
    def update(self, wall_list):
        if self.moving:
            self.step += 1
            if self.step == 4:
                self.step = 0
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.step = 0
        # check if the player hits a wall
        block_hit_list = pygame.sprite.spritecollide(self, wall_list, False)
        for block in block_hit_list:
            print("hit wall, dead.")
            self.kill()
            return True