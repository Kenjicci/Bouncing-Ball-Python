import pygame
import random

WIDTH, HEIGHT = 1280, 720
ball_qty = 10

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

class Ball:
  def __init__(self):
    self.radius = random.randint(20, 50)
    self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    self.x = random.randint(self.radius, WIDTH - self.radius *2)
    self.y = random.randint(self.radius, HEIGHT - self.radius*2)
    self.dx = random.choice([-1, 1]) * random.uniform(1, 4)
    self.dy = random.choice([-1, 1]) * random.uniform(1, 4)


  def move(self):
    self.x += self.dx
    self.y += self.dy

    if self.x <= self.radius or self.x >= WIDTH - self.radius:
      self.dx *= (-1)
    if self.y <= self.radius or self.y >= HEIGHT - self.radius:
      self.dy *= (-1)

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

balls = [Ball() for i in range(ball_qty)]

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


