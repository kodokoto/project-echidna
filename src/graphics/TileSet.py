import pygame
class TileSet:
    
    TILE_SIZE = 32
    
    def __init__(self, imagePath: str, tile_size):
        self.TILE_SIZE = tile_size
        self.image = self.load_image(imagePath)

    def load_image(self, imagePath: str) -> pygame.Surface:
        return pygame.image.load(imagePath)
        
    def get_tile(self, x, y, width=TILE_SIZE, height=TILE_SIZE, flipX=False, flipY=False) -> pygame.Surface:
        return pygame.transform.flip(self.image.subsurface((x, y, width, height)), flipX, flipY) 
    
