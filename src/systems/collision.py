import pygame

def check_bounds(rect1: pygame.Rect, rect2: pygame.Rect) -> bool:
    return rect1.colliderect(rect2)