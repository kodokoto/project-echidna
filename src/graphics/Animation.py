import pygame

class Animation:

    def __init__(self, speed):
        self.index = 0
        self.speed = speed
        self.previous_time = pygame.time.get_ticks()
        

    def update(self):
        current_time = pygame.time.get_ticks() 

        if current_time - self.previous_time >= self.speed:
            self.index += 1
            self.previous_time = current_time
            if self.index >= 4:
                self.index = 0
    
    def get_current_frame(self, frames):
        return frames[self.index]
