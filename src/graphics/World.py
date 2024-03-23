import math
from entities.Player import Player
from graphics.WorldMap import WorldMap
from systems.cardinal import get_opposite_direction

class World:

    def __init__(self):
        
        self.map = WorldMap()
        self.room = self.map.current_room()
        # self.room = Spawn(True)
        print([(d, r.name) for d, r in self.room.adj_rooms.items()])
        self.player = Player(*self.room.spawns[0])

    def update(self):
        self.room.update()
        self.player.update()
        # handle teleport collisions
        # self.check_for_teleport_collision()
            
    def render(self):
        sprites = []
        entities = self.room.entities.copy()
        tiles = self.room.tiles.copy()
        
        # if player is below floor, render player before tiles
        if self.player.is_below_floor():
            sprites.append(self.player)
        # else render player as an entity
        else:
            entities.append(self.player)

        # render tiles
        for tile in tiles:
            sprites.append(tile)
        
        # sort entetiesby distance from camera (origin)
        sprites.sort(key=lambda sprite: self.distance_from_origin(*sprite.rect.center), reverse=True)
        entities.sort(key=lambda sprite: self.distance_from_origin(*sprite.rect.center), reverse=True)
        
        # render entities in order
        for entity in entities:
            sprites.append(entity)
            
        # render sprites
        for sprite in sprites:
            sprite.render()
        
    def distance_from_origin(self, x, y):
        return math.sqrt((x - self.room.origin[0])**2 + (y - self.room.origin[1])**2)
    
    def check_for_teleport_collision(self):
        for teleport in [e for e  in self.room.get_teleports()]:
            if self.player.collides_with(teleport):
                self.handle_teleport_collision(teleport)
                break
            
    def handle_teleport_collision(self, teleport):
        self.map.move_to_room_by_direction(teleport.direction)
        self.room = self.map.current_room()
        print(self.room)
        n = self.room.get_teleport_by_direction(get_opposite_direction(teleport.direction))
        self.player.teleport_to(n.x, n.y)
