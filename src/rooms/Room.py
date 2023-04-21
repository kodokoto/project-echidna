from graphics.Assets import Assets

class Room:

    def __init__(self, name, spawns, tilemap, entities):
        self.name = name
        self.spawns = spawns
        self.tilemap = tilemap
        self.entities = entities
        self.origin = (self.tilemap.width * Assets.ASSET_SIZE, self.tilemap.height * Assets.ASSET_SIZE)
    
    def update(self):
        pass
    
    def render(self):
        pass

    @property
    def tiles(self):
        return self.tilemap.tiles
    
    @tiles.setter
    def tiles(self, tiles):
        self.tilemap.tiles = tiles
