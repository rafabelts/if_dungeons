import pygame
import os
import random


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, logic_value):
        pygame.sprite.Sprite.__init__(self)
        x_coordinates = [127, 165]
        y_coordinates = [175, 194]
        x_position = random.choice(x_coordinates)
        self.image = image
        self.rect = self.image.get_rect()
        self.logic_value = logic_value
        self.rect.x = x_position

        if x_position == 127:
            self.rect.y = y_coordinates[0]
        else:
            self.rect.y = y_coordinates[1]

    def get_coordinates(self):
        return [self.rect.x, self.rect.y]

    def change_coordinates(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_logic_value(self):
        return self.logic_value


# Obtengo la ruta del directorio
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
conjunction_tile = Tile(conjunction_image, "and")
exclusive_conjunction_tile = Tile(exclusive_conjunction_image, "exlusive conjunction")
disjunction_tile = Tile(disjunction_image, "or")
exclusive_disjunction_tile = Tile(exclusive_disjunction_image, "exclusive disjunction")
negation_tile = Tile(negation_image, "not")
implies_tile = Tile(implies_image, "implies")
biconditional_tile = Tile(biconditional_image, "biconditional")


def assigned_tile(answer):
    if answer == "and":
        return conjunction_tile
    elif answer == "exclusive conjunction":
        return exclusive_conjunction_tile
    elif answer == "or":
        return disjunction_tile
    elif answer == "exclusive disjunction":
        return exclusive_disjunction_tile
    elif answer == "not":
        return negation_tile
    elif answer == "implies":
        return implies_tile
    else:
        return biconditional_tile

def get_conector(answer):
    if answer == "and":
        return "^"
    elif answer == "exclusive conjunctio":
        return "_^_"
    elif answer == "or":
        return "v"
    elif answer == "exclusive disjunction":
        return "_v_"
    elif answer == "not":
        return "¬"
    elif answer == "implies":
        return "->"
    else:
        return "<->"

