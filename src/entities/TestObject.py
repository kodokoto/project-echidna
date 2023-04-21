import pygame
from graphics.Assets import Assets
from config import screen
from systems import coordinates

class TestObject:
    
    def __init__(self, x, y, z, isSolid=True):
        self.isSolid = isSolid
        self.SPRITE = Assets.test_object
        self.width = self.SPRITE.get_width()/2
        self.height = self.SPRITE.get_height()/2
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.z = z
        
    def get_projected_coordinates(self):
        return coordinates.project(self.rect.x - self.width, self.rect.y , self.z)

    def update(self):
        pass
    
    def render(self):
        screen.blit(self.SPRITE, self.get_projected_coordinates())