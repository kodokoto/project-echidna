from entities.Teleport import Teleport
from rooms.Room import Room

class Cross(Room):
    
    def __init__(self, adj_rooms, rotate=0):
        name = 'cross'
        entities = [
            Teleport(64, 0, 'N'),
            Teleport(0, 32, 'E'),
            Teleport(64, 128, 'S'),
            Teleport(128, 32, 'W'),
        ]
        adj_rooms = adj_rooms
        Room.__init__(self, name, entities, adj_rooms, rotate)
        
            
    