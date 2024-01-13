from player import *
import sys


pygame.init()

# Set up the screen
res = (1280, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Bullseye_game")

ground_color = (0, 255, 0)
def draw_ground():
    pygame.draw.line(screen, ground_color, (0, 100), (1280, 100))

# Initialize the player
player = Player(res[0], res[1])

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill((255, 255, 255))
    player.draw(screen)

    if keys[pygame.K_q]:
        player.shoot(screen)

    pygame.display.flip()
    clock.tick(60)
