from config import SCREEN_WIDTH, SCREEN_HEIGHT

def process(x, y, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT):
    return center_coordinates(*cartesian_to_isometric(x, y), screen_width, screen_height)

def cartesian_to_isometric(x, y):
    return (x - y, (x + y) / 2)

def center_coordinates(x, y, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT):
    return (x + screen_width / 2, y + screen_height / 2)
