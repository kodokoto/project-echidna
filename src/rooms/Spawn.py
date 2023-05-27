from entities.TestEntity import TestEntity
from graphics.Assets import Assets
from rooms.Room import Room
from graphics.TileMap import TileMap

class Spawn(Room):
    
    def __init__(self, flip=False):
        name = 'spawn'
        tilemap = TileMap('src/assets/rooms/spawn.txt', flip)
        entities = [TestEntity(64, 32, 16)]
        spawns = [((Assets.ASSET_SIZE/2)*tilemap.width//2, (Assets.ASSET_SIZE/2)*tilemap.height//2)]
        sockets = {
            "N": [2],
            "E": [0],
            "S": [0],
            "W": [0]
        }
        Room.__init__(self, name, spawns, tilemap, entities, sockets, flip)
                
            
    