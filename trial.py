import pygame
import random

Width, Height = 1280, 720
Ball_count = 10

Colors = [255, 255, 255]

screen = pygame.display.set_mode(Width, Height)
pygame.display.set_caption("Bouncing Balls")

class Ball:
  def __init__(self):
    self.radius = random.randint(20, 50)