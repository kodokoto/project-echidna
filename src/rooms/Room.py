from graphics.Assets import Assets

class Room:

    def __init__(self, name, spawns, tilemap, entities, sockets, weight=1, flip=False):
        self.name = name
        self.spawns = spawns
        self.tilemap = tilemap
        self.entities = entities
        self.origin = (self.tilemap.width * Assets.ASSET_SIZE, self.tilemap.height * Assets.ASSET_SIZE)
        self.sockets = sockets
        self.adjacency_lists = {
            "N": [],
            "E": [],
            "S": [],
            "W": []
        }
        self.weight = weight
        self.flip = flip
        

    def update(self):
        for tile in self.tiles:
            tile.update()
        for entity in self.entities:
            entity.update()
    
    def render(self):
        pass

    @property
    def tiles(self):
        return self.tilemap.tiles
    
    @tiles.setter
    def tiles(self, tiles):
        self.tilemap.tiles = tiles
