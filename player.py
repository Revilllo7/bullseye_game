import pygame
import math
class Player:
    def __init__(self, screen_width, screen_height, size=101, player_sprite="assets/Player_Sprite.png"):
        self.size = size
        self.image = pygame.image.load(player_sprite)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect.center = (screen_width // 2, screen_height // 2)

        self.jump_height = 10  # Adjust the jump height as needed
        self.velocity_y = 0
        self.gravity = 1
        self.is_jumping = False


        self.direction = 1
        self.flip = False

        self.shooting = False
        self.shoot_indicator_color = (255, 0, 0)  # Red color for the indicator




    def move(self, keys):
        speed = 5

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if not self.is_jumping:
                self.is_jumping = True
                self.velocity_y = self.jump_height  # Set initial jump velocity

        if self.is_jumping:
            self.velocity_y -= self.gravity  # Apply gravity
            self.rect.y -= self.velocity_y  # Update vertical position

            if self.rect.y >= self.screen_height - self.size:
                self.rect.y = self.screen_height - self.size
                self.is_jumping = False
                self.velocity_y = 0  # Reset velocity when on the ground

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += speed if self.rect.y < self.screen_height - self.size else 0  # Move down
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.flip = True
            self.direction = -1
            self.rect.x -= speed if self.rect.x > 0 else 0  # Move left
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.flip = False
            self.direction = 1
            self.rect.x += speed if self.rect.x < self.screen_width - self.size else 0  # Move right


    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def shoot(self, screen):
        self.shooting = True
        indicator_radius = 100
        angle = 45

        while self.shooting:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP and event.key == pygame.K_q:
                    self.shooting = False

            pygame.draw.circle(screen, self.shoot_indicator_color, self.rect.center, indicator_radius, 2)

            ball_x = self.rect.center[0] + indicator_radius * math.cos(math.radians(angle))
            ball_y = self.rect.center[1] + indicator_radius * math.sin(math.radians(angle))
            ball_rect = pygame.Rect(ball_x - 10, ball_y - 10, 20, 20)  # Adjust size as needed
            pygame.draw.circle(screen, (0, 0, 255), ball_rect.center, ball_rect.width // 2)

            pygame.display.flip()
            screen.fill((255, 255, 255))

            angle += 5  # Adjust the angle change for the curve
            pygame.time.delay(50)  # Adjust the delay for the curve smoothness