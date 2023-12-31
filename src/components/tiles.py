import pygame
import os

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, logic_value, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.logic_value = logic_value
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


current_dir = os.path.dirname(os.path.abspath(__file__))

# Absolute routes
conjunction_image_path = os.path.join(current_dir, "../../assets/Conjunction_Tile.png")
exclusive_conjunction_image_path = os.path.join(current_dir, "../../assets/Exclusive_Conjunction_Tile.png")
disjunction_image_path = os.path.join(current_dir, "../../assets/Disjunction_Tile.png")
exlusive_disjunction_image_path = os.path.join(current_dir, "../../assets/Exclusive_Disjunction_Tile.png")
negation_image = os.path.join(current_dir, "../../assets/Negation_Tile.png")
implies_image = os.path.join(current_dir, "../../assets/Implies_Tile.png")
biconditional_image = os.path.join(current_dir, "../../assets/Biconditional_Tile.png")

conjunction_image = pygame.image.load(conjunction_image_path)
exclusive_conjunction_image = pygame.image.load(exclusive_conjunction_image_path)
disjunction_image = pygame.image.load(disjunction_image_path)
exclusive_disjunction_image = pygame.image.load(exlusive_disjunction_image_path)
negation_image = pygame.image.load(negation_image)
implies_image = pygame.image.load(implies_image)
biconditional_image = pygame.image.load(biconditional_image)

# Assign values to tiles
conjunction_tile = Tile(conjunction_image, "and", 127, 246)
exclusive_conjunction_tile = Tile(exclusive_conjunction_image, "not and", 127, 246)
disjunction_tile = Tile(disjunction_image, "or", 127, 246)
exclusive_disjunction_tile = Tile(exclusive_disjunction_image, "not or", 127, 246)
negation_tile = Tile(negation_image, "not", 127, 246)
implies_tile = Tile(implies_image, "implies", 127, 246)
biconditional_tile = Tile(biconditional_image, "biconditional", 127, 246)
