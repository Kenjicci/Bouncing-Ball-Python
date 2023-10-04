import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
BALL_COUNT = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Ball Swapping")

# Function to create random balls
def create_random_balls():
    balls = []
    for _ in range(BALL_COUNT):
        x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
        y = random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS)
        ball = {
            'x': x,
            'y': y,
            'dx': random.randint(-5, 5),
            'dy': random.randint(-5, 5),
            'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        }
        balls.append(ball)
    return balls

# Main game loop
balls = create_random_balls()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball positions
    for ball in balls:
        ball['x'] += ball['dx']
        ball['y'] += ball['dy']

        # Check for collisions with the screen edges
        if ball['x'] - BALL_RADIUS < 0 or ball['x'] + BALL_RADIUS > WIDTH:
            ball['dx'] *= -1
        if ball['y'] - BALL_RADIUS < 0 or ball['y'] + BALL_RADIUS > HEIGHT:
            ball['dy'] *= -1

    # Clear the screen
    screen.fill(WHITE)

    # Draw the balls
    for ball in balls:
        pygame.draw.circle(screen, ball['color'], (ball['x'], ball['y']), BALL_RADIUS)

    pygame.display.flip()

    # Pause for a moment
    pygame.time.delay(1000)

    # Create new random balls for the next run
    balls = create_random_balls()

# Quit Pygame
pygame.quit()