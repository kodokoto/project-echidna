import itertools
from entities.Teleport import Teleport
from graphics.Assets import Assets

class Room:
    uid = itertools.count()


    def __init__(self, name, entities, adj_rooms, weight=1, rotate=0):
        self.id = next(Room.uid)
        self.name = f'{name}-{self.id}'

        print([_key for _key in Assets.tile_maps.keys()])
        print(name)
        self.tilemap = Assets.tile_maps[name]
        self.spawns = [((Assets.ASSET_SIZE/2)*self.tilemap.width//2, (Assets.ASSET_SIZE/2)*self.tilemap.height//2)]
        self.entities = entities
        self.origin = (self.tilemap.width * Assets.ASSET_SIZE, self.tilemap.height * Assets.ASSET_SIZE)
        self.adj_rooms = adj_rooms
        self.adjacency_lists = {
            "N": [],
            "E": [],
            "S": [],
            "W": []
        }
        self.weight = weight
        self.rotate = rotate        

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
        
    def get_teleports(self):
        return [entity for entity in self.entities if isinstance(entity, Teleport)]
    
    def get_teleport_by_direction(self, direction):
        print(f"Getting teleport in direction {direction}")
        print(f"Number of teleports: {len(self.entities)}")
        print(self.name)
        print([teleport.direction for teleport in self.get_teleports()])
        for teleport in self.get_teleports():
            if teleport.direction == direction:
                return teleport
        else: raise Exception(f"Teleport in direction {direction} not found")
