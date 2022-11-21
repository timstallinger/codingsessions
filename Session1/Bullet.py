import pygame
from spritehandler import *


BLACK = ( 0, 0, 0)
# class Bullet
# this class represents the bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, special,scale = 1):
        super().__init__()
        self.image = spritesheet("assets/Objects/Effect0.png").image_at((96,353,16,16))
        self.image = pygame.transform.scale(self.image, (16*scale,16*scale))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4
        # direction is tuple (x, y)
        self.direction = direction
    


    def updatex(self):
        # update position according to direction and speed
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

