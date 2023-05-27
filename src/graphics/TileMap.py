from graphics.Assets import Assets
from graphics.Tile import Tile
import numpy as np

SOLID_TILES = [
    'wall-fwd-left',
]

class TileMap:
    def __init__(self, map_file, flip=False):
        self.map_file = map_file
        self.width = 0
        self.height = 0
        self.flip = flip
        self.tiles = self.load_map()

    def load_map(self):
        _map = []
        parsed_map_file = self.parse_map_file()
        
        if self.flip:
            parsed_map_file = list(zip(*parsed_map_file[::-1]))
        
        for y, r in enumerate(parsed_map_file):
            row = []
            self.height += 1
            self.width = max(self.width, len(r))
            for x, tile in enumerate(r):
                
                if tile == 'none':
                    continue
                
                surface = Assets.tiles[tile]
                xPos = x*surface.get_width()/2
                yPos = y*surface.get_height()/2
                isSolid = True if tile in SOLID_TILES else False
                
                tile = Tile(surface, xPos, yPos, tile, isSolid)
                
                if self.flip:
                    tile.flip()
                    
                row.append(tile)
            _map.append(row)
            
        # flatten map
        _map = [j for sub in _map for j in sub]
        
        return _map
    
    def parse_map_file(self):
        _map = []
        with open(self.map_file, 'r') as file:
            for line in file:
                row = []
                # remove newline character
                line = line.replace('\n', '')
                # split by comma
                tiles = line.split(',')
                # get max width
                for tile in tiles:
                    row.append(tile)
                _map.append(row)
        return _map

    def render(self):
        for row in self.tiles:
            for tile in row:
                tile.render()