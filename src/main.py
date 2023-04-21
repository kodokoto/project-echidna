import pygame
from graphics.Assets import Assets
from graphics.World import World
import config

# pygame setup
config.assets = Assets()
config.world = World()

while config.running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.running = False

    # fill the screen with a color to wipe away anything from last frame
    config.screen.fill("black")

    # update() and render() your game objects
    config.world.update()
    config.world.render()

    # flip() the display to put your work on screen
    pygame.display.flip()

    config.dt = config.clock.tick(60) / 1000

pygame.quit()
