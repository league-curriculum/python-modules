class Ghost:
    def __init__(self, y, speed, direction):
        self.ghost_img = loadImage("ghost.png")
        self.ghost_img.resize(150, 250)
        self.x = random(0, width)
        self.y = y
        self.speed = 5
        self.direction = direction
        self.transparency = 125

    # 0 = most transparent; 100 = most opaque
    def set_ghost_transparency(self, transparency):
        # Normalize value from 0-255
        this.transparency = ( 255 - ( ( transparency * 255 ) / 100 ) )

    def draw(self):
        push()

        # Makes ghost transparent
        tint(255, self.transparency)
    
        if self.direction.lower() == 'left':
            # Ghost goes right to left
      
            # Flip on X axis
            scale(-1, 1)
            image(self.ghost_img, -self.x, self.y)
      
            self.x -= self.speed
      
            if self.x < -self.ghost_img.width:
                self.x = width + self.ghost_img.width
    
        else:
            # Ghost goes left to right
      
            image(self.ghost_img, self.x, self.y)
            
            self.x += self.speed
      
            if self.x > width:
                self.x = -self.ghost_img.width

        pop()
