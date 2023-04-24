import pygame
# pygame setup


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
debug = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # load image from assets/test.png
    
    tilemap = pygame.image.load("src/assets/test.png")
    rooms = ['spawn', 'dead-end-s', 'straight', 'corner', 'T', 'cross', 'dead-end-w', 'dead-end-n', 'dead-end-e']
    images = {}
    images["empty"] = pygame.Surface((32, 32))
    for room in rooms:
        images[room] = tilemap.subsurface(pygame.Rect(rooms.index(room)*32, 0, 32, 32))
    
    tiles = []
    # get the map from map.txt
    with open("map.txt") as f:
        for y, line in enumerate(f):
            line = line.replace('\n', '')
            row = line.split(',')
            row_tiles = []
            for x, tile in enumerate(row):
                if tile == '':
                    continue
                row_tiles.append(tile)
            tiles.append(row_tiles)
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            screen.blit(images[tile], (x*32, y*32))
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
