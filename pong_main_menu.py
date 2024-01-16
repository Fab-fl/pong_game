import pygame
from pygame.locals import *
import subprocess
import sys

pygame.init()

window_width = 900
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Fab's Pong Game - Main Menu")

font = pygame.font.Font('C:/Users/UPraktikant/Desktop/pongygame/pong_game-main/pongfont.otf', 50)

white = (255, 255, 255)
black = (0, 0, 0)

def main_menu():
    while True:
        window.fill(black)

        title_text = font.render("Fabs' Pong_game", True, white)
        window.blit(title_text, (window_width / 2 - title_text.get_width() / 2, 50))

        single_player_text = font.render("Press 1 for Single Player", True, white)
        window.blit(single_player_text, (window_width / 2 - single_player_text.get_width() / 2, 200))

        multiplayer_text = font.render("Or 2 for Multiplayer", True, white)
        window.blit(multiplayer_text, (window_width / 2 - multiplayer_text.get_width() / 2, 300))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_1:
                    print('starting singleplayer')
                    subprocess.call([sys.executable, r"C:\Users\UPraktikant\Desktop\pongygame\pong_game-main\pong_singleplayer.py"])
                elif event.key == pygame.K_2:
                    print('starting multiplayer')
                    subprocess.call([sys.executable, r"C:\Users\UPraktikant\Desktop\pongygame\pong_game-main\pong_local_multiplayer.py"])


main_menu()