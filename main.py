import pygame

pygame.init()

window = pygame.display.set_mode(size=(720, 480))

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close Window
            quit()  # End Pygame
