import pygame
import math
import random

BLACK = ( 0, 0, 0)
#weapons class for player to use

class weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, name,ammo,damage,range,rate_of_fire,accuracy):
        super().__init__()
        self.image = pygame.Surface([10, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.ammo = ammo
        self.damage = damage
        self.range = range
        self.rate_of_fire = rate_of_fire
        self.accuracy = accuracy


    def spawn_weapon(all_sprites_list):
    
        weapon= (100,150 , BLACK, 6, 12, 15,1,1, 0.9)
        all_sprites_list.add(weapon)
        print("hola")
        return weapon
        
    def update(self):
        pass

    def pickup_n_drop(self):
        pass

    
    def reload(self):
        pass

    def get_ammo(self):
        return self.ammo

    def get_hitbox(self):
        return self.hitbox

    #TODO: add shot parameters and link up with bullet class to pass projectiles