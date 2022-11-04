import pygame
import math
import random


#weapons class for player to use

class weapon(pygame.sprite.Sprite,...,...,...):
    def __init__(self, x, y, color, name,ammo,damage,range,rate_of_fire,accuracy):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.ammo = ammo
        self.damage = damage


    def update(self):
        pass

    def pickup(self):
        pass

    def use(self):
        pass

    def drop(self):
        pass

    def get_name(self):
        return self.name

    def get_hitbox(self):
        return self.hitbox