from player import *
from Bullet import *
from level_creation import *
from controls import *
from spritehandler import *
import math
import os
from items import *
import pygame
from config import *


# TODO: add a health bar for the player
# TODO: add a health bar for the enemy
# TODO: main menu
# TODO: Items
# TODO: Music
# TODO: Enemies movement
# TODO: Buffs and debuffs 
# TODO: Bullet class
# TODO: Sprites
'''

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
                    enemy.health -= bullet.damage
                    print(enemy.health)
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)
                if curr_enemy.health <= 0:
                    enemy_list.remove(curr_enemy)
                    curr_enemy.image = pygame.transform.rotate(curr_enemy.image, 90)

        if len(enemy_list) == 0 and fight_running == True: 
            fight_running = False
            reward = spawn_reward()
            all_sprites_list.add(reward)
            items_list.append(reward)

    
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
'''

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.items = pygame.sprite.LayeredUpdates()

        create_room_for_tilemap(self)

        self.player.imagerow = spritesheet("assets/Characters/animated.png").images_at([(64,0,16,16),(48,0,16,16),(80,0,16,16),(64,16,16,16),(48,16,16,16),(80,16,16,16),(64,32,16,16),(48,32,16,16),(80,32,16,16),(64,48,16,16),(48,48,16,16),(80,48,16,16)], colorkey = None)

        self.playerCntrl = Controls()

    def events(self):
        self.playerCntrl.get_input(self)

    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.flip()
    
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    
    def game_over(self):
        print("Game Over")

    def intro_screen(self):
        pass

    def play_sound(self, sound):
        # Load audio file
        script_dir = os.path.dirname(__file__)
        rel_path = "assets/music/"+sound+".wav"
        abs_file_path = os.path.join(script_dir, rel_path)
        pygame.mixer.music.load(abs_file_path)

        pygame.mixer.music.play()


pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Pew Pew")

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
pygame.quit()