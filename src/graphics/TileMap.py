from graphics.Assets import Assets
from graphics.Tile import Tile

class TileMap:
    def __init__(self, map_file):
        self.map_file = map_file
        self.tiles = self.load_map()

    def load_map(self):
        _map = []
        with open(self.map_file, 'r') as file:
            for y, line in enumerate(file):
                # remove newline character
                line = line.replace('\n', '')
                row = []
                # split by comma
                for x, tile in enumerate(line.split(',')):
                    row.append(Tile(Assets.tiles[tile], x, y))
                _map.append(row)
        return _map
    
    def render(self):
        for row in self.tiles:
            for tile in row:
                tile.render()