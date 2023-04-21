from abc import ABC, abstractmethod
from systems import coordinates
class Visible(ABC):

    def __init__(self, surface, x, y):
        self.surface = surface
        self.model = self.surface.get_rect()
        new = coordinates.project(x * self.model.width /2, y * self.model.height /2)
        self.model.x = new[0]
        self.model.y = new[1]

    @abstractmethod
    def render(self):
        pass

    def is_colliding_with(self, other):
        return self.model.colliderect(other.model)
        
    def get_surface(self):
        return self.surface
        
    @property
    def x(self):
        return self.model.x

    @x.setter
    def x(self, x):
        print(f'old: {self.model.x}, new: {x}')
        self.model.x = x
    
    @property
    def y(self):
        return self.model.y

    @y.setter
    def y(self, y):
        self.model.y = y
        
    @property
    def width(self):
        return self.model.width
    
    @width.setter
    def width(self, width):
        self.model.width = width
    
    @property
    def height(self):
        return self.model.height
    
    @height.setter
    def height(self, height):
        self.model.height = height
    
    def get_coordinates(self):
        return self.model.x, self.model.y
    
    def set_coordinates(self, x, y):
        self.model.move(x, y)
    
    
