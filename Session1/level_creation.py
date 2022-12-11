from player import *
from items import *
from spritehandler import *
import random

maps = [
    [
        "BBBBBBBBBBBBBBBBBBBBBB",
        "B............B.DD....B",
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
        "B.................DD.B",
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
        "B..........P......DD.B",
        "BBBBBBBBBBBBBBBBBBBBBB",
    ],
]


skins = [
    [
        "assets/Objects/basictiles.png",
        [(0,128)], # ground
        [(78,144), (64,32)], # obstacles
        [(0,0)] # TODO DOORS
    ],
    [
        "assets/Objects/basictiles.png",
        [(16,128)],
        [(96,64),(96,48)],
        [(0,0)] # TODO DOORS
    ],  
    [
        "assets/Objects/basictiles.png",
        [(16,128)],
        [(64,112)],
        [(0,0)] # TODO DOORS
    ],
    [
        "assets/Objects/basictiles.png",
        [(16,16)],
        [(16,32)],
        [(0,0)] # TODO DOORS
    ],
    [
        "assets/Objects/basictiles.png",
        [(48,16)],
        [(64,16)],
        [(0,0)] # TODO DOORS
    ],
]

dungeons = [
    [
        "assets/Objects/basictiles.png",
        [(96,32)], # black
        [(16,0)], # ground
        [(112,16), (112,32)] # obstacle
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
    skin = random.choice(skins)
    for row, tiles in enumerate(map):
        for col, tile in enumerate(tiles):
            if tile == "B":
                #random choice here necessary? skin is picked already?
                ground = random.choice(skin[1])
                block = random.choice(skin[2])
                Block(game, col, row, skin[0],ground[0],ground[1])
                Block(game, col, row, skin[0],block[0],block[1], block=True)
            elif tile == "E":
                ground = random.choice(skin[1])
                Block(game, col, row, skin[0],ground[0],ground[1])
                game.enemies.add(Player(game, col*TILESIZE, row*TILESIZE, "assets/Characters/Undead0.png",0,0, enemy=True))
            elif tile == "I":
                ground = random.choice(skin[1])
                Block(game, col, row, skin[0],ground[0],ground[1])
                Item(game, "nuke", col*TILESIZE, row*TILESIZE, "assets/Items/Book.png",0,0)
            elif tile == "C":
                ground = random.choice(skin[1])
                Block(game, col, row, skin[0],ground[0],ground[1])
                Item(game, "chest", col*TILESIZE, row*TILESIZE, "assets/Items/Chest0.png",0,0)
            elif tile == "P":                
                ground = random.choice(skin[1])
                Block(game, col, row, skin[0],ground[0],ground[1])
                game.player = Player(game, col*TILESIZE, row*TILESIZE)
            elif tile == "D":
                ground = random.choice(skin[3])
                Block(game, col, row, "assets/Objects/Door0.png", ground[0],ground[1])
            else:
                ground = random.choice(skin[1])
                Block(game, col, row, skin[0],ground[0],ground[1])