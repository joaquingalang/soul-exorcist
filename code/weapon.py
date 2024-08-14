import pygame
from settings import *
import math

class Weapon(pygame.sprite.Sprite):

    def __init__(self, player, groups):
        super().__init__(groups)

        self.player = player

        self.image = pygame.image.load('../graphics/staff.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 2.5)
        self.rect = self.image.get_rect(center = self.player.rect.center)

    # https://stackoverflow.com/questions/58603835/how-to-rotate-an-imageplayer-to-the-mouse-direction

    # def weapon_direction(self):
    #     mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    #     direction_x, direction_y = mouse_pos_x - self.player.rect.centerx, self.player.rect.centery - mouse_pos_y
    #     angle = math.degrees(math.atan2(-direction_y, direction_x))
    #     print(angle)
    #     self.image = pygame.transform.rotate(self.image, angle)
    #     self.rect = self.image.get_rect(center = self.player.rect.center)

    def update(self):
        self.rect.center = self.player.rect.center
        # self.weapon_direction()
