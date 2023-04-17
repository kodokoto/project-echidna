class Tile: 
    TILE_WIDTH = 32
    TILE_HEIGHT = 32

    def __init__(self, texture, x, y, solid=True):
        self.x = x
        self.y = y
        self.texture = texture
        self.solid = solid

