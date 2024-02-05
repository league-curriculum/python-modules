class Ring():
    def __init__(self, x, y, radius=100, speed=5):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_speed = speed
        
    def update(self):
        self.x += self.x_speed
        
        if self.x > width or self.x < 0:
            self.x_speed = -self.x_speed
        
    def draw(self):
        push()
        noFill()
        stroke(0)
        for i in range(50):
            ring_size = 2 * self.radius - (10 * i)
            ellipse(self.x, self.y, ring_size, ring_size)
        pop()
