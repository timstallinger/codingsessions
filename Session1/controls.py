import pygame
import math
from player import *
from Bullet import *

def controls(event, player, bullet_list, all_sprites_list):
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
    

    return 0