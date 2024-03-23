from entities.Entity import Entity
from graphics.Assets import Assets
from config import screen

class Teleport(Entity):
    
    def __init__(self, x, y, direction):
        Entity.__init__(self, Assets.teleport, Assets.teleport.get_width()/2, Assets.teleport.get_height()/2, x-16, y-16, 0, False)
        self.direction = direction
        
    def update(self):
        pass

    def render(self):
        screen.blit(self.surface, self.get_projected_coordinates())
        