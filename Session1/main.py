import pygame
import math
import random


# player controls a cube that he can move up and down with the arrow keys
# the cube can also shoot bullets
# the goal is to shoot the enemy cube
# the enemy cube moves up and down and shoots bullets
# the player and enemy cubes have health bars

pygame.init()
pygame.display.list_modes()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)


class Player(pygame.sprite.Sprite):
    # this class represents the player
    def __init__(self, x, y, color, ):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.health = 50


    def update(self):
        # move up and down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # check if the player hits a wall
        block_hit_list = pygame.sprite.spritecollide(self, wall_list, False)
        for block in block_hit_list:
            if self.speed > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

# class Bullet
# this class represents the bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
        # direction is tuple (x, y)
        self.direction = direction
    


    def updatex(self):
        # update position according to direction and speed
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

# Loop until the user clicks the close button.
done = False
carryOn = True
clock = pygame.time.Clock()

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


# create map with random walls
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


hold_right = False
hold_left = False
hold_up = False
hold_down = False


# make enemy an online player
# enemy moves up and down
# enemy shoots bullets



while carryOn and not done:
    # --- Main event loop
    for event in pygame.event.get():
        # if player pushes button
        if event.type == pygame.KEYDOWN:
            # if player pushes up
            if event.key == pygame.K_UP:
                hold_up = True
            # if player pushes down
            if event.key == pygame.K_DOWN:
                hold_down = True
            # if player pushes space
            if event.key == pygame.K_SPACE:
                # create 4 bullets in all directions
                bullet = Bullet(player.rect.x, player.rect.y, (1, 0))
                bullet_list.append(bullet)
                all_sprites_list.add(bullet)
                bullet = Bullet(player.rect.x, player.rect.y, (-1, 0))
                bullet_list.append(bullet)
                all_sprites_list.add(bullet)
                bullet = Bullet(player.rect.x, player.rect.y, (0, 1))
                bullet_list.append(bullet)
                all_sprites_list.add(bullet)
                bullet = Bullet(player.rect.x, player.rect.y, (0, -1))
                bullet_list.append(bullet)
                all_sprites_list.add(bullet)
                
            # if player presses right arrow move player right
            if event.key == pygame.K_RIGHT:
                hold_right = True
            # if player presses left arrow move player left
            if event.key == pygame.K_LEFT:
                hold_left = True
        # if player clicks left mouse, create bullet in according direction
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                hold_right = False
            if event.key == pygame.K_LEFT:
                hold_left = False
            if event.key == pygame.K_UP:
                hold_up = False
            if event.key == pygame.K_DOWN:
                hold_down = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position
            pos = pygame.mouse.get_pos()
            # calculate direction vector with mouse position
            mouse_x = pos[0]
            mouse_y = pos[1]
            rel_x = mouse_x - player.rect.x
            rel_y = mouse_y - player.rect.y
            # calculate the length of the vector
            length = math.hypot(rel_x, rel_y)
            # normalize the vector
            rel_x /= length
            rel_y /= length

            direction = (rel_x, rel_y)

            # create bullet
            bullet = Bullet(player.rect.x, player.rect.y, direction)
            bullet_list.append(bullet)
            all_sprites_list.add(bullet)
            
        
        if event.type == pygame.QUIT:
            carryOn = False
    if hold_right:
        player.rect.x += 3
    if hold_left:
        player.rect.x -= 3
    if hold_up:
        player.rect.y -= 3
    if hold_down:
        player.rect.y += 3

    for bullet in bullet_list:
        # update bullet position
        bullet.updatex()
        # if bullet collides with enemy, remove bullet and damage enemy
        if pygame.sprite.collide_rect(bullet, enemy):
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            enemy.health -= 10
            print(enemy.health)
            if enemy.health <= 0:
                enemy.kill()


    # check enemy health
    if enemy.health <= 0:
        enemy.kill()
    # if player collides with any wall, kill player
    block_hit_list = pygame.sprite.spritecollide(player, wall_list, False)
    for block in block_hit_list:
        player.kill()
        done = True
    
    # if bullet hits wall, kill bullet
    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, wall_list, False)
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet) 
    
    
    screen.fill(WHITE)
    wall_list.draw(screen)
    all_sprites_list.draw(screen)

    pygame.display.flip()
     
    clock.tick(60)

pygame.quit()