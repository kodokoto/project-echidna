from entities.Teleport import Teleport
from rooms.Room import Room

class Straight(Room):
    
    def __init__(self, adj_rooms, rotate=0):
        name = 'straight'
        entities = [
            Teleport(64, 0, 'N'),
            Teleport(64, 128, 'S'),
        ]
        adj_rooms = adj_rooms
        Room.__init__(self, name, entities, adj_rooms, rotate)
        
            
    