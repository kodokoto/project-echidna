import pygame
from systems import coordinates
from config import screen, debug
from pygame.sprite import Sprite
class Tile(Sprite): 

    def __init__(self, surface, x, y, name, isSolid=False):
        print(f'x: {x}, y: {y}')
        self.name = name
        self.surface = surface
        self.isSolid = isSolid
        self.width = self.surface.get_width()/2
        self.height = self.surface.get_height()/2
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.mask = pygame.mask.from_surface(self.surface)
        self.z = 0
        if debug:
            self.opaque = False
            
    def get_isometric_coordinates(self):
        return coordinates.isometric_to_cartesian(self.rect.x, self.rect.y)
    
    def get_projected_coordinates(self):
        return coordinates.project(self.rect.x - self.width, self.rect.y , self.z)

    def update(self):
        self.mask = pygame.mask.from_surface(self.surface)

    def render(self):
        if debug:
            if self.opaque:
                self.surface.set_alpha(100)
            else:
                self.surface.set_alpha(255)
            col = (0, 0, 255)
            if self.isSolid:
                col = (255, 0, 0)
            pygame.draw.rect(screen, col, self.rect, 1)
            
        screen.blit(self.surface, self.get_projected_coordinates())

