import pygame
from constants import *
from logger import log_state

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

 # Main game loop
 while True:
      log_state()
      # Handle user events (like closing the window)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return

     # clears screen with black background + refresh display with a cap at 60 FPS & delta time
      screen.fill("black")
      pygame.display.flip()
      dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()
