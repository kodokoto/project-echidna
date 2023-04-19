import pygame
from graphics.Visible import Visible
from systems import coordinates
from config import screen

class Tile(Visible): 

    def __init__(self, surface, x, y, isSolid=False):
        super().__init__(surface, x, y)
        self.isSolid = isSolid
        self.width /=4

    def render(self):
        if self.isSolid:
            self.surface.set_alpha(100)
            pygame.draw.rect(screen, (255, 0, 0), self.model, 1)
        screen.blit(self.surface, (self.x, self.y))
