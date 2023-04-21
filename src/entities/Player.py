import pygame
from graphics.Assets import Assets
from graphics.Visible import Visible
from systems import coordinates
from config import screen, debug
import config

class Player(Visible):
    
    def __init__(self, x, y):
        self.animation_count = 0
        self.direction = "E"
        self.action = "idle"
        self.animation_speed = 4
        Visible.__init__(self, self.get_frame(), 1, 1, x, y)
        self.mask = None
    
    def handle_move(self, dx, dy):
        self.move( dx, dy)
        if self.is_colliding():
            self.move(-dx, -dy)
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def update(self):
        self.mask = pygame.mask.from_surface(self.surface)
        _input = pygame.key.get_pressed()
        
        self.action = "run"   
        self.old_direction = self.direction
        
        # 8 directions + idle
        if _input[pygame.K_w] and _input[pygame.K_a]:
            self.direction = "W"
            self.handle_move(-2, 0)
        elif _input[pygame.K_w] and _input[pygame.K_d]:
            self.direction = "N"
            self.handle_move(0, -2)
        elif _input[pygame.K_s] and _input[pygame.K_a]:
            self.direction = "S"
            self.handle_move(0, 2)
        elif _input[pygame.K_s] and _input[pygame.K_d]:
            self.direction = "E"
            self.handle_move(2, 0)
        elif _input[pygame.K_w]:
            self.direction = "NW"
            self.handle_move(-2, -2)
        elif _input[pygame.K_a]:
            self.direction = "SW"
            self.handle_move(-1, 1)
        elif _input[pygame.K_d]:
            self.direction = "NE"
            self.handle_move(1, -1)
        elif _input[pygame.K_s]:
            self.direction = "SE"
            self.handle_move(2, 2)
        elif _input[pygame.K_SPACE]:
            self.z += 32
        else:
            self.action = "idle"
        
        # increment animation if direction is the same
        # else reset animation
        if self.old_direction != self.direction:
            self.animation_count = 0
        else:
            self.animation_count += 1
            
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
        if self.action == "run":
            frames = Assets.player[f'{self.action} {self.direction}']
        else:
            frames = Assets.player[f'{self.action}']
        
        return frames[self.animation_count // self.animation_speed % len(frames)]