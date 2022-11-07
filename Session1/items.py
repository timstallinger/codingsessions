import random
import pygame

GREEN = ( 0, 255, 0)

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.fill(self.color)

def spawn_reward(all_sprites_list):
    reward = Item(300, 250, GREEN)
    all_sprites_list.add(reward)
