import sys
from time import sleep
import pygame

def check_keydown_events(event, ai_settings, screen, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = True

    elif event.key == pygame.K_LEFT:
        player.moving_left = True

    elif event.key == pygame.K_SPACE:
        player.moving_top = True

    elif event.key == pygame.K_q:
        pygame.quit()
        exit()
    

def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False

    elif event.key == pygame.K_LEFT:
        player.moving_left = False


def check_events(ai_settings, screen, stats, player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, aisettings, screen, player)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats,play_button, player, mouse_x, mouse_y)



def update_screen(ai_settings, screen, stats, player):
    screen.fill(ai_settings.bg_color)


    pygame.display.flip()



def player_hit(ai_settings, screen, stats, player):
    pass


def check_play_button(ai_settings, screen, stats, play_button, player, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reste_stats()
        stats.game_active = True
        







































