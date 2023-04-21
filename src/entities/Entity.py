from graphics.Visible import Visible
import config
class Entity(Visible):
    def __init__(self, surface, width, height, x, y, z, isSolid):
        Visible.__init__(self, surface, width, height, x, y, z)
        self.isSolid = isSolid
    
    def is_on_floor(self):
        return self.rect.collidelist([t.rect for t in config.world.room.tiles]) != -1 and not self.is_below_floor()
    
    def is_below_floor(self):
        return self.z < 0