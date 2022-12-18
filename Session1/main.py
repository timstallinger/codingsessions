from player import *
from Bullet import *
from level_creation import *
from controls import *
from spritehandler import *
from mainmenu import *
import math
import os
from items import *
import pygame
from config import *

# TODO: add a health bar for the player
# TODO: add a health bar for the enemy
# TODO: main menu
# TODO: Music
# TODO: Enemies movement
# TODO: Buffs and debuffs

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        self.status = "mainmenu"

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.items = pygame.sprite.LayeredUpdates()
        self.doors = pygame.sprite.LayeredUpdates()

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
    
    def game_over(self):
        print("Game Over")

    def intro_screen(self):
        mainmenu(self)
        menuControls(self)
        self.clock.tick(FPS)
        pygame.display.flip()

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
while g.status == "mainmenu":
    g.intro_screen()
g.new()
pygame.display.update()
print("running")
g.main()
g.game_over()
# pygame.quit()