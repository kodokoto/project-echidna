import pygame
from graphics.TileSet import TileSet
import os

class Assets:
    
    TILE_SIZE = 32
    ASSET_SIZE = 64

    tiles = {}
    
    player = {}
    
    test_object = None

    def __init__(self):
        self.tileset = TileSet('src/assets/tileset.png', self.TILE_SIZE)
        
        Assets.tiles = self.load_tiles()
        Assets.player = self.load_player_frames()
        Assets.test_object = self.load_test_object()
        
    def load_test_object(self):
        tile = self.tileset.get_tile(self.TILE_SIZE, self.TILE_SIZE*6)
        return pygame.transform.scale(tile, (self.ASSET_SIZE, self.ASSET_SIZE))
        
    def load_player_frames(self):
        
        actions = ["idle", "run E", "run N", "run NE", "run NW", "run SE"]
        
        sprites = {}
        
        for action in actions:
            path = os.path.join("src/assets", "player", action)
            images = [f for f in os.listdir(path) if f.endswith(".png")]
            
            sprites[action] = []
            
            for image in images:
                sprites[action].append(pygame.image.load(os.path.join(path, image)).convert_alpha())
                
            if action == "run E" or action == "run NE" or action == "run N":
                if action == "run E":
                    new_action = "run S"
                elif action == "run NE":
                    new_action = "run SW"
                elif action == "run N":
                    new_action = "run W"
                sprites[new_action] = []
                for image in images:
                    sprites[new_action].append(pygame.transform.flip(pygame.image.load(os.path.join(path, image)).convert_alpha(), True, False))
                    
        return sprites
 
    def load_tiles(self):
        tiles = {
            'basic': self.tileset.get_tile(0, 0),
            'floor-lg': self.tileset.get_tile(self.TILE_SIZE , 0),
            'ramp-left': self.tileset.get_tile(self.TILE_SIZE * 2, 0),
            'ramp-right': self.tileset.get_tile(self.TILE_SIZE * 3, 0),
            'stair-left': self.tileset.get_tile(self.TILE_SIZE * 4, 0),
            'stair-right': self.tileset.get_tile(self.TILE_SIZE * 5, 0),
            'floor-md': self.tileset.get_tile(0, self.TILE_SIZE),
            'floor-sm': self.tileset.get_tile(self.TILE_SIZE, self.TILE_SIZE),
            'ramp-back-left': self.tileset.get_tile(self.TILE_SIZE * 2, self.TILE_SIZE),
            'ramp-back-right': self.tileset.get_tile(self.TILE_SIZE * 3, self.TILE_SIZE),
            'wall-left': self.tileset.get_tile(self.TILE_SIZE * 4, self.TILE_SIZE),
            'wall-fwd-left': self.tileset.get_tile(self.TILE_SIZE * 5, self.TILE_SIZE),
            'water-top': self.tileset.get_tile(0, self.TILE_SIZE * 2),
            'water-full': self.tileset.get_tile(self.TILE_SIZE, self.TILE_SIZE * 2),
            'water-right': self.tileset.get_tile(self.TILE_SIZE * 2, self.TILE_SIZE * 2),
            'water-left': self.tileset.get_tile(self.TILE_SIZE * 3, self.TILE_SIZE * 2),
            'wall-right': self.tileset.get_tile(self.TILE_SIZE * 4, self.TILE_SIZE * 2),
            'wall-forward-right': self.tileset.get_tile(self.TILE_SIZE * 5, self.TILE_SIZE * 2),
            'bridge': self.tileset.get_tile(self.TILE_SIZE, self.TILE_SIZE * 6),
        }

        return {
            key: pygame.transform.scale(value, (self.ASSET_SIZE, self.ASSET_SIZE))
            for key, value in tiles.items()
        }