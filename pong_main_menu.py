import pygame
from pygame.locals import *
import subprocess
import sys
import os

pygame.init()

window_width = 900
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Fab's Pong Game - Main Menu")


script_dir = os.path.dirname(__file__)

font = pygame.font.Font(os.path.join(script_dir, 'pongfont.otf'), 40)


###bg = pygame.image.load('C:/Users/UPraktikant/Desktop/pongygame/pong_game-main/Samurai-Wallpaper.png')


white = (255, 255, 255)
black = (0, 0, 0)

font_color = white

def main_menu():
    while True:
        window.fill(black)

        ###window.blit(pygame.transform.scale(bg, (window_width, window_height)), (0,0))

        title_text = font.render("Fabs' Pong_game", True, font_color)
        window.blit(title_text, (window_width / 2 - title_text.get_width() / 2, 50))

        single_player_text = font.render("Press 1 for Single Player", True, font_color)
        window.blit(single_player_text, (window_width / 2 - single_player_text.get_width() / 2, 200))

        local_multiplayer_text = font.render("2 for Multiplayer", True, font_color)
        window.blit(local_multiplayer_text, (window_width / 2 - local_multiplayer_text.get_width() / 2, 300))

        multiplayer_text = font.render("Or 3 for Beta-Multiplayer", True, font_color)
        window.blit(multiplayer_text, (window_width / 2 - multiplayer_text.get_width() / 2, 400))

        

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_1:
                    print('starting singleplayer')
                    subprocess.call([sys.executable, os.path.join(script_dir, 'pong_singleplayer.py')])
                elif event.key == pygame.K_2:
                    print('starting local multiplayer')
                    subprocess.call([sys.executable, os.path.join(script_dir, 'pong_local_multiplayer.py')])
                elif event.key == pygame.K_3:
                    print('starting multiplayer')
                    subprocess.call([sys.executable, os.path.join(script_dir, 'pong_multiplayer.py')])


main_menu()