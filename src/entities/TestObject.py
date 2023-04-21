import pygame
from graphics.Assets import Assets
from config import screen
from graphics.Visible import Visible
from systems import coordinates

class TestObject(Visible):
    
    def __init__(self, x, y, z, isSolid=True):
        Visible.__init__(self, Assets.test_object, Assets.test_object.get_width()/2, Assets.test_object.get_height()/2, x, y, z)
        self.isSolid = isSolid
        
    def get_projected_coordinates(self):
        return coordinates.project(self.x - self.width, self.y , self.z)

    def update(self):
        pass
    
    def render(self):
        screen.blit(self.surface, self.get_projected_coordinates())