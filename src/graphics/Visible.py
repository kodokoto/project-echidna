from abc import ABC, abstractmethod

import pygame
from pygame.sprite import Sprite
class Visible(ABC, Sprite):

    def __init__(self, surface, width, height, x, y, z=0):
        self.surface = surface
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.z = z
        Sprite.__init__(self)

    @abstractmethod
    def render(self):
        pass
    
    def collides_with(self, other):
        if isinstance(other, pygame.Rect):
            return self.rect.colliderect(other)
        return self.rect.colliderect(other.rect)
        
    def get_surface(self):
        return self.surface
            
    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, x):
        self.rect.x = x
    
    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, y):
        self.rect.y = y
        
    def get_coordinates(self):
        return self.rect.x, self.rect.y
    
    
