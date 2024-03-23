from entities.Teleport import Teleport
from rooms.Room import Room

class T(Room):
    
    def __init__(self, adj_rooms, flip=False):
        name = 'T'
        entities = [
            Teleport(64, 0, 'N'),
            Teleport(64, 128, 'S'),
            Teleport(128, 64, 'E'),
        ]
        adj_rooms = adj_rooms
        Room.__init__(self, name, entities, adj_rooms, flip)