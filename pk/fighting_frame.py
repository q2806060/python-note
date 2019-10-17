import sys
import pygame
from pygame.locals import *
from sys import exit
from player import Player
from setting import Settings 
import player_functions as pf 
# from button import Button 
# from game_stats import GameStats 


def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Emoticon fighting")

    player = Player(ai_settings, screen)
    player.blitme()

    # stats = GameStats(ai_settings)

    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        x, y = pygame.mouse.get_pos()

        pygame.display.update()

if __name__ == "__main__":
    run_game()
























