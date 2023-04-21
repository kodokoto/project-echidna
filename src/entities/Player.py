import pygame
from entities.Entity import Entity
from graphics.Assets import Assets
from systems import coordinates
from config import screen, debug
import config

class Player(Entity):
    
    def __init__(self, x, y):
        self.animation_count = 0
        self.direction = "SE"
        self.action = "idle"
        self.animation_speed = 4
        self.vel = 0
        
        Entity.__init__(self, self.get_frame(), 1, 1, x, y, 0, True)
        self.mask = None
    
    def handle_move(self, dx, dy):
        self.move( dx, dy)
        if self.is_colliding():
            self.move(-dx, -dy)
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def jump(self):
        self.z += self.vel 
        
    def fall(self):
        self.z -= self.vel
        
    def die(self):
        self.reset()
        
    def reset(self):
        self.animation_count = 0
        self.direction = "SE"
        self.action = "idle"
        self.vel = 0
        self.x, self.y = config.world.midpoint
        self.z = 0

    def update(self):
        self.mask = pygame.mask.from_surface(self.surface)
        _input = pygame.key.get_pressed()
        self.old_direction = self.direction
        
        # if we arent falling or jumping, we assume we're running
        if not self.action == "jump" and not self.action == "fall":
            self.action = "run"
            self.vel = 2
        
        # if we are pressing space, we jump
        if _input[pygame.K_SPACE] and self.action != "jump" and self.action != "fall":
            self.action = "jump"
            self.vel = 4
        
        # If we are above 32, we have reached the top of our jump, and we start falling
        if self.z >= 32:
            self.action = "fall"
        
        # else if we are at ground level, we stop falling and start idling
        elif self.z <=0 and self.action == "fall" and self.is_on_floor():
            self.action = "idle"
            self.direction = "SE"
            self.vel = 0
        
        if not self.is_on_floor():
            self.action = "fall"
            self.vel = 6
            
        if self.z <= -250:
            self.die()
        
        if self.action == "jump":
            self.jump()
        elif self.action == "fall":
            self.fall()
        
        # 8 directions + idle
        if _input[pygame.K_w] and _input[pygame.K_a]:
            self.direction = "W"
            self.handle_move(-self.vel, 0)
        elif _input[pygame.K_w] and _input[pygame.K_d]:
            self.direction = "N"
            self.handle_move(0, -self.vel)
        elif _input[pygame.K_s] and _input[pygame.K_a]:
            self.direction = "S"
            self.handle_move(0, self.vel)
        elif _input[pygame.K_s] and _input[pygame.K_d]:
            self.direction = "E"
            self.handle_move(self.vel, 0)
        elif _input[pygame.K_w]:
            self.direction = "NW"
            self.handle_move(-self.vel, -self.vel)
        elif _input[pygame.K_a]:
            self.direction = "SW"
            self.handle_move(-self.vel//2, self.vel//2)
        elif _input[pygame.K_d]:
            self.direction = "NE"
            self.handle_move(self.vel//2, -self.vel//2)
        elif _input[pygame.K_s]:
            self.direction = "SE"
            self.handle_move(self.vel, self.vel)
        elif not self.action == "jump" and not self.action == "fall":
            self.action = "idle" 
            self.direction = "SE"
            self.vel = 0           
            
        # increment animation if direction is the same
        # else reset animation
        if self.old_direction != self.direction or self.action == "jump" or self.action == "fall":
            self.animation_count = 0
        else:
            self.animation_count += 1
        
        print(self.z)
        print(self.is_on_floor())
        print(f'velocity: {self.vel}')
        print(f'action: {self.action}')
            
    def is_colliding(self):
        
        collision_box = self.rect.copy()
        collision_box.width = 16
        collision_box.height = 16
        collision_box.center = collision_box.topleft
        
        for entity in config.world.entities + config.world.tilemap.tiles:
            if entity.collides_with(collision_box) and entity.isSolid:
                return True
        return False
    
    def centered_projection(self):
        width = self.surface.get_width()
        height = self.surface.get_height()
        new_rect = pygame.Rect(*coordinates.project(self.x, self.y, self.z), width, height)
        new_rect.midbottom = new_rect.topleft
        new_rect.y += height//4
        return new_rect
            
    def render(self):
        self.surface = self.get_frame()
        screen.blit(self.surface, self.centered_projection())
        
        if debug:
            debug_rect = self.rect.copy()
            debug_rect.width = 3
            debug_rect.height = 3
                        
            pygame.draw.rect(screen, (0, 0, 255), self.centered_projection(), 1)
            pygame.draw.rect(screen, (255, 0, 0), debug_rect, 1)
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 1)
                
    def get_frame(self):
        
        match self.action:
            case "run" |  "jump" | "fall": 
                frames = Assets.player[f'{"run"} {self.direction}']
            case _:
                frames = Assets.player[f'{self.action}']
        
        return frames[self.animation_count // self.animation_speed % len(frames)]