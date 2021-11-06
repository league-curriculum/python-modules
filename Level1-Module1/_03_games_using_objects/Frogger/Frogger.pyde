
def setup():
    pass
    # 1. Use the size function to set the size of your sketch

    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    # global bg, frog
    # bg = loadImage("froggerBackground.png")
    
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    
def draw():
    pass
    # 4. Use the background function to draw the background
    
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.

    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in this draw function:
    # global frog_x, frog_y
    
    # 7. Complete the keyPressed() function below to make the frog move
    # when the UP, DOWN, LEFT, and RIGHT keys are pressed.
    
    # 8. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    
    # 9. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
    
    # 10. Create more car objects of different lengths, speed, and size

def keyPressed():
    global frog_x, frog_y
    if key == CODED:
        if keyCode == UP:
            # Frog Y position goes up
            print("up")
        elif keyCode == DOWN:
            # Frog Y position goes down
            print("down")
        elif keyCode == RIGHT:
            # Frog X position goes right
            print("right")
        elif keyCode == LEFT:
            # Frog X position goes left
            print("left")

class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
