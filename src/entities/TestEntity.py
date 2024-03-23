from entities.Entity import Entity
from graphics.Assets import Assets
from config import screen

class TestEntity(Entity):
    
    def __init__(self, x, y, z, isSolid=True):
        Entity.__init__(self, Assets.test_object, Assets.test_object.get_width()/2, Assets.test_object.get_height()/2, x, y, z, isSolid)
        
    def update(self):
        pass
    
    def render(self):
        screen.blit(self.surface, self.get_projected_coordinates())