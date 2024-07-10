import pygame

class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)

        # if sprite_type == 'box':
        self.image = pygame.image.load('../graphics/test/box.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft = pos)
        
