import pygame
from Bullet import *
import math

class Controls:
    hold_right = False
    hold_left = False
    hold_up = False
    hold_down = False

    def get_input(self, game):
        for event in pygame.event.get():
            # if player pushes button
            if event.type == pygame.KEYDOWN:
                # if player pushes up
                if event.key == pygame.K_UP:
                    self.hold_up = True
                # if player pushes down
                if event.key == pygame.K_DOWN:
                    self.hold_down = True
                # if player presses right arrow move player right
                if event.key == pygame.K_RIGHT:
                    self.hold_right = True
                # if player presses left arrow move player left
                if event.key == pygame.K_LEFT:
                    self.hold_left = True
                # if player pushes space
                if event.key == pygame.K_SPACE:
                    # create bullet in direction player is facing
                    if game.player.direction == 0:
                        #runter
                        bullet = Bullet(game.player.rect.x, game.player.rect.y, (0, 1), game.player.special)
                    elif game.player.direction == 2:
                        #rechts
                        bullet = Bullet(game.player.rect.x, game.player.rect.y, (1, 0), game.player.special)
                    elif game.player.direction == 3:
                        #hoch
                        bullet = Bullet(game.player.rect.x, game.player.rect.y, (0, -1), game.player.special)
                    elif game.player.direction == 1:
                        #links
                        bullet = Bullet(game.player.rect.x, game.player.rect.y, (-1, 0), game.player.special)
                    game.attacks.add(bullet)
                    game.all_sprites.add(bullet)
                    
                
            # if game.player clicks left mouse, create bullet in according direction
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.hold_right = False
                if event.key == pygame.K_LEFT:
                    self.hold_left = False
                if event.key == pygame.K_UP:
                    self.hold_up = False
                if event.key == pygame.K_DOWN:
                    self.hold_down = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                pos = pygame.mouse.get_pos()
                # calculate direction vector with mouse position
                mouse_x = pos[0]
                mouse_y = pos[1]
                rel_x = mouse_x - game.player.rect.x
                rel_y = mouse_y - game.player.rect.y
                # calculate the length of the vector
                length = math.hypot(rel_x, rel_y)
                # normalize the vector
                rel_x /= length
                rel_y /= length

                direction = (rel_x, rel_y)

                # create bullet
                bullet = Bullet(game.player.rect.x, game.player.rect.y, direction, game.player.special)
                game.attacks.add(bullet)
                game.all_sprites.add(bullet)
                
            
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
        
        if self.hold_right:
            game.player.rect.x += 3
            game.player.moving=True
            game.player.direction = 2
        if self.hold_left:
            game.player.rect.x -= 3
            game.player.moving=True
            game.player.direction = 1
        if self.hold_up:
            game.player.rect.y -= 3
            game.player.moving=True
            game.player.direction = 3
        if self.hold_down:
            game.player.rect.y += 3
            game.player.moving=True
            game.player.direction = 0
        if not self.hold_right and not self.hold_left and not self.hold_up and not self.hold_down:
            game.player.moving=False