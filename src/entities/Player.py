from entities.Entity import Entity
import pygame
from graphics.Animation import Animation
from graphics.Assets import Assets

class Player:
    
    def __init__(self, x, y):
        # super().__init__(self, x, y)
        self.x = x
        self.y = y
        # _input = pygame.key.get_pressed()
        self.animation = Animation(100)


    def update(self):
        _input = pygame.key.get_pressed()
        if _input[pygame.K_w]:
            self.animation.update()
            self.y -= 2
        if _input[pygame.K_s]:
            self.animation.update()
            self.y += 2
        if _input[pygame.K_a]:
            self.animation.update()
            self.x -= 2
        if _input[pygame.K_d]:
            self.animation.update()
            self.x += 2

    def render(self):
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
