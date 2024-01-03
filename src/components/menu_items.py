import pygame
class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 108
        self.rect.y = y
    
    def change_y_position(self, y):
        self.rect.y = y

class Restart_Button(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 118
        self.rect.y = 200

class Exit_Button(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 138
        self.rect.y = 240
