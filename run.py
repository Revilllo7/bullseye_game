import pygame
import sys

res = (1280, 720)
screen = pygame.display.set_mode(res)

while True:
    # Handle events – close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    pygame.draw.rect(screen, (0, 200, 150), pygame.Rect(10, 50, 200, 100))
    pygame.display.flip()