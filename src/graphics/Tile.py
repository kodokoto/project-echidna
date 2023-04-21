import pygame
from graphics.Visible import Visible
from systems import coordinates
from config import screen, debug
class Tile(Visible): 

    def __init__(self, surface, x, y, name, isSolid=False):
        Visible.__init__(self, surface, surface.get_width()/2, surface.get_height()/2, x, y)
        self.name = name
        self.isSolid = isSolid
        self.mask = pygame.mask.from_surface(self.surface)
        if debug:
            self.opaque = False
            
    def get_isometric_coordinates(self):
        return coordinates.isometric_to_cartesian(self.x, self.y)
    
    def get_projected_coordinates(self):
        return coordinates.project(self.x - self.width, self.y , self.z)

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

