from player import *
from Bullet import *
from level_creation import *
from controls import *
import math

import pygame


# player controls a cube that he can move up and down with the arrow keys
# the cube can also shoot bullets
# the goal is to shoot the enemy cube
# the enemy cube moves up and down and shoots bullets
# the player and enemy cubes have health bars

# TODO: add a health bar for the player
# TODO: add a health bar for the enemy
# TODO: main menu
# TODO: Items
# TODO: Music
# TODO: Enemies movement
# TODO: Buffs and debuffs 
# TODO: Bullet class
# TODO: Sprites

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)

pygame.init()
pygame.display.list_modes()


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


# creates the room and returns list of main walls
wall_list = create_room()


all_sprites_list = pygame.sprite.Group()

# create the player
player = Player(50, 50, BLUE)
all_sprites_list.add(player)

enemy = Player(650, 50, RED)

# create list for bullets
bullet_list = []

# add all sprites to a list
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
all_sprites_list.add(enemy)


#level creation file, creates objects arount players
create_objects(wall_list, player, enemy)

cntl = Controls()

# main loop
while cntl.carryOn and not done:
    # --- Main event loop
    cntl.get_input(player,bullet_list,all_sprites_list)

    for bullet in bullet_list:
        # update bullet position
        bullet.updatex()
        # if bullet collides with enemy, remove bullet and damage enemy
        if pygame.sprite.collide_rect(bullet, enemy):
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            if(enemy.alive):
                enemy.health -= 10
                print(enemy.health)
            if enemy.health <= 0:
                enemy.kill()


    # check enemy health
    if enemy.health <= 0:
        enemy.kill()
        # TODO: Win screen, wait, new level
    # if player collides with any wall, kill player
    block_hit_list = pygame.sprite.spritecollide(player, wall_list, False)
    for block in block_hit_list:
        player.kill()
        # TODO: Game over label, wait, new level
    
    # if bullet hits wall, kill bullet
    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, wall_list, False)
        for block in block_hit_list:
            # bugfix, sometimes bug "list.remove(x) : x not in list" occurs
            if (bullet in bullet_list):
                bullet_list.remove(bullet)
            all_sprites_list.remove(bullet) 
    
    
    screen.fill(WHITE)
    wall_list.draw(screen)
    all_sprites_list.draw(screen)

    pygame.display.flip()
     
    clock.tick(60)

pygame.quit()