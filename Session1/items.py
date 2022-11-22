import random
import pygame
from spritehandler import *
from config import *

class Item(pygame.sprite.Sprite):
    def __init__(self, game, special, x, y, sprite, imx, imy, scale = 1):
        self._layer = ITEM_LAYER
        self.groups = game.all_sprites, game.items
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = spritesheet(sprite).image_at((imx,imy,16,16))
        self.image = pygame.transform.scale(self.image, (32*scale,32*scale))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.special = special

        self.imx = imx
        self.imy = imy

    def update(self):
        # if the player hits the item, it will be removed
        if pygame.sprite.collide_rect(self, self.game.player):
            if self.special == "health":
                self.game.player.health += 10
                if self.game.player.health > 50:
                    self.game.player.health = 50
                self.kill()
                return
            elif self.special == "chest":
                self.image= spritesheet("assets/Items/Chest1.png").image_at((self.imx,self.imy,16,16))
                self.image = pygame.transform.scale(self.image, (32,32))
                self.special = "chestopen"
                Item(self.game, "health", self.rect.x+10, self.rect.y+10, "assets/Items/Potion.png", 0, 0)
                return
            elif self.special == "chestopen":
                return
            else:
                self.game.player.special = self.special
                self.kill()
                return