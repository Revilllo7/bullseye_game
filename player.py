import pygame
class Player:
    def __init__(self, screen_width, screen_height, size=100, player_sprite="assets/Player_sprite.png"):
        self.size = size
        self.image = pygame.image.load(player_sprite)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect.center = (screen_width // 2, screen_height // 2)

    def move(self, keys):
        speed = 5
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= speed if self.rect.y > 0 else 0  # Move up
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += speed if self.rect.y < self.screen_height - self.size else 0  # Move down
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= speed if self.rect.x > 0 else 0  # Move left
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += speed if self.rect.x < self.screen_width - self.size else 0  # Move right


    def draw(self, screen):
        screen.blit(self.image, self.rect)