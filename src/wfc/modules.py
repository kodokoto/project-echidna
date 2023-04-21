
from enum import Enum

class SocketType(Enum):
    NONE = 0
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3
    
class Direction(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"

# Wave Function Collapse - Python implementation
class Prototype:
    
    def __init__(self, name: str, flip: bool, sockets: dict):
        self.name = name
        self.flip = flip
        self.sockets = sockets
        self.neighbors = {
            "N": [],
            "E": [],
            "S": [],
            "W": []
        }        
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
modules = [
    Prototype(
        "spawn", 
        False, 
        {
            "N": 2,
            "E": 0,
            "S": 0,
            "W": 0
        }
    ),
    Prototype(
        "dead-end",
        False,
        {
            "N": 0,
            "E": 0,
            "S": 2,
            "W": 0
        }
    ),
    Prototype(
        "straight",
        False,
        {
            "N": 2,
            "E": 0,
            "S": 2,
            "W": 0
        }
    ),
    Prototype(
        "corner",
        False,
        {
            "N": 2,
            "E": 2,
            "S": 0,
            "W": 0
        }
    ),
    Prototype(
        "T",
        False,
        {
            "N": 2,
            "E": 2,
            "S": 2,
            "W": 0
        },
    ),
    Prototype(
        "cross",
        False,
        {
            "N": 2,
            "E": 2,
            "S": 2,
            "W": 2
        }
    )
]

def generate_prototypes():
    for module in modules:
        for direction in module.neighbors:
            if module.sockets[direction] == 0:
                continue
            for neighbor in modules:
                
                if module.sockets[direction] == neighbor.sockets[opposite_direction(direction)]:
                    module.neighbors[direction].append(neighbor)
                    
def opposite_direction(direction: str):
    match direction:      
        case "N": return "S"
        case "E": return "W"
        case "S": return "N"
        case "W": return "E"         
    
generate_prototypes()

for module in modules:
    print(module)
    print(module.neighbors)

