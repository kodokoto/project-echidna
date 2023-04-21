from graphics.Visible import Visible
import config
class Entity(Visible):
    def __init__(self, surface, x, y):
        super().__init__(surface, x, y)
    
    def is_colliding_with_tiles(self) -> bool:
        for row in config.world.tilemap.tiles:
            for tile in row:
                if self.is_colliding_with(tile) and tile.isSolid: 
                    return True
        return False    