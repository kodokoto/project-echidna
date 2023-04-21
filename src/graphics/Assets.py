import pygame
from graphics.TileSet import TileSet
import os

class Assets:
    
    TILE_SIZE = 32
    CHAR_SIZE = 350
    ASSET_SIZE = 64

    tiles = {}

    player_up = []
    player_down = []
    player_left = []
    player_right = []
    player_idle = []
    
    player = {}
    
    test_object = None

    def __init__(self):
        self.tileset = TileSet('src/assets/tileset.png')
        self.character_sprite_front = TileSet('src/assets/CharacterSheet_CharacterFront.png')
        self.character_sprite_back = TileSet('src/assets/CharacterSheet_CharacterBack.png')

        Assets.tiles = self.load_tiles()
        Assets.player_up, Assets.player_down, Assets.player_left, Assets.player_right, Assets.player_idle = self.load_character_frames()
        Assets.player = self.load_player_frames()
        Assets.test_object = self.load_test_object()
        
    def load_test_object(self):
        tile = self.tileset.get_tile(self.TILE_SIZE, self.TILE_SIZE*6, self.TILE_SIZE, self.TILE_SIZE)
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
            'basic': self.tileset.get_tile(0, 0, self.TILE_SIZE, self.TILE_SIZE),
            'floor-lg': self.tileset.get_tile(self.TILE_SIZE , 0, self.TILE_SIZE, self.TILE_SIZE),
            'ramp-left': self.tileset.get_tile(self.TILE_SIZE * 2, 0, self.TILE_SIZE, self.TILE_SIZE),
            'ramp-right': self.tileset.get_tile(self.TILE_SIZE * 3, 0, self.TILE_SIZE, self.TILE_SIZE),
            'stair-left': self.tileset.get_tile(self.TILE_SIZE * 4, 0, self.TILE_SIZE, self.TILE_SIZE),
            'stair-right': self.tileset.get_tile(self.TILE_SIZE * 5, 0, self.TILE_SIZE, self.TILE_SIZE),
            'floor-md': self.tileset.get_tile(0, self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE),
            'floor-sm': self.tileset.get_tile(self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE),
            'ramp-back-left': self.tileset.get_tile(self.TILE_SIZE * 2, self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE),
            'ramp-back-right': self.tileset.get_tile(self.TILE_SIZE * 3, self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE),
            'wall-left': self.tileset.get_tile(self.TILE_SIZE * 4, self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE),
            'wall-fwd-left': self.tileset.get_tile(self.TILE_SIZE * 5, self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE),
            'water-top': self.tileset.get_tile(0, self.TILE_SIZE * 2, self.TILE_SIZE, self.TILE_SIZE),
            'water-full': self.tileset.get_tile(self.TILE_SIZE, self.TILE_SIZE * 2, self.TILE_SIZE, self.TILE_SIZE),
            'water-right': self.tileset.get_tile(self.TILE_SIZE * 2, self.TILE_SIZE * 2, self.TILE_SIZE, self.TILE_SIZE),
            'water-left': self.tileset.get_tile(self.TILE_SIZE * 3, self.TILE_SIZE * 2, self.TILE_SIZE, self.TILE_SIZE),
            'wall-right': self.tileset.get_tile(self.TILE_SIZE * 4, self.TILE_SIZE * 2, self.TILE_SIZE, self.TILE_SIZE),
            'wall-forward-right': self.tileset.get_tile(self.TILE_SIZE * 5, self.TILE_SIZE * 2, self.TILE_SIZE, self.TILE_SIZE),
        }

        return {
            key: pygame.transform.scale(value, (self.ASSET_SIZE, self.ASSET_SIZE))
            for key, value in tiles.items()
        }

    def load_character_frames(self):
        char_assets = [
            # player_up
            [
                self.character_sprite_back.get_tile(0, self.CHAR_SIZE, self.CHAR_SIZE, self.CHAR_SIZE, flipX=True),
                self.character_sprite_back.get_tile(self.CHAR_SIZE, self.CHAR_SIZE, self.CHAR_SIZE, self.CHAR_SIZE, flipX=True),
                self.character_sprite_back.get_tile(self.CHAR_SIZE * 2, self.CHAR_SIZE, self.CHAR_SIZE, self.CHAR_SIZE, flipX=True),
                self.character_sprite_back.get_tile(self.CHAR_SIZE * 3, self.CHAR_SIZE, self.CHAR_SIZE, self.CHAR_SIZE, flipX=True),
            ],
            # player_down
            [
                self.character_sprite_front.get_tile(0, self.CHAR_SIZE * 2, self.CHAR_SIZE, self.CHAR_SIZE),
                self.character_sprite_front.get_tile(self.CHAR_SIZE, self.CHAR_SIZE * 2, self.CHAR_SIZE, self.CHAR_SIZE),
                self.character_sprite_front.get_tile(self.CHAR_SIZE * 2, self.CHAR_SIZE * 2, self.CHAR_SIZE, self.CHAR_SIZE),
                self.character_sprite_front.get_tile(self.CHAR_SIZE * 3, self.CHAR_SIZE * 2, self.CHAR_SIZE, self.CHAR_SIZE),
            ],
            # player_left
            [
                self.character_sprite_back.get_tile(0, self.CHAR_SIZE, self.CHAR_SIZE, self.CHAR_SIZE),
                self.character_sprite_back.get_tile(self.CHAR_SIZE, self.CHAR_SIZE, self.CHAR_SIZE, self.CHAR_SIZE),
                self.character_sprite_back.get_tile(self.CHAR_SIZE * 2, self.CHAR_SIZE, self.CHAR_SIZE, self.CHAR_SIZE),
                self.character_sprite_back.get_tile(self.CHAR_SIZE * 3, self.CHAR_SIZE, self.CHAR_SIZE, self.CHAR_SIZE),
            ],
            #player_right
            [
                self.character_sprite_front.get_tile(0, self.CHAR_SIZE * 2, self.CHAR_SIZE, self.CHAR_SIZE, flipX=True),
                self.character_sprite_front.get_tile(self.CHAR_SIZE, self.CHAR_SIZE * 2, self.CHAR_SIZE, self.CHAR_SIZE, flipX=True),
                self.character_sprite_front.get_tile(self.CHAR_SIZE * 2, self.CHAR_SIZE * 2, self.CHAR_SIZE, self.CHAR_SIZE, flipX=True),
                self.character_sprite_front.get_tile(self.CHAR_SIZE * 3, self.CHAR_SIZE * 2, self.CHAR_SIZE, self.CHAR_SIZE, flipX=True),
            ],
            #player_idle
            [
                self.character_sprite_front.get_tile(0, 0, self.CHAR_SIZE, self.CHAR_SIZE),
                self.character_sprite_front.get_tile(self.CHAR_SIZE, 0, self.CHAR_SIZE, self.CHAR_SIZE),
                self.character_sprite_front.get_tile(0, 0, self.CHAR_SIZE, self.CHAR_SIZE),
                self.character_sprite_front.get_tile(self.CHAR_SIZE, 0, self.CHAR_SIZE, self.CHAR_SIZE),
            ]

        ]
        
        return [
            [pygame.transform.scale(char, (self.ASSET_SIZE, self.ASSET_SIZE)) for char in char_assets[0]],
            [pygame.transform.scale(char, (self.ASSET_SIZE, self.ASSET_SIZE)) for char in char_assets[1]],
            [pygame.transform.scale(char, (self.ASSET_SIZE, self.ASSET_SIZE)) for char in char_assets[2]],
            [pygame.transform.scale(char, (self.ASSET_SIZE, self.ASSET_SIZE)) for char in char_assets[3]],
            [pygame.transform.scale(char, (self.ASSET_SIZE, self.ASSET_SIZE)) for char in char_assets[4]],
        ]
