import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

# Sprite Groups
updatable = pygame.sprite.Group() # objects that need updating
drawable = pygame.sprite.Group() # objects that need drawing
asteroids = pygame.sprite.Group() # specifically for asteroids
shots = pygame.sprite.Group() # Specifically for shooting

# Class Containers
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,) # Only needs updating, not drawing
Shot.containers = (updatable, drawable)

# Create an asteroid field to spawn asteroids
asteroid_field = AsteroidField()

# Player Object Instance
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
player.shots_group = shots # Give player a reference to the shots group

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # After initializing pygame but before your game loop:
    clock = pygame.time.Clock()
    dt = 0  # Delta time (time between frames)

    rect_x = 100
    rect_y = 100
    rect_speed_x = 5 # Move 5 pixels per frame
    rect_speed_y = 5

    # Game loop
    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check if the "close" button is clicked
                # Exit the main() function, which ends the game
                game_running = False

        screen.fill(BLACK)  # Fill the screen with black (RGB: 0, 0, 0)

        rect_x += rect_speed_x # Move rect on x
        rect_y += rect_speed_y # Move rect on y

        # Check for collisions with left or right edges of screen
        if rect_x + 50 > SCREEN_WIDTH or rect_x < 0:
            rect_speed_x = -rect_speed_x  # Reverse x direction

        # Check for collisions with top and bottom edges of screen
        if rect_y +50 > SCREEN_HEIGHT or rect_y < 0:
            rect_speed_y = -rect_speed_y #Revere y direction

        # Updates all objects in the updatable group
        updatable.update(dt)

        # Check for asteroid collisions with player ship
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                import sys
                sys.exit()

        # Check for Asteroid/Shot collisions
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
        
        # Draws each object in the drawable group
        for sprite in drawable:
            sprite.draw(screen)  
        
        pygame.display.flip() # Refresh the screen

        clock.tick(60)  # Limit the game to 60 frames per second

        # This limits the game to 60 FPS and returns milliseconds since last frame
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

    print(f"""
          Starting Asteroids!
          Screen width: {SCREEN_WIDTH}
          Screen height: {SCREEN_HEIGHT}
          """)

if __name__ == "__main__":
    main()