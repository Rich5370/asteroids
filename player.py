import pygame
from shot import Shot
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, shots_group):
        if self.shot_timer <= 0:

            # Create a new shot at the player's position
            new_shot = Shot(self.position.x, self.position.y)
        
            # Set the shot's velocity
            # Start with a vector pointing upward
            shot_direction = pygame.Vector2(0, 1)  # Note: in Pygame, y increases downward
        
            # Rotate the vector to match the player's direction
            shot_direction.rotate_ip(self.rotation)
        
            # Scale by the shot speed
            new_shot.velocity = shot_direction * PLAYER_SHOOT_SPEED
        
            # Add the shot to the shots group
            # You'll need to have access to the shots group here
            shots_group.add(new_shot)

            # Activate Shot Cool Down
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
            
    def update(self, dt):
        # Decrease Shot timer by `dt` each time update is called
        self.shot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) # Rotate left - 'a'
        if keys[pygame.K_d]:
            self.rotate(dt) # Rotate right - 'd'

        if keys[pygame.K_w]:
            self.move(dt) # Move forward - 'w'
        if keys[pygame.K_s]:
            self.move(-dt) # Move backward - 's'

        if keys[pygame.K_SPACE]:
            self.shoot(self.shots_group) # Shoot! - <spacebar>
        