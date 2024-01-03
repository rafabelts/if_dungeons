import pygame
import textwrap
import random
from components.tiles import (conjunction_tile, exclusive_conjunction_tile, disjunction_tile, exclusive_disjunction_tile, negation_tile, implies_tile, biconditional_tile)
from components.tiles import (assigned_tile, get_conector)
from components.character import character
from components.prepositions import (list_of_prepositions, get_answer)
from components.wrapper import renderTextCenteredAt
from components.menus import Game_Over_Menu
from components.menu_items import Arrow

background_image_path = "../assets/Background.png"
front_hill_image_path = "../assets/Front_Hill.png"
back_hill_image_path = "../assets/Back_Hill.png"
arrow_image_path = "../assets/Arrow.png"

tiles_available = [conjunction_tile, exclusive_conjunction_tile, disjunction_tile, exclusive_disjunction_tile, negation_tile, implies_tile, biconditional_tile]


def screen_render(): 
    pygame.init()
    width = 320  # 256
    height = 448  # 352
    screen = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont("Arial", 20)
    score = 0
    random_preposition = random.choice(list_of_prepositions)
    answer = get_answer(random_preposition)
    conector = "[ ]"

    # Load background image
    bg_image = pygame.image.load(background_image_path)
    front_hill_image = pygame.image.load(front_hill_image_path)
    back_hill_image = pygame.image.load(back_hill_image_path)
    arrow_image = pygame.image.load(arrow_image_path)

    arrow = Arrow(arrow_image, 199)

    # Create a list of sprites
    sprites = pygame.sprite.Group()
    character_sprite = pygame.sprite.Group()
    game_over_sprite_list = pygame.sprite.Group()

    first_tile = assigned_tile(answer)
    print(assigned_tile(answer))

    while True:
        second_tile = random.choice(tiles_available)
        first_tile_x_coordenate = first_tile.get_coordinates()[0]
        second_tile_x_coordenate = second_tile.get_coordinates()[0]

        if first_tile_x_coordenate == second_tile_x_coordenate:
            if first_tile_x_coordenate == 127:
                second_tile.change_coordinates(165, 194)
            else:
                second_tile.change_coordinates(127, 175)
        if second_tile != first_tile:
            break

    first_tile_value = first_tile.get_logic_value()
    second_tile_value = second_tile.get_logic_value()

    sprites.add(first_tile)
    sprites.add(second_tile)
    character_sprite.add(character)
    game_over_sprite_list.add(arrow)

    game_over_menu = Game_Over_Menu(screen, arrow, game_over_sprite_list)
    running = True
    game_over = False

    clock = pygame.time.Clock()
    counter = 2
    counter_running = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if first_tile.rect.collidepoint(event.pos):
                        character.move_to_tile(first_tile.get_coordinates()[0], first_tile.get_coordinates()[1])
                        if first_tile_value == answer and not counter_running:
                            score += 1
                            conector = get_conector(answer)
                            character.move_to_hill()
                            counter_running = True
                        else:
                            game_over = True
                    elif second_tile.rect.collidepoint(event.pos):
                        if second_tile_value == answer and not counter_running:
                            score += 1
                            conector = get_conector(answer)
                            character.move_to_hill()
                            counter_running = True
                        else:
                            game_over = True
            else:
                game_over_menu.Menu_Logic(event, running)

        if not game_over:
            score_text = f"Puntaje: {score}"
            color = (255, 255, 255)

            if counter_running:
                counter -= 1
                if counter == 0:
                    counter_running = False
                    character.reset_position()
                    random_preposition = random.choice(list_of_prepositions)
                    answer = get_answer(random_preposition)
                    print("Fin")
                    sprites.empty()

                    random_preposition = random.choice(list_of_prepositions)
                    answer = get_answer(random_preposition)
                    conector = "[ ]"

                    first_tile = assigned_tile(answer)
                    print(assigned_tile(answer))

                    while True:
                        second_tile = random.choice(tiles_available)
                        first_tile_x_coordenate = first_tile.get_coordinates()[0]
                        second_tile_x_coordenate = second_tile.get_coordinates()[0]

                        if first_tile_x_coordenate == second_tile_x_coordenate:
                            if first_tile_x_coordenate == 127:
                                second_tile.change_coordinates(165, 194)
                            else:
                                second_tile.change_coordinates(127, 175)
                            if second_tile != first_tile:
                                break

                    first_tile_value = first_tile.get_logic_value()
                    second_tile_value = second_tile.get_logic_value()

                    sprites.add(first_tile)
                    sprites.add(second_tile)
                    counter = 2

                    continue
                    

            show_score = font.render(score_text, True, color)
            screen.blit(bg_image, (0, 0))
            screen.blit(front_hill_image, (32, 190))
            screen.blit(back_hill_image, (162, 146))
            screen.blit(show_score, (10, 420))
            renderTextCenteredAt(f"p {conector} q", font, color, 160, 70, screen, 320)
            renderTextCenteredAt(random_preposition, font, color, 160, 0, screen, 320)
            sprites.update()
            character_sprite.update()

            sprites.draw(screen)
            character_sprite.draw(screen)
            
            pygame.display.flip()
            clock.tick(1)
        else:
            game_over_menu.Show_Game_Over_Menu()
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    screen_render()
