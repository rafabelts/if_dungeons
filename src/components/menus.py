import pygame
import os
import sys
from components.menu_items import (Arrow, Exit_Button)

current_dir = os.path.dirname(os.path.abspath(__file__))
arrow_image_path = os.path.join(current_dir, "../../assets/Arrow.png")
exit_image_path = os.path.join(current_dir, "../../assets/Exit.png")
game_over_image_path = os.path.join(current_dir, "../../assets/Game_Over.png")

arrow_image = pygame.image.load(arrow_image_path)
exit_image = pygame.image.load(exit_image_path)
game_over_image = pygame.image.load(game_over_image_path)

class Game_Over_Menu():
    def __init__(self, screen, arrow, sprites, game_over):
        self.exit_button = Exit_Button(exit_image)
        self.screen = screen
        self.sprites = sprites
        self.arrow = arrow
        self.game_over = game_over

    def Show_Game_Over_Menu(self):
        self.buttons_sprite = pygame.sprite.Group()
        self.screen.blit(game_over_image, (70, 150))
        self.buttons_sprite.add(self.exit_button)
        self.buttons_sprite.update()
        self.buttons_sprite.draw(self.screen)
        self.sprites.update()
        self.sprites.draw(self.screen)

    def Menu_Logic(self, event):
        if self.exit_button.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                sys.exit()

