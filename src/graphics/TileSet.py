import pygame

class TileSet:
    def __init__(self, imagePath: str):
        self.image = self.load_image(imagePath)

    def load_image(self, imagePath: str) -> pygame.Surface:
        return pygame.image.load(imagePath)
        
    def get_tile(self, x, y, width, height, flipX=False, flipY=False) -> pygame.Surface:
        return pygame.transform.flip(self.image.subsurface((x, y, width, height)), flipX, flipY) 
    
