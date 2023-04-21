from graphics.Visible import Visible
class Entity(Visible):
    def __init__(self, surface, width, height, x, y, z, isSolid):
        Visible.__init__(self, surface, width, height, x, y, z)
        self.isSolid = isSolid
    