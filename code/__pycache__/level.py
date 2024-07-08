import pygame
from settings import *

class Level:
    def __init__(self):
        self.visibile_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        self.visibile_sprites.draw()
        self.visibile_sprites.update()