from pygame.sprite import Sprite
import pygame

class Player(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        self.image = pygame.image.load('test.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.left)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.player_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.player_speed_factor

        self.rect.left = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def left_player(self):
        self.center = self.screen_rect.left
    

































