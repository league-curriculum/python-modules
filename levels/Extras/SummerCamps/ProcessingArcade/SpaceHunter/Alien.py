class Alien:
    arc_speed = 1.05          # makes the aliens move faster
    collision_radius = 100    # bigger => easier to hit
     
    alien1 = alien2 = alien3 = alien4 = alien5 = alien_types = None
    images_initialized = False
    
    @staticmethod
    def initialize_images():
        if Alien.images_initialized:
            return
        
        Alien.alien1 = loadImage("ufo1.png")
        Alien.alien2 = loadImage("ufo2.png")
        Alien.alien3 = loadImage("ufo3.png")
        Alien.alien4 = loadImage("ufo4.png")
        Alien.alien5 = loadImage("ufo5.png")
        
        Alien.alien1.resize(200, 157)
        Alien.alien2.resize(250, 199)
        Alien.alien3.resize(200, 108)
        Alien.alien4.resize(157, 200)
        Alien.alien5.resize(150, 124)
        
        Alien.alien_types = (Alien.alien1, Alien.alien2, Alien.alien3,
                              Alien.alien4, Alien.alien5)
    
    def __init__(self, alien_type=None, speed=None):
        if alien_type is None:
            alien_type = int(random(1, 5))
            
        self.image = Alien.alien_types[alien_type]
        self.speed = speed
        self.x_speed = None
        self.y_speed = None
        self.move_direction = None
        self.move_pattern = None
        self.is_alive = True
        
        # Don't start near edges, alien should pass through middle of screen
        largest_alien_width = 250
        largest_alien_height = 200
        self.x = random(largest_alien_width, width - largest_alien_width)
        self.y = random(largest_alien_height, height - largest_alien_height)
        
        # Random spawn side                
        rand = random(100)
        if rand < 25.0:
            self.move_direction = 'right'
            self.x = -largest_alien_width
            self.x_speed = int(random(1, 5))
            self.y_speed = int(random(1, 2)) if self.y < height/2 else int(random(-2, -1))
        elif rand < 50.0:
            self.move_direction = 'left'
            self.x = width + largest_alien_width
            self.x_speed = int(random(-5, -1))
            self.y_speed = int(random(1, 2)) if self.y < height/2 else int(random(-2, -1))
        elif rand < 75.0:
            self.move_direction = 'down'
            self.y = - largest_alien_height
            self.y_speed = int(random(1, 5))
            self.x_speed = int(random(1, 2)) if self.x < width/2 else int(random(-2, -1))
        else:
            self.move_direction = 'up'
            self.y = height + largest_alien_height
            self.y_speed = int(random(-5, -1))
            self.x_speed = int(random(1, 2)) if self.x < width/2 else int(random(-2, -1))
            
        # Random movement pattern
        rand = random(100)
        if rand < 50.0:
            self.move_pattern = 'linear'
        else:
            self.move_pattern = 'arc'
    
    def move(self):
        if self.move_pattern == 'arc':
            self.x_speed *= Alien.arc_speed
            self.y_speed *= Alien.arc_speed
            
        x_dir = self.x_speed
        y_dir = self.y_speed
        
        # Ensure alien moves across the screen
        if self.move_direction == 'left':
            x_dir = -self.speed
        elif self.move_direction == 'right':
            x_dir = self.speed
        elif self.move_direction == 'up':
            y_dir = -self.speed
        elif self.move_direction == 'down':
            y_dir = self.speed

        self.x += x_dir
        self.y += y_dir
       
        # Check out of bounds
        largest_alien_width = 250
        largest_alien_height = 200
        if (self.x < -largest_alien_width or
            self.x > width + largest_alien_width or
            self.y < -largest_alien_height or
            self.y > height + largest_alien_height):
            self.is_alive = False
    
    def draw(self):
        image(self.image, self.x, self.y)
        
