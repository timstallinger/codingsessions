import random
import pygame
from spritehandler import *
from config import *

GREEN = ( 0, 255, 0)

class Item(pygame.sprite.Sprite):
    def __init__(self, game, special, x, y, sprite, im_x, im_y, scale = 1):
        self._layer = BULLET_LAYER
        self.groups = game.all_sprites, game.items
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = spritesheet(sprite).image_at((im_x,im_y,16,16))
        self.image = pygame.transform.scale(self.image, (32*scale,32*scale))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.special = special

    def update(self):
        # if the player hits the item, it will be removed
        if pygame.sprite.collide_rect(self, self.game.player):
            self.kill()
            self.game.player.special = self.special

def spawn_reward():
    reward = Item(300, 250, "assets/Items/Book.png",0,0)
    reward.special = "nuke"    
    return reward
