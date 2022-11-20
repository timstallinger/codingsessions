from player import *
import random
class wall_location:
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.walls = [[(200, 100, 50, 800),(400, 0, 50, 400),(400, 450, 50, 200)], [(400, 450, 50, 800),(100, 0, 50, 300),(0,0,0,0)],[(150, 100, 50, 100),(250, 200, 100, 300),(400, 250, 50, 200),(400, 450, 250, 900)]]
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
    wall_list = room(wall_list, 2)
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




