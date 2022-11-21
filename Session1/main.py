from player import *
from Bullet import *
from level_creation import *
from controls import *
from spritehandler import *
import math
import os
from items import *
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
#Instantiate mixer
pygame.mixer.init()

# Load audio file
script_dir = os.path.dirname(__file__)
rel_path = "assets/music/60sec.wav"
abs_file_path = os.path.join(script_dir, rel_path)
pygame.mixer.music.load(abs_file_path)

pygame.mixer.music.play()



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
player = Player(50, 50, "assets/Characters/Player0.png")
all_sprites_list.add(player)



#add all items to a list
items_list = []

#enemy list added
enemy_list = []
for i in range (1):
    enemy = Player(650, 50, "assets/Characters/Undead0.png")
    enemy_list.append(enemy)
    all_sprites_list.add(enemy)

# create list for bullets
bullet_list = []


#level creation file, creates objects arount players
create_objects(wall_list, player, enemy)

cntl = Controls()
# exists so that rewards spawn only once
fight_running = True
# main loop
while cntl.carryOn and not done:
    # --- Main event loop
    cntl.get_input(player,bullet_list,all_sprites_list)

    for bullet in bullet_list:
        # update bullet position
        bullet.updatex()
        for curr_enemy in enemy_list:
        # if bullet collides with enemy, remove bullet and damage enemy
            if pygame.sprite.collide_rect(bullet, curr_enemy):
                if(curr_enemy.alive()):
                    enemy.health -= 10
                    print(enemy.health)
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)
                if curr_enemy.health <= 0:
                    enemy_list.remove(curr_enemy)
                    curr_enemy.kill()

        if len(enemy_list) == 0 and fight_running == True: 
            fight_running = False
            reward = spawn_reward(all_sprites_list)
            items_list.append(reward)
         
    
    # check enemy health
    if enemy.health <= 0:
        enemy.kill()
    
    for item in items_list:
        if pygame.sprite.collide_rect(player, item):
            player.special = item.special
            items_list.remove(item)
            all_sprites_list.remove(item)
        # TODO: Win screen, wait, new level
    
    # if bullet hits wall, kill bullet
    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, wall_list, False)
        for block in block_hit_list:
            # bugfix, sometimes bug "list.remove(x) : x not in list" occurs
            if (bullet in bullet_list):
                bullet_list.remove(bullet)
            all_sprites_list.remove(bullet) 
    
    # if player collides with any wall, kill player
    done = player.update(wall_list)

    screen.fill(WHITE)
    wall_list.draw(screen)
    all_sprites_list.draw(screen)

    pygame.display.flip()
     
    clock.tick(60)

pygame.quit()