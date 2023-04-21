from entities.TestEntity import TestEntity
from graphics.Assets import Assets
from rooms.Room import Room
from graphics.TileMap import TileMap

class Spawn(Room):
    
    def __init__(self,):
        name = 'Spawn'
        tilemap = TileMap('src/assets/rooms/spawn.txt')
        entities = [TestEntity(64, 32, 16)]
        spawns = [((Assets.ASSET_SIZE/2)*tilemap.width//2, (Assets.ASSET_SIZE/2)*tilemap.height//2)]
        Room.__init__(self, name, spawns, tilemap, entities)
        
    def update(self):
        for tile in self.tiles:
            tile.update()
        for entity in self.entities:
            entity.update()
            
    