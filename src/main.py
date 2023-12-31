import pygame
from components.tiles import (conjunction_tile, exclusive_conjunction_tile, disjunction_tile, exclusive_disjunction_tile, negation_tile, implies_tile, biconditional_tile)

background_image_path = "../assets/Background.png"
front_hill_image_path = "../assets/Front_Hill.png"
back_hill_image_path = "../assets/Back_Hill.png"


def screen_render():
    width = 320  # 256
    height = 448  # 352
    screen = pygame.display.set_mode((width, height))

    # Load background image
    bg_image = pygame.image.load(background_image_path)
    front_hill_image = pygame.image.load(front_hill_image_path)
    back_hill_image = pygame.image.load(back_hill_image_path)

    # Create a list of sprites
    tiles = pygame.sprite.Group()
    tiles.add(conjunction_tile)
    tiles.add(exclusive_conjunction_tile)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg_image, (0, 0))
        screen.blit(front_hill_image, (32, 190))
        screen.blit(back_hill_image, (162, 146))

        tiles.update()
        tiles.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    screen_render()
