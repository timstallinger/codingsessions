from player import *
from items import *
from spritehandler import *
import random

maps = [
    [
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
        "B..C..B..............B",
        "B.....B..............B",
        "BBBBBBBBBBBBBBBBBBBBBB",
    ],
    [
        "BBBBBBBBBBBBBBBBBBBBBB",
        "B..P.................B",
        "B....................B",
        "BBBBBBBBBBBBBBB...C..B",
        "B....E...............B",
        "B....................B",
        "B.C.....BBBBBBBBBBBBBB",
        "B....................B",
        "B....................B",
        "BBBBBBBBBBBBBBBBBB...B",
        "B...............C....B",
        "B....................B",
        "B..C..BBBBBBBBBBBBBBBB",
        "B....................B",
        "B................E...B",
        "BBBBBBBBBBBBBBBBBBBBBB",
    ],
    [
        "BBBBBBBBBBBBBBBBBBBBBB",
        "BB........EE........BB",
        "B.B................B.B",
        "B..B..............B..B",
        "B...B............B...B",
        "B....B..........B....B",
        "B.....B........B.....B",
        "B..C...B......B...C..B",
        "B.......B....B.......B",
        "B........B..B........B",
        "B.........EE.........B",
        "B....................B",
        "B....................B",
        "B....................B",
        "B..........P.........B",
        "BBBBBBBBBBBBBBBBBBBBBB",
    ],
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
    # chose random map
    map = random.choice(maps)
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
                Item(game, "nuke", col*TILESIZE, row*TILESIZE, "assets/Items/Book.png",0,0)
            elif tile == "C":
                Block(game, col, row, "assets/Objects/Floor.png",0,48)
                Item(game, "chest", col*TILESIZE, row*TILESIZE, "assets/Items/Chest0.png",0,0)
            elif tile == "P":
                Block(game, col, row, "assets/Objects/Floor.png",0,48)
                game.player = Player(game, col*TILESIZE, row*TILESIZE)
            else:
                Block(game, col, row, "assets/Objects/Floor.png",0,48)