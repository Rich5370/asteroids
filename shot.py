import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,0)

    def update(self, dt):
        # Move the shot based on its velocity and time elapsed
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def draw(self, screen):
        # Draw the shot as a small white circle
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)
