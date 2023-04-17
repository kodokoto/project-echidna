class WorldGrid:

    def __init__(self,  tilemap, cell_size=32):
        self.cell_size = cell_size
        self.tilemap = tilemap

    def render(self, screen):
        for y in range(len(self.tilemap.tiles)):
            for x in range(len(self.tilemap.tiles[y])):
                screen.blit(self.tilemap.tiles[y][x].texture, self.center_coordinates(*self.convert_to_isometric_coordinates(x * self.cell_size/2, y * self.cell_size/2), screen))
        
    def convert_to_isometric_coordinates(self, x, y):
        return (x - y, (x + y) / 2)
    
    def center_coordinates(self, x, y, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        return (x + screen_width / 2, y + screen_height / 2)