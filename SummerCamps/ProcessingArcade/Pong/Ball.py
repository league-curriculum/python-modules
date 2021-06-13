from Paddle import Paddle

color_progression = ['#FFFFFF', '#FFFF00', '#FFFA00', '#FF0000',
                     '#800080', '#0000FF']

class Ball():
    def __init__(self, x=0, y=0, ball_speed=5, radius=20):
        self.x = x
        self.y = y
        self.speed = ball_speed
        self.radius = radius
        self.color_index = 0
        self.ball_color = color_progression[self.color_index]
        self.x_speed = random(-self.speed, self.speed)
        self.y_speed = self.speed
        self.currently_intersects = False
        
    def update(self):
        if self.x + self.radius > width or self.x - self.radius < 0:
            self.x_speed = -self.x_speed
            
        if self.y + self.radius < self.radius:
            self.y_speed = -self.y_speed
            
        self.x += self.x_speed
        self.y += self.y_speed
        
    def draw(self):
        push()
        
        strokeWeight(5)
        if self.color_index >= len(color_progression):
            fill(random(255), random(255), random(255))
        else:
            fill(color_progression[self.color_index])
        ellipse(self.x, self.y, 2 * self.radius, 2 * self.radius)
        
        pop()

    def collision(self, paddle):
        side = None

        # Temporary variables to set edges for testing
        edge_x = self.x
        edge_y = self.y

        if self.x < paddle.x:
            edge_x = paddle.x                  # Ball is left of the paddle
            side = 'left'
        elif self.x > paddle.x + paddle.width:
            edge_x = paddle.x + paddle.width   # Ball is right of the paddle
            side = 'right'
        if self.y < paddle.y:
            edge_y = paddle.y                  # Ball is above the paddle
            side = 'top'
        elif self.y > paddle.y + paddle.height:
            edge_y = paddle.y + paddle.height  # Ball is below the paddle
            side = 'bottom'

        # Get distance from pythagoream theorem
        dist_x = self.x - edge_x
        dist_y = self.y - edge_y
        distance = sqrt( (dist_x * dist_x) + (dist_y * dist_y) )

        # If the distance is less than the radius, collision!
        if distance <= self.radius:
            if not self.currently_intersects:
                self.currently_intersects = True
    
                self.x_speed += 2
                self.y_speed += 2
                
                if self.color_index < len(color_progression):
                    self.ball_color = color_progression[self.color_index]
    
                self.color_index += 1
    
                if side == 'right' or side == 'left':
                    self.x_speed = -self.x_speed
                else:
                    self.y_speed = -self.y_speed
        else:
            # Sometimes upon first collision the ball would still be within
            # the paddle, causing the ball to rebound back and forth.
            # Resetting the variable here ensures there's only 1 change of
            # direction until the ball and paddle no longer intersect 
            self.currently_intersects = False
