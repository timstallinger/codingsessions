
import pygame
import math

BLACK = ( 0, 0, 0)
# class Bullet
# this class represents the bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
        # direction is tuple (x, y)
        self.direction = direction
    


    def updatex(self):
        # update position according to direction and speed
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed


