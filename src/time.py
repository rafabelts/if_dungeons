import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Timer con Pygame")

# Configuración del timer
font = pygame.font.Font(None, 36)
timer_value = 10
timer_running = False

# Función para mostrar el tiempo en la pantalla
def display_timer():
    timer_text = font.render(f"Tiempo: {timer_value} segundos", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not timer_running:
            # Inicia el timer cuando el usuario hace clic con el mouse
            timer_running = True

    # Actualiza el timer si está corriendo
    if timer_running:
        timer_value -= 1
        if timer_value == 0:
            timer_running = False
            

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Mostrar el tiempo en la pantalla
    display_timer()

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad del bucle
    pygame.time.Clock().tick(1)  # 1 FPS para que el contador aumente cada 
