import math
from entities.TestEntity import TestEntity
from graphics.Assets import Assets
from graphics.TileMap import TileMap
from entities.Player import Player
class World:

    def __init__(self):
        self.tilemap = TileMap('src/assets/tilemap.txt')
        self.midpoint = ((Assets.ASSET_SIZE/2)*self.tilemap.width//2, (Assets.ASSET_SIZE/2)*self.tilemap.height//2)
        self.player = Player(*self.midpoint)
        self.entities = [TestEntity(64, 32, 16)]
        self.origin = (self.tilemap.width * Assets.ASSET_SIZE, self.tilemap.height * Assets.ASSET_SIZE)

    def update(self):
        for tile in self.tilemap.tiles:
            tile.update()
        self.player.update()

    def render(self):
        all_sprites = []
        entities = self.entities.copy()
        
        if self.player.is_below_floor():
            all_sprites.append(self.player)
        else:
            entities.append(self.player)

        for tile in self.tilemap.tiles:
            all_sprites.append(tile)
        
        all_sprites.sort(key=lambda sprite: self.distance_from_origin(*sprite.rect.center), reverse=True)

        
        entities.sort(key=lambda sprite: self.distance_from_origin(*sprite.rect.center), reverse=True)
        for entity in entities:
            all_sprites.append(entity)

        for sprite in all_sprites:
            sprite.render()
        
    def distance_from_origin(self, x, y):
        return math.sqrt((x - self.origin[0])**2 + (y - self.origin[1])**2)