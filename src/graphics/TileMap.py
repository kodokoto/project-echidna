from graphics.Assets import Assets
from graphics.Tile import Tile

class TileMap:
    def __init__(self, map_file):
        self.map_file = map_file
        self.width = 0
        self.height = 0
        self.tiles = self.load_map()

    def load_map(self):
        _map = []
        with open(self.map_file, 'r') as file:
            for y, line in enumerate(file):
                self.height += 1
                # remove newline character
                line = line.replace('\n', '')
                # split by comma
                tiles = line.split(',')
                
                # get max width
                self.width = max(self.width, len(tiles))
                for x, tile in enumerate(tiles):
                    if tile == 'none':
                        continue
                    surface = Assets.tiles[tile]
                    width = surface.get_width()
                    height = surface.get_height()
                    _map.append(Tile(Assets.tiles[tile], x*width/2, y*height/2, tile, True if tile == 'wall-fwd-left' else False))
        return _map
    
    def render(self):
        for row in self.tiles:
            for tile in row:
                tile.render()