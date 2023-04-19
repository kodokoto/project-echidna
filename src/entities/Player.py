from entities.Entity import Entity
import pygame
from graphics.Animation import Animation
from graphics.Assets import Assets
from systems import coordinates
from config import screen

class Player(Entity):
    
    def __init__(self, x, y):
        super().__init__(Assets.player_right[0], x, y)
        self.animation = Animation(100)
        # modify bounding box
        self.width /= 2
        # self.x - self.width / 2

    def update(self):
        _input = pygame.key.get_pressed()
        if _input[pygame.K_w]:
            self.animation.update()
            if self.is_colliding_with_tiles():
                self.y += 10
                return 
            else:
                self.y -= 2
            
        if _input[pygame.K_s]:
            self.animation.update()
            if self.is_colliding_with_tiles():
                self.y -= 10
                return 
            else:
                self.y += 2
        if _input[pygame.K_a]:
            self.animation.update()
            if self.is_colliding_with_tiles():
                self.x += 10
                return 
            else:
                self.x -= 2
        if _input[pygame.K_d]:
            self.animation.update()
            if self.is_colliding_with_tiles():
                self.x -= 10
                return 
            else:
                self.x += 2

    def render(self):
        screen.blit(self.get_frame(), (self.x, self.y))
        pygame.draw.rect(screen, (0, 0, 255), self.model, 1)

    def get_frame(self):
        _input = pygame.key.get_pressed()
        if _input[pygame.K_w]:
            return self.animation.get_current_frame(Assets.player_up)
        elif _input[pygame.K_a]:
            return self.animation.get_current_frame(Assets.player_left)
        elif _input[pygame.K_d]:
            return self.animation.get_current_frame(Assets.player_right)
        elif _input[pygame.K_s]:
            return self.animation.get_current_frame(Assets.player_down)
        else:
            return self.animation.get_current_frame(Assets.player_idle)
