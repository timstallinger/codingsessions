import pygame
from spritehandler import *
from config import *
from items import *
from Bullet import *
import random
import math

class Player(pygame.sprite.Sprite):
    # this class represents the player
    def __init__(self, game, x, y, spritesh = "assets/Characters/animated.png", imx = 64, imy = 0, scale = 1, enemy = False, special = None):
        self.enemy = enemy
        if self.enemy:
            self._layer = ENEMY_LAYER
            self.groups = game.all_sprites, game.enemies
            self.cooldown = 0
        else:
            self._layer = PLAYER_LAYER
            self.groups = game.all_sprites
            self.cooldown = 1*FPS
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.speed = 5
        self.health = 50
        self.sprite = spritesheet(spritesh)
        self.image = self.sprite.image_at((imx,imy,16,16))
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.step = 0
        self.direction = 1
        self.imagerow = [self.image for i in range(4)]
        self.special = special
        self.moving = False
        self.drop = "health"

    def update(self):
        if self.health <= 0 and self.enemy:
            if self in self.game.enemies:
                self.image = pygame.transform.rotate(self.image, 90)
                Item(self.game, self.drop, self.rect.x+10, self.rect.y+10, "assets/Items/Potion.png", 0, 0)
                self.remove(self.game.enemies)
        elif self.moving:
            self.step += 1
            self.image = self.imagerow[self.direction*3 + int(self.step/6) % 3]
            self.image = pygame.transform.scale(self.image, (32,32)) 
        else:
            self.image = self.imagerow[self.direction*3]
            self.image = pygame.transform.scale(self.image, (32,32))
        # check if the player hits a wall
        block_hit_list = pygame.sprite.spritecollide(self, self.game.blocks, False)
        for _ in block_hit_list:
            self.game.playing = False
            return
        # check if the player hits a door
        door_hit_list = pygame.sprite.spritecollide(self, self.game.doors, False)
        for _ in door_hit_list:
            self.game.new()
        
        if self.health <= 0 and self == self.game.player:
            self.game.playing = False
            return
        if self.cooldown > 0:
            self.cooldown -= 1

    def drawHealth(self):
        pygame.draw.rect(self.game.screen, (0,128,0), (self.rect.x-10, self.rect.y - 15, self.health, 5))
    
    def checkcooldown(self):
        if self.cooldown > 0:
            return False
        return True

    def randomShoot(self):
        r = random.randint(0,100)
        if r < 1:
            # calculate the angle between the player and self.game.player
            angle = math.atan2(self.game.player.rect.y - self.rect.y, self.game.player.rect.x - self.rect.x)
            # calculate the direction vector
            dx = math.cos(angle)
            dy = math.sin(angle)
            # create a bullet
            bullet = Bullet(self.game, self.rect.x + 16, self.rect.y + 16, (dx, dy), self.special, hitEnemy=False)
            # add the bullet to the game
    # check if the enemy sees a player
    def checkPlayer(self):
        if self.enemy:
            if self.game.player.rect.x > self.rect.x:
                self.direction = 2
            elif self.game.player.rect.x < self.rect.x:
                self.direction = 1
            if self.game.player.rect.y > self.rect.y:
                self.direction = 0
            elif self.game.player.rect.y < self.rect.y:
                self.direction = 3
            if self.game.player.rect.x > self.rect.x - 100 and self.game.player.rect.x < self.rect.x + 100:
                if self.game.player.rect.y > self.rect.y - 100 and self.game.player.rect.y < self.rect.y + 100:
                    self.moving = False
                    self.randomShoot()
                else:
                    self.moving = True
            else:
                self.moving = True
        else:
            self.moving = False
        if self.moving:
            if self.direction == 0:
                self.rect.y += self.speed
            elif self.direction == 1:
                self.rect.x -= self.speed
            elif self.direction == 2:
                self.rect.x += self.speed
            elif self.direction == 3:
                self.rect.y -= self.speed