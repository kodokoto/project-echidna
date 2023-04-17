from graphics.TileSet import TileSet

ASSET_SIZE = 32

class Assets:

    tiles = {}

    def __init__(self):
        self.tileset = TileSet('src/assets/tileset.png')
        Assets.tiles = self.load_tiles()
        
    def load_tiles(self):
        return {
            'basic': self.tileset.get_tile(0, 0, ASSET_SIZE, ASSET_SIZE),
            'floor-lg': self.tileset.get_tile(ASSET_SIZE , 0, ASSET_SIZE, ASSET_SIZE),
            'ramp-left': self.tileset.get_tile(ASSET_SIZE * 2, 0, ASSET_SIZE, ASSET_SIZE),
            'ramp-right': self.tileset.get_tile(ASSET_SIZE * 3, 0, ASSET_SIZE, ASSET_SIZE),
            'stair-left': self.tileset.get_tile(ASSET_SIZE * 4, 0, ASSET_SIZE, ASSET_SIZE),
            'stair-right': self.tileset.get_tile(ASSET_SIZE * 5, 0, ASSET_SIZE, ASSET_SIZE),
            'floor-md': self.tileset.get_tile(0, ASSET_SIZE, ASSET_SIZE, ASSET_SIZE),
            'floor-sm': self.tileset.get_tile(ASSET_SIZE, ASSET_SIZE, ASSET_SIZE, ASSET_SIZE),
            'ramp-back-left': self.tileset.get_tile(ASSET_SIZE * 2, ASSET_SIZE, ASSET_SIZE, ASSET_SIZE),
            'ramp-back-right': self.tileset.get_tile(ASSET_SIZE * 3, ASSET_SIZE, ASSET_SIZE, ASSET_SIZE),
            'wall-left': self.tileset.get_tile(ASSET_SIZE * 4, ASSET_SIZE, ASSET_SIZE, ASSET_SIZE),
            'wall-fwd-left': self.tileset.get_tile(ASSET_SIZE * 5, ASSET_SIZE, ASSET_SIZE, ASSET_SIZE),
            'water-top': self.tileset.get_tile(0, ASSET_SIZE * 2, ASSET_SIZE, ASSET_SIZE),
            'water-full': self.tileset.get_tile(ASSET_SIZE, ASSET_SIZE * 2, ASSET_SIZE, ASSET_SIZE),
            'water-right': self.tileset.get_tile(ASSET_SIZE * 2, ASSET_SIZE * 2, ASSET_SIZE, ASSET_SIZE),
            'water-left': self.tileset.get_tile(ASSET_SIZE * 3, ASSET_SIZE * 2, ASSET_SIZE, ASSET_SIZE),
            'wall-right': self.tileset.get_tile(ASSET_SIZE * 4, ASSET_SIZE * 2, ASSET_SIZE, ASSET_SIZE),
            'wall-forward-right': self.tileset.get_tile(ASSET_SIZE * 5, ASSET_SIZE * 2, ASSET_SIZE, ASSET_SIZE),
        }

