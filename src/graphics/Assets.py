import pygame
from graphics.TileSet import TileSet

TILE_SIZE = 32
CHAR_SIZE = 350
ASSET_SIZE = 64

class Assets:

    tiles = {}

    player_up = []
    player_down = []
    player_left = []
    player_right = []
    player_idle = []


    def __init__(self):
        self.tileset = TileSet('src/assets/tileset.png')
        self.character_sprite_front = TileSet('src/assets/CharacterSheet_CharacterFront.png')
        self.character_sprite_back = TileSet('src/assets/CharacterSheet_CharacterBack.png')

        Assets.tiles = self.load_tiles()
        Assets.player_up, Assets.player_down, Assets.player_left, Assets.player_right, Assets.player_idle = self.load_character_frames()
 
    def load_tiles(self):
        tiles = {
            'basic': self.tileset.get_tile(0, 0, TILE_SIZE, TILE_SIZE),
            'floor-lg': self.tileset.get_tile(TILE_SIZE , 0, TILE_SIZE, TILE_SIZE),
            'ramp-left': self.tileset.get_tile(TILE_SIZE * 2, 0, TILE_SIZE, TILE_SIZE),
            'ramp-right': self.tileset.get_tile(TILE_SIZE * 3, 0, TILE_SIZE, TILE_SIZE),
            'stair-left': self.tileset.get_tile(TILE_SIZE * 4, 0, TILE_SIZE, TILE_SIZE),
            'stair-right': self.tileset.get_tile(TILE_SIZE * 5, 0, TILE_SIZE, TILE_SIZE),
            'floor-md': self.tileset.get_tile(0, TILE_SIZE, TILE_SIZE, TILE_SIZE),
            'floor-sm': self.tileset.get_tile(TILE_SIZE, TILE_SIZE, TILE_SIZE, TILE_SIZE),
            'ramp-back-left': self.tileset.get_tile(TILE_SIZE * 2, TILE_SIZE, TILE_SIZE, TILE_SIZE),
            'ramp-back-right': self.tileset.get_tile(TILE_SIZE * 3, TILE_SIZE, TILE_SIZE, TILE_SIZE),
            'wall-left': self.tileset.get_tile(TILE_SIZE * 4, TILE_SIZE, TILE_SIZE, TILE_SIZE),
            'wall-fwd-left': self.tileset.get_tile(TILE_SIZE * 5, TILE_SIZE, TILE_SIZE, TILE_SIZE),
            'water-top': self.tileset.get_tile(0, TILE_SIZE * 2, TILE_SIZE, TILE_SIZE),
            'water-full': self.tileset.get_tile(TILE_SIZE, TILE_SIZE * 2, TILE_SIZE, TILE_SIZE),
            'water-right': self.tileset.get_tile(TILE_SIZE * 2, TILE_SIZE * 2, TILE_SIZE, TILE_SIZE),
            'water-left': self.tileset.get_tile(TILE_SIZE * 3, TILE_SIZE * 2, TILE_SIZE, TILE_SIZE),
            'wall-right': self.tileset.get_tile(TILE_SIZE * 4, TILE_SIZE * 2, TILE_SIZE, TILE_SIZE),
            'wall-forward-right': self.tileset.get_tile(TILE_SIZE * 5, TILE_SIZE * 2, TILE_SIZE, TILE_SIZE),
        }

        return {
            key: pygame.transform.scale(value, (ASSET_SIZE, ASSET_SIZE))
            for key, value in tiles.items()
        }


    
    def load_character_frames(self):
        char_assets = [
            # player_up
            [
                self.character_sprite_back.get_tile(0, CHAR_SIZE, CHAR_SIZE, CHAR_SIZE, flipX=True),
                self.character_sprite_back.get_tile(CHAR_SIZE, CHAR_SIZE, CHAR_SIZE, CHAR_SIZE, flipX=True),
                self.character_sprite_back.get_tile(CHAR_SIZE * 2, CHAR_SIZE, CHAR_SIZE, CHAR_SIZE, flipX=True),
                self.character_sprite_back.get_tile(CHAR_SIZE * 3, CHAR_SIZE, CHAR_SIZE, CHAR_SIZE, flipX=True),
            ],
            # player_down
            [
                self.character_sprite_front.get_tile(0, CHAR_SIZE * 2, CHAR_SIZE, CHAR_SIZE),
                self.character_sprite_front.get_tile(CHAR_SIZE, CHAR_SIZE * 2, CHAR_SIZE, CHAR_SIZE),
                self.character_sprite_front.get_tile(CHAR_SIZE * 2, CHAR_SIZE * 2, CHAR_SIZE, CHAR_SIZE),
                self.character_sprite_front.get_tile(CHAR_SIZE * 3, CHAR_SIZE * 2, CHAR_SIZE, CHAR_SIZE),
            ],
            # player_left
            [
                self.character_sprite_back.get_tile(0, CHAR_SIZE, CHAR_SIZE, CHAR_SIZE),
                self.character_sprite_back.get_tile(CHAR_SIZE, CHAR_SIZE, CHAR_SIZE, CHAR_SIZE),
                self.character_sprite_back.get_tile(CHAR_SIZE * 2, CHAR_SIZE, CHAR_SIZE, CHAR_SIZE),
                self.character_sprite_back.get_tile(CHAR_SIZE * 3, CHAR_SIZE, CHAR_SIZE, CHAR_SIZE),
            ],
            #player_right
            [
                self.character_sprite_front.get_tile(0, CHAR_SIZE * 2, CHAR_SIZE, CHAR_SIZE, flipX=True),
                self.character_sprite_front.get_tile(CHAR_SIZE, CHAR_SIZE * 2, CHAR_SIZE, CHAR_SIZE, flipX=True),
                self.character_sprite_front.get_tile(CHAR_SIZE * 2, CHAR_SIZE * 2, CHAR_SIZE, CHAR_SIZE, flipX=True),
                self.character_sprite_front.get_tile(CHAR_SIZE * 3, CHAR_SIZE * 2, CHAR_SIZE, CHAR_SIZE, flipX=True),
            ],
            #player_idle
            [
                self.character_sprite_front.get_tile(0, 0, CHAR_SIZE, CHAR_SIZE),
                self.character_sprite_front.get_tile(CHAR_SIZE, 0, CHAR_SIZE, CHAR_SIZE),
                self.character_sprite_front.get_tile(0, 0, CHAR_SIZE, CHAR_SIZE),
                self.character_sprite_front.get_tile(CHAR_SIZE, 0, CHAR_SIZE, CHAR_SIZE),
            ]

        ]
        return [
            [pygame.transform.scale(char, (ASSET_SIZE, ASSET_SIZE)) for char in char_assets[0]],
            [pygame.transform.scale(char, (ASSET_SIZE, ASSET_SIZE)) for char in char_assets[1]],
            [pygame.transform.scale(char, (ASSET_SIZE, ASSET_SIZE)) for char in char_assets[2]],
            [pygame.transform.scale(char, (ASSET_SIZE, ASSET_SIZE)) for char in char_assets[3]],
            [pygame.transform.scale(char, (ASSET_SIZE, ASSET_SIZE)) for char in char_assets[4]],
        ]
