import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check if the "close" button is clicked
                return  # Exit the main() function, which ends the game

        screen.fill((0, 0, 0))  # Fill the screen with black (RGB: 0, 0, 0)
        pygame.display.flip()  # Refresh the screen

    print(f"""
          Starting Asteroids!
          Screen width: {SCREEN_WIDTH}
          Screen height: {SCREEN_HEIGHT}
          """)

if __name__ == "__main__":
    main()