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

assets = Assets()
world = TileMap("src/assets/tilemap.txt")
grid = WorldGrid(world)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # update() and render() your game objects
    grid.update()
    grid.render(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
