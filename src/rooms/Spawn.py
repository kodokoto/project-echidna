from entities.Teleport import Teleport
from rooms.Room import Room

class Spawn(Room):
    
    def __init__(self, adj_rooms, flip=False):
        name = 'spawn'
        entities = [
            Teleport(64, 0, 'N'),
            # TestEntity(64, 32, 16)
        ]
        adj_rooms = adj_rooms
        Room.__init__(self, name, entities, adj_rooms, flip)
        
            
    