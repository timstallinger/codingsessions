from player import *

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
    for i in range(30):
        wall = pygame.sprite.Sprite()
        wall.image = pygame.Surface([random.randint(0,100), random.randint(0,100)])
        wall.rect = wall.image.get_rect()
        wall.rect.x = random.randrange(0, 700)
        wall.rect.y = random.randrange(0, 500)
        # if wall touches player or enemy, move it
        while pygame.sprite.collide_rect(wall, player) or pygame.sprite.collide_rect(wall, enemy):
            wall.rect.x = random.randrange(0, 700)
            wall.rect.y = random.randrange(0, 500)
        wall_list.add(wall)

    return 0