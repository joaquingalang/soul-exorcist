import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visibile_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for x_index, row in enumerate(WORLD_MAP):
            for y_index, col in enumerate(row):
                x_pos = x_index * TILESIZE
                y_pos = y_index * TILESIZE
                tile_pos = (x_pos, y_pos)
                if col == 'X':
                    Tile(tile_pos, [self.visibile_sprites, self.obstacle_sprites])
                elif col == 'P':
                    Player(tile_pos, [self.visibile_sprites])

    def run(self):
        self.visibile_sprites.draw(self.display_surface)
        self.visibile_sprites.update()