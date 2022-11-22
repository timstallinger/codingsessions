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
'''
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

# pygame.mixer.music.play()



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
player = Player(50, 50, "assets/Characters/animated.png", 64,0)
player.imagerow = spritesheet("assets/Characters/animated.png").images_at([(64,0,16,16),(48,0,16,16),(80,0,16,16),(64,16,16,16),(48,16,16,16),(80,16,16,16),(64,32,16,16),(48,32,16,16),(80,32,16,16),(64,48,16,16),(48,48,16,16),(80,48,16,16)], colorkey = None)
all_sprites_list.add(player)



#add all items to a list
items_list = []

#enemy list added
enemy_list = []
for i in range (1):
    enemy = Player(650, 50, "assets/Characters/Undead0.png",0,0)
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
        self.all_sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.attacks = pygame.sprite.Group()

        create_room_for_tilemap(self)

        self.player.imagerow = spritesheet("assets/Characters/animated.png").images_at([(64,0,16,16),(48,0,16,16),(80,0,16,16),(64,16,16,16),(48,16,16,16),(80,16,16,16),(64,32,16,16),(48,32,16,16),(80,32,16,16),(64,48,16,16),(48,48,16,16),(80,48,16,16)], colorkey = None)

        self.playerCntrl = Controls()


        self.all_sprites.add(self.player)

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

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
pygame.quit()