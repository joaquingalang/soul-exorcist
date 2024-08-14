import pygame
import sys
from settings import *
from tile import Tile
from player import Player
from weapon import Weapon

class Game:
    def __init__(self):
        # General Set Up
        pygame.init()
        pygame.display.set_caption('Soul Exorcist')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # Cursor
        pygame.mouse.set_visible(False)
        self.crosshair_surf = pygame.image.load('../graphics/crosshair.png').convert_alpha()
        self.crosshair_surf = pygame.transform.scale_by(self.crosshair_surf, 2)
        self.crosshair_rect = self.crosshair_surf.get_rect(center = (0, 0))
        
        # Initialize Sprite Groups
        self.visible_sprites = YSortCameraGroup()
        self.floor_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Initialize Map
        self.create_map()

        # Create Weapon
        weapon = Weapon(self.player, [self.visible_sprites])

    def create_map(self):
        print('INITIALIZED MAP')
        for x_index, row in enumerate(WORLD_MAP):
            for y_index, col in enumerate(row):
                x_pos = y_index * TILESIZE
                y_pos = x_index * TILESIZE
                pos = (x_pos, y_pos)

                if col == 'X':
                    # Create Boundry Tile
                    Tile(pos, [self.obstacle_sprites], 'boundry')
                elif col == 'C':
                    # Create Column
                    Tile(pos, [self.visible_sprites, self.obstacle_sprites], 'column')
                elif col == 'P':
                    # Create Player
                    self.player = Player(pos, [self.visible_sprites])
                else:
                    print(col)

                # Build Floor For Each Tile
                Tile(pos, [self.floor_sprites], 'floor')

    def crosshair(self):
        mouse_pos = pygame.mouse.get_pos()
        self.crosshair_rect.center = mouse_pos
        self.screen.blit(self.crosshair_surf, self.crosshair_rect)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Fill Screen With Black
            self.screen.fill('black')

            # Draw & Update Sprite Groups
            self.floor_sprites.custom_draw(self.player)
            self.floor_sprites.update()
            self.visible_sprites.custom_draw(self.player)
            self.visible_sprites.update()

            # Update & Draw Crosshair
            self.crosshair()



            # Update Display
            pygame.display.update()
            self.clock.tick(FPS)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # General Setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)


if __name__ == '__main__':
    game = Game()
    game.run()