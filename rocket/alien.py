from typing import Any
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, rf_game):
        super().__init__()
        self.screen = rf_game.screen
        self.settings = rf_game.settings
        self.image = pygame.image.load('images/hutao.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 999
        self.rect.y = 1
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.x -= self.settings.alien_speed
        self.rect.x = self.x
        
