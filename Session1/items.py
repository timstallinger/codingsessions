import random
import pygame
from spritehandler import *

GREEN = ( 0, 255, 0)

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = spritesheet("assets/Items/Book.png").image_at((0,0,16,16))
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.special = "blank"

def spawn_reward():
    reward = Item(300, 250, GREEN)
    reward.special = "nuke"
    print(reward.special)
    
    return reward
