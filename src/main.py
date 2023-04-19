import pygame
from graphics.Assets import Assets
from graphics.World import World
from graphics.TileMap import TileMap
from config import screen, clock, running, dt

# pygame setup

assets = Assets()
grid = World()

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
    grid.render()

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
