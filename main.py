import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame and set up the display window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Setup clock for limiting framerate
    clock = pygame.time.Clock()
    dt = 0.0

    # Initialize font for score display
    font = pygame.font.Font(None, 36)
    score = 0

    # Create sprite groups for updating, drawing, asteroids, and shots
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign containers for classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Instantiate game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Main game loop
    while True:
        log_state()

        # Handle user events (like closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects in the updatable group
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print(f"Game over! Final Score: {score}")
                sys.exit()

        # Check for collisions between shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    score += 100  # Award 100 points per asteroid hit!

        # Clear screen with black background
        screen.fill("black")

        # Draw all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)

        # Render and draw the score text
        score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surface, (20, 20))

        # Refresh display
        pygame.display.flip()

        # Cap at 60 FPS and update delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
