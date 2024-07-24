class Shot:
    initial_width = 100
    collision_radius = 10
    
    def __init__(self):
        self.x = mouseX
        self.y = mouseY
        self.width = Shot.initial_width
        self.speed = 35
        self.is_alive = True
        
    def draw(self):
        if self.width > 0:
            push()
        
            fill(0, 230, 230)
            stroke(128, 0, 128)
            strokeWeight(2)
            circle(mouseX, mouseY, self.width)
            self.width -= self.speed
        
            pop()
        else :
            self.is_alive = False
