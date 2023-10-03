import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720
BALL_COUNT = 10

# Colors
WHITE = (255, 255, 255)

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

# Ball class
class Ball:
    def __init__(self):
        self.radius = random.randint(20, 50)  # Random radius between 20 and 50
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.dx = random.choice([-1, 1]) * random.uniform(1, 4)
        self.dy = random.choice([-1, 1]) * random.uniform(1, 4)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off the walls
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.dx *= -1
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Create a list of balls
balls = [Ball() for _ in range(BALL_COUNT)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for ball in balls:
        ball.move()
        ball.draw(screen)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
