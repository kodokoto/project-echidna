import math
from entities.TestEntity import TestEntity
from graphics.Assets import Assets
from graphics.TileMap import TileMap
from entities.Player import Player
from rooms.Spawn import Spawn
class World:

    def __init__(self):
        # self.tilemap = TileMap('src/assets/tilemap.txt')
        # self.midpoint = ((Assets.ASSET_SIZE/2)*self.tilemap.width//2, (Assets.ASSET_SIZE/2)*self.tilemap.height//2)
        self.room = Spawn()
        print(self.room.spawns)
        self.player = Player(*self.room.spawns[0])
        # self.entities = [TestEntity(64, 32, 16)]
        # self.origin = (self.tilemap.width * Assets.ASSET_SIZE, self.tilemap.height * Assets.ASSET_SIZE)

    def update(self):
        self.room.update()
        self.player.update()

    def render(self):
        sprites = []
        entities = self.room.entities.copy()
        tiles = self.room.tiles.copy()
        
        # if player is below floor, render player before tiles
        if self.player.is_below_floor():
            sprites.append(self.player)
        # else render player as an entity
        else:
            entities.append(self.player)

        # render tiles
        for tile in tiles:
            sprites.append(tile)
        
        # sort entetiesby distance from camera (origin)
        sprites.sort(key=lambda sprite: self.distance_from_origin(*sprite.rect.center), reverse=True)
        entities.sort(key=lambda sprite: self.distance_from_origin(*sprite.rect.center), reverse=True)
        
        # render entities in order
        for entity in entities:
            sprites.append(entity)
            
        # render sprites
        for sprite in sprites:
            sprite.render()
        
    def distance_from_origin(self, x, y):
        return math.sqrt((x - self.room.origin[0])**2 + (y - self.room.origin[1])**2)