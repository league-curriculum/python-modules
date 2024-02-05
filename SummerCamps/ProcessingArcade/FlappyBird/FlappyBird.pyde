"""
Create the classic Flappy Bird game!
"""

def setup():
    pass
    # 1. Use the size(width, height) function to set the width and height
    # of the game window
    size(800, 600)
    
    # 2. Remove the comment (the '#') in the line below 
    global bg, bird, lower_pipe, upper_pipe
    
    # 3. Use the loadImage function to inialize the bg variable with the
    # flappyBackground.jpg image
    bg = loadImage("flappyBackground.jpg") 
    
    # 4. Use the bg variable's resize(width, height) method to set
    # the background to the width and height of the game window
    bg.resize(width, height)
    
    # 5. Use the Bird class defined below to create a Bird object.
    bird = Bird('bird.png', 100, height/2)
    
    # 6. Initialize the 'lower_pipe' and 'upper_pipe' variables using
    # the Pipe class defined below.
    # The pipe images are named, "upper_pipe.png" and "lower_pipe.png"
    upper_pipe = Pipe('upper_pipe.png')
    lower_pipe = Pipe('lower_pipe.png')

    # 7. Call the reset_pipes(lower_pipe, upper_pipe) function to set
    # the initial positions of the pipes
    reset_pipes(lower_pipe, upper_pipe)


def draw():
    # 8. Use the background() function to draw the game's background
    background(bg)

    # 9. Find the Bird class below and follow the instructions
    # there to complete the Bird class before continuing

    # 16. Call the bird's update and draw methods.
    # Is the bird displayed and move up when the mouse is clicked?
    bird.update()
    bird.draw()
    
    # 17. Call the upper and lower pipe's update methods.
    upper_pipe.update()
    lower_pipe.update()
    
    # 18. Call the upper and lower pipe's draw methods. 
    # Do the pipes move across the screen?
    upper_pipe.draw()
    lower_pipe.draw()

    # 19. Call the reset_pipes function defined below when the pipes
    # move past the screen (lower_pipe.x < 0) to reset their position.
    if upper_pipe.x < 0 and lower_pipe.x < 0:
        reset_pipes(lower_pipe, upper_pipe)

    # 20. Use an if statement along with the intersects_pipes() function
    # defined below to check if the bird collided with one of the pipes.
    # If there's a collision, stop the game by calling noLoop()
    if intersects_pipes(bird, lower_pipe, upper_pipe):
        noLoop()
    
    # 21. End the game if the bird flies too low (hitting the ground)
    # OR flies too high (above the screen)
    if bird.y > height or bird.y < 0:
        noLoop()
        
        
    # *** ENHANCEMENTS ***
    # * Change the bird image to something else!
    # * Add a score that increments every time the bird gets through the pipes.
    # * Add a way to reset the game when it's over.
    # * Make the pipes move faster the longer the game goes.

class Bird:
    def __init__(self, image_file, bird_x, bird_y):
        self.x = bird_x
        self.y = bird_y
        self.width = 50
        self.height = ( 3 * self.width ) / 4
        self.image = loadImage(image_file)
        self.image.resize(self.width, self.height)
        
        # 10. Remove the 'None' and pick a new value for the bird gravity,
        # typically a value of 1 to 5
        self.gravity = 2
        
        # 11. Remove the 'None' and pick a new value for the bird flap_height
        # typically a value at least double the gravity 
        self.flap_height = 6
        
    def update(self):
        pass
        # 13. Move the bird downward by the gravity member variable to make
        # it look like the bird is falling
        self.y += self.gravity
        
        # 14. Use an if statement and the mousePressed variable to flap (jump)
        # the bird up by flap distance member variable the when the mouse is pressed
        if mousePressed:
            self.y -= self.flap_height
    
    def draw(self):
        pass
        # 15. Use the image function and the class's member variables to
        # draw the bird
        # image( <image>, <x positon>, <y position> )
        image(self.image, self.x, self.y)
        


# =================== DO NOT MODIFY THE CODE BELOW ======================

class Pipe:
    pipe_gap = 125
    
    def __init__(self, image_file, pipe_y=0, pipe_height=0):
        self.x = width
        self.y = pipe_y
        self.width = 50
        self.height = pipe_height
        self.image = loadImage(image_file)
        self.image.resize(self.width, self.height)
    
    def update(self):
        self.x -= 3
    
    def draw(self):
        image(self.image, self.x, self.y)

    def teleport(self, pipe_y, pipe_height):
        self.x = width
        self.y = pipe_y
        self.height = pipe_height
        self.image.resize(self.width, self.height)
        

def reset_pipes(lower_pipe, upper_pipe):
    random_height = int((2 * random(height) / 3) + 50)
    upper_pipe.teleport(0, random_height)
    lower_pipe.teleport(random_height + Pipe.pipe_gap, height - random_height)
    
    
def intersects_pipes(bird, lower_pipe, upper_pipe):
    # Check upper pipe collision
    if (bird.x + bird.width >= upper_pipe.x and
        bird.x <= upper_pipe.x + upper_pipe.width and
        bird.y + bird.height >= upper_pipe.y and
        bird.y <= upper_pipe.y + upper_pipe.height):
        return True

    # Check lower pipe collision
    if (bird.x + bird.width >= lower_pipe.x and
        bird.x <= lower_pipe.x + lower_pipe.width and
        bird.y + bird.height >= lower_pipe.y and
        bird.y <= lower_pipe.y + lower_pipe.height):
        return True

    return False
