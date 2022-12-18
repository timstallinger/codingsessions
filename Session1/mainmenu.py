from config import *
import pygame


# pygame main menu with startgame options and highscores option
def mainmenu(game):
    game.screen.fill((0, 0, 0))
    # play button
    pygame.draw.rect(game.screen, (255, 255, 255), (WINWIDTH/2-50, WINHEIGHT/2-25, 100, 50))
    # quit button
    pygame.draw.rect(game.screen, (255, 255, 255), (WINWIDTH/2-50, WINHEIGHT/2+25, 100, 50))
    # play text
    game.screen.blit(pygame.font.SysFont("Arial", 20).render("Play", True, (0, 0, 0)), (WINWIDTH/2-20, WINHEIGHT/2-10))
    # quit text
    game.screen.blit(pygame.font.SysFont("Arial", 20).render("Quit", True, (0, 0, 0)), (WINWIDTH/2-20, WINHEIGHT/2+40))

def menuControls(game):
    # if player presses button
    for event in pygame.event.get():
        # if player presses quit button
        if event.type == pygame.QUIT:
            game.running = False
            game.playing = False
            game.status = "quit"
        # if player presses play button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.Rect(WINWIDTH/2-50, WINHEIGHT/2-25, 100, 50).collidepoint(event.pos):
                    game.playing = True
                    game.running = True
                    game.status = "playing"
                if pygame.Rect(WINWIDTH/2-50, WINHEIGHT/2+25, 100, 50).collidepoint(event.pos):
                    pygame.quit()