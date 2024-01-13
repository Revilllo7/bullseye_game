from player import *
import sys


pygame.init()

# Set up the screen
res = (1280, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Bullseye_game")

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

    # Get the keys that are currently being pressed
    keys = pygame.key.get_pressed()

    # Move and draw the player
    player.move(keys)
    screen.fill((255, 255, 255))
    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
