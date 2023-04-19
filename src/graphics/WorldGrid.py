from entities.Player import Player
from graphics.Assets import Assets

class WorldGrid:

    def __init__(self,  tilemap, cell_size=Assets.ASSET_SIZE):
        self.cell_size = cell_size
        self.tilemap = tilemap
        self.player = Player(0, 0)

    def update(self):
        self.player.update()

    def render(self, screen):
        # render world
        for y in range(len(self.tilemap.tiles)):
            for x in range(len(self.tilemap.tiles[y])):
                screen.blit(self.tilemap.tiles[y][x].texture, self.center_coordinates(*self.convert_to_isometric_coordinates(x * self.cell_size/2, y * self.cell_size/2), screen))

        # render player
        screen.blit(self.player.render(), self.center_coordinates(*self.convert_to_isometric_coordinates(self.player.x, self.player.y), screen))

    def convert_to_isometric_coordinates(self, x, y):
        return (x - y, (x + y) / 2)
    
    def center_coordinates(self, x, y, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        return (x + screen_width / 2, y + screen_height / 2)