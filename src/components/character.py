import pygame
import os

# Se obtiene ruta del directorio
current_dir = os.path.dirname(os.path.abspath(__file__))
character_image = os.path.join(current_dir, "../../assets/Character.png")


class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(character_image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 170

    def move_to_tile(self, tile_x_position, tile_y_position):
        if tile_x_position == 127 and tile_y_position == 175:
            self.rect.x += 36
            self.rect.y -= 26
        else:
            self.rect.x += 73
            self.rect.y -= 6

    def move_to_hill(self):
        if self.rect.x == 127 + 36:
            self.rect.x += 70
        else:
            self.rect.x += 60
            self.rect.y -= 24

    def reset_position(self):
        self.rect.x = 100
        self.rect.y = 170

character = Character()
