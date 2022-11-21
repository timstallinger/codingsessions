import random
import pygame
from spritehandler import *

GREEN = ( 0, 255, 0)

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite, im_x, im_y, scale = 1):
        super().__init__()
        self.image = spritesheet(sprite).image_at((im_x,im_y,16,16))
        self.image = pygame.transform.scale(self.image, (32*scale,32*scale))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.special = None

def spawn_reward():
    reward = Item(300, 250, "assets/Items/Book.png",0,0)
    reward.special = "nuke"    
    return reward
