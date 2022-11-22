from player import *
import random
from items import *
from spritehandler import *

class wall_location:
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.walls = [[(200, 100, 50, 800),(400, 0, 50, 400),(400, 450, 50, 200)], [(400, 450, 50, 800),(100, 0, 50, 300),(0,0,0,0)],[(150, 100, 50, 100),(150, 200, 100, 300),(400, 250, 50, 200),(400, 450, 250, 900)]]
        self.walls = self.walls[number]
        
    def build_walls(self, i):
        return self.walls[i]


def create_room():
    # create one wall around the screen
    wall_list = pygame.sprite.Group()
    wall = pygame.sprite.Sprite()
    wall.image = pygame.Surface([700, 10])
    wall.rect = wall.image.get_rect()
    wall.rect.x = 0
    wall.rect.y = 0
    wall_list.add(wall)

    wall = pygame.sprite.Sprite()
    wall.image = pygame.Surface([10, 500])
    wall.rect = wall.image.get_rect()
    wall.rect.x = 0
    wall.rect.y = 0
    wall_list.add(wall)

    wall = pygame.sprite.Sprite()
    wall.image = pygame.Surface([700, 10])
    wall.rect = wall.image.get_rect()
    wall.rect.x = 0
    wall.rect.y = 490
    wall_list.add(wall)

    wall = pygame.sprite.Sprite()
    wall.image = pygame.Surface([10, 500])
    wall.rect = wall.image.get_rect()
    wall.rect.x = 690
    wall.rect.y = 0
    wall_list.add(wall)

    return wall_list

def create_objects(wall_list, player, enemy):
    room_nr = random.randint(0,2)
    wall_list = room(wall_list, room_nr)
    # if wall touches player or enemy, move it

    return 0

def room(wall_list, number):
    #add variable iterator
    wall_loc = wall_location(number)
    
    for i in range (len(wall_loc.walls)):

        wall = pygame.sprite.Sprite()
        loc = wall_loc.build_walls(i)
        wall.image = pygame.Surface([loc[2],loc[3]])
        wall.rect = wall.image.get_rect()
        wall.rect.x = loc[0]
        wall.rect.y = loc[1]
        wall_list.add(wall)

    return(wall_list)

map = [
    "BBBBBBBBBBBBBBBBBBBBBB",
    "B............B.......B",
    "B............B...E...B",
    "B............B.......B",
    "B............B.......B",
    "B...P........B.......B",
    "B............B.......B",
    "B............B.......B",
    "B............B.......B",
    "B.....B......B.......B",
    "B.....B......B...I...B",
    "B.....B......B.......B",
    "B.....B......B.......B",
    "B.....B..............B",
    "B.....B..............B",
    "BBBBBBBBBBBBBBBBBBBBBB",
]

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, sprite, im_x, im_y, scale = 1, block=False):
        if block:
            self._layer = BLOCK_LAYER
            self.groups = game.all_sprites, game.blocks
        else:
            self._layer = GROUND_LAYER
            self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = spritesheet(sprite).image_at((im_x,im_y,16,16))
        self.image = pygame.transform.scale(self.image, (32*scale,32*scale))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

def create_room_for_tilemap(game):
    for row, tiles in enumerate(map):
        for col, tile in enumerate(tiles):
            if tile == "B":
                Block(game, col, row, "assets/Objects/Floor.png",0,0, block=True)
            elif tile == "E":
                Block(game, col, row, "assets/Objects/Floor.png",0,48)
                game.enemies.add(Player(game, col*TILESIZE, row*TILESIZE, "assets/Characters/Undead0.png",0,0, enemy=True))
            elif tile == "I":
                # Item
                Block(game, col, row, "assets/Objects/Floor.png",0,48)
                game.items.add(Item(game, "nuke", col*TILESIZE, row*TILESIZE, "assets/Items/Book.png",0,0))
            elif tile == "P":
                Block(game, col, row, "assets/Objects/Floor.png",0,48)
                game.player = Player(game, col*TILESIZE, row*TILESIZE)
            else:
                Block(game, col, row, "assets/Objects/Floor.png",0,48)