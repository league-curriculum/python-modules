
def setup():
    global bg, frog, cars
    
    # 1. Use the size(width, height) function to set the size of your sketch

    # 2. Initialize the 'bg' variable using the loadImage() function and the
    # "froggerBackground.png" image
    
    # 3. Use the bg variable's resize(width, height) method to set it's size
    # to the width and height of the sketch.
    
    # 4. Use the Frog class defined below to create a new frog and store it
    # in the 'frog' variable.
    # frog = Frog(x, y, width, height)
    
    # 5. Initialize the 'cars' variable to a list()
    #cars = list()
    
    # 6. Use the Car class defined below to create a new car
    # and store it in a variable.
    # *HINT* if speed is negative it moves left!
    #car = Car(x, y, length, speed)
    
    # 7. Call the cars.append() method and add the car that was
    # made in the previous step
    
    
def draw():
    pass
    # 8. Use the background() function to draw the bg variable
    # When you run the program do you see the background?
    
    # 9. Call the frog variable's draw() method to draw the frog.
    # When you run the program do you see the frog displayed?
    
    # 10. Use an if statement to check if a key is pressed by using the
    # keyPressed variable
        
        # 11. Use an if statement to check if the 'keyCode' variable is UP
            
            # 12. If key is UP, decrease the frog's y variable to move it up
            
        # 13. Make if statements for the LEFT, RIGHT, and DOWN keys
    
    
    # 14. Use a for loop to iterate through all the cars in the 'cars' list
    #for car in cars:
        
        # 15. Call each car's update() method
        
        # 16. Call each car's draw() method
        # When you run the program do you see the car?
        
    
    # 17. Use a for loop to iterate through all the cars in the cars list
    
        # 18. Use an if statement and the is_collision(frog, car) function
        # defined below
            
            # 19. If there's a collision, call the noLoop() function to
            # end the game

    
    # 20. Create more car objects of different lengths, speed, and size



# =================== DO NOT MODIFY THE CODE BELOW ======================

class Frog:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = loadImage("frog.png")
        self.image.resize(self.width, self.height)
        
    def draw(self):
        image(self.image, self.x, self.y)

class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.width = length
        self.height = length / 3
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.width, self.height)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.width
            
        if self.x < -self.width:
            self.x = width
            
def is_collision(frog, car):
    r1x = frog.x
    r1y = frog.y
    r1w = frog.width
    r1h = frog.height
    r2x = car.x
    r2y = car.y
    r2w = car.width
    r2h = car.height
    
    if (r1x + r1w >= r2x and
        r1x <= r2x + r2w and
        r1y + r1h >= r2y and
        r1y <= r2y + r2h):
        return True;

    return False;
