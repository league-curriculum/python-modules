class Pumpkin:
    
    def __init__(self, x, pumpkin_color):
        self.x = x
        self.y = height - 300
        self.x_speed = 0
        self.bouncing = False
        self.bounce_height = 30
        self.bounce_speed = 0
        self.gravity = 1
        self.pumpkin_color = pumpkin_color
        self.size_pixels = 150
        self.glowing_eyes_color = color(240 + random(15), 240 + random(15), random(255))
        self.green_stem_color = '#2EA22C'
  
    def bounce(self):
        self.bouncing = True

    def stop(self):
        self.bouncing = False
        self.x_speed = 0
  
    def move_right(self, speed):
        self.x_speed = speed
  
    def move_left(self, speed):
        self.x_speed = -speed

    def set_pumpkin_color(new_color):
        self.pumpkin_color = new_color

    def draw(self):
        push()

        if self.bounce_speed < self.bounce_height:
            self.bounce_speed += self.gravity
    
        self.y += self.bounce_speed

        if self.y > height - 100:
            self.y = height - 100

            if self.bouncing:
                self.bounce_speed = -self.bounce_speed
    
        self.x += self.x_speed
    
        if self.x > width + self.size_pixels:
            self.x = 0 - self.size_pixels

        if self.x < 0 - self.size_pixels:
            self.x = width

        ellipseMode(CENTER)

        # Black outline
        stroke(0)
        strokeWeight(2)

        # Draw top stem
        fill(self.green_stem_color)
        rect(self.x - 10, self.y - (self.size_pixels / 2) - 20, 15, 20)

        # Draw body
        fill(self.pumpkin_color)
        ellipse(self.x, self.y, self.size_pixels, self.size_pixels)

        # Set glowing eyes
        fill(self.glowing_eyes_color, random(200) + 50 )  

        # Draw eyes
        triangle(self.x-30, self.y-20, self.x-20, self.y, self.x-40, self.y)
        triangle(self.x+30, self.y-20, self.x+20, self.y, self.x+40, self.y)
        triangle(self.x, self.y, self.x+10, self.y+20, self.x-10, self.y+20)

        # Draw shadow
        ellipse(self.x, height - 15, (150 * self.y) / height, (10 * self.y) / height)

        # Draw mouth
        arc(self.x, self.y + 30, 80, 80, 0, PI, 0)
        line(self.x - 40, self.y + 30, self.x + 40, self.y + 30)

        # Draw tooth  
        fill(self.pumpkin_color)
        rect(self.x + 10, self.y + 30, 10, 15)

        # Clear the top outline of the tooth
        strokeWeight(3)
        stroke(self.pumpkin_color)
        fill(self.pumpkin_color)
        line(self.x + 12, self.y + 30, self.x + 17, self.y + 30)

        pop()
