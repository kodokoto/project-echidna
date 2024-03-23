from enum import Enum
from graphics.World import World
from systems.cardinal import get_opposite_direction

class State(Enum):
    INGAME = 0,
    TELEPORTING = 1,
    MENU = 2
    GAMEOVER = 3,
    
class Game:
    def __init__(self):
        self.state = State.INGAME
        self.world = World()
        
    def set_state(self, state):
        self.state = state
        
    def get_state(self):
        return self.state
    
    def update(self):
        match self.state:
            case State.INGAME:
                self.ingame()
            case State.TELEPORTING:
                self.teleporting()
            case State.GAMEOVER:
                pass
            case _:
                raise ValueError("Invalid state")
            
    def render(self):
        self.world.render()
    
    def ingame(self):
        self.world.update()
        self.check_for_teleport_collision()
        
    def teleporting(self):
        self.world.update()
        
        if not any([e for e in self.world.room.get_teleports() if self.world.player.collides_with(e)]):
            self.set_state(State.INGAME)
          
    def check_for_teleport_collision(self):
        for teleport in [e for e  in self.world.room.get_teleports()]:
            if self.world.player.collides_with(teleport):
                self.handle_teleport_collision(teleport)
                break
            
    def handle_teleport_collision(self, teleport):
        self.world.map.move_to_room_by_direction(teleport.direction)
        self.world.room = self.world.map.current_room()
        n = self.world.room.get_teleport_by_direction(get_opposite_direction(teleport.direction))
        center = n.get_center()
        self.world.player.teleport_to(*center)
        self.set_state(State.TELEPORTING)
