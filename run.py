import pygame
from player import Player
import sys

pygame.init()

res = (1280, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Bullseye_game")

player = Player(screen)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill((255, 255, 255))
    player.draw()
    player.shoot_arrow()

    pygame.display.flip()
    clock.tick(60)