import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (int(self.position.x), int(self.position.y)),  self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # IF the radius is minimum, then just kill
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        
        # Generate a new random angle
        new_rand_angle = random.uniform(20,50)

        # Create two new velocity vectors
        new_velocity1 = self.velocity.rotate(new_rand_angle)
        new_velocity2 = self.velocity.rotate(-new_rand_angle)

        # Calculate new radius
        new_radius =  self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids
        # pass these parameters to the Asteroid constuctor
        new_asteroid1 = Asteroid(
            x=self.position.x,
            y=self.position.y,
            radius=new_radius)
        new_asteroid2 = Asteroid(
            x=self.position.x,
            y=self.position.y,
            radius=new_radius)
        
        # set their velocities (and make them faster)
        new_asteroid1.velocity = new_velocity1 * 1.2
        new_asteroid2.velocity = new_velocity2 * 1.2

        self.kill()
