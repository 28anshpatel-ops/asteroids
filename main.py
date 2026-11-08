import pygame
from constants import *
from logger import log_state
from player import Player


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

  #
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

 	 #
  Player.containers = (updatable, drawable)

  #
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  # Main game loop
  while True:
      log_state()

      # Handle user events (like closing the window)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return

      #
      updatable.update(dt)

      #
      player.update(dt)

      # Clear screen with black background
      screen.fill("black")

      # Draw all objects in the drawable group
      for obj in drawable:
          obj.draw(screen)

      # Refresh display
      pygame.display.flip()

      # Cap at 60 FPS and update delta time
      dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
