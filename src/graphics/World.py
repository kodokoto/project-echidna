from graphics.TileMap import TileMap
from entities.Player import Player

class World:

    def __init__(self):
        self.tilemap = TileMap('src/assets/tilemap.txt')
        self.player = Player(0, 0)

    def update(self):
        self.player.update()

    def render(self):
        self.tilemap.render()
        self.player.render()
    
    