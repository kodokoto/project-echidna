from systems import coordinates
from config import screen
from graphics import Assets
class Tile: 

    def __init__(self, texture, x, y, solid=True):
        self.x = x
        self.y = y
        self.texture = texture
        self.solid = solid

    def render(self):
        screen.blit(self.texture, coordinates.process(self.x * Assets.ASSET_SIZE/2, self.y * Assets.ASSET_SIZE/2))