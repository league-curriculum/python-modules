#
# This class will be used to represent each part of the moving snake.
#
class Segment:
    size = 20
    speed = size
    
    # Add a constructor with parameters to initialize x and y member variables
    def __init__(self, x, y, snake_color=color(255, 255, 255)):
        self.x = x
        self.y = y
        self.color = snake_color

    def draw(self):
        fill(self.color)
        rect(self.x, self.y, Segment.size, Segment.size )
