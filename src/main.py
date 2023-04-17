# Example file showing a basic pygame "game loop"
import pygame
from graphics.Assets import Assets
from graphics.WorldGrid import WorldGrid
from graphics.TileMap import TileMap

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
assets = Assets()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    world = TileMap("src/assets/tilemap.txt")

    grid = WorldGrid(world)
    grid.render(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
