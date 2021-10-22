from Ghost import Ghost
from Lightning import Lightning
from Pumpkin import Pumpkin
from Rain import Rain
from Spotlight import Spotlight

def setup():
    pass
    # START HERE!
    #
    # Set the size of your sketch to at least 600, 400 using
    # the size() method.
    

    # Make a global variable for the scary house background
    #  example: global scary_house
    
  
    # Pick a scary house and initialize it using loadImage,
    #  example: scary_house = loadImage("scaryHouse1.jpg")
    
  
    # Resize your scary house to the window size using
    #  scary_house.resize(width, height)
    
  
    # DRAWING THE SCARY HOUSE
    #
    # In the draw function below, call draw_background() with your
    # scary house as an input parameter
    # Do you see your scary house??
  
    # DRAWING THE PUMPKINS
    #
    # Create a global variable for a pumpkin
    # then initialize it to a new Pumpkin(x, pumpkin_color)
    #   example: global pumpkin
    #            pumpkin = Pumpkin(350, '#E26238')
  
    # In the draw function below, call the pumpkin's draw() method
    # Do you see your pumpkin?
  
    # DRAWING THE GHOSTS
    #
    # Create a global variable for a ghost
    # then initialize it to a new Ghost(y, speed, flying_direction)
    #   example: global ghost
    #            ghost = Ghost(50, 5, "right")
  
    # In the draw function below, call the ghost's draw() method
    # Do you see your ghost?
  
    # DRAWING THE LIGHTNING
    #
    # Create a global variable for the lightning
    # then initialize it to new Lightning()
    #   example: global lightning
    #            lightning = Lightning()
  
    # In the draw function below, call the lightnings's draw()
    # method ONLY when the mouse is pressed
    # Do you see the lightning?
  
    # DRAWING THE SPOTLIGHT
    #
    # Create a new global variable for the spotlight
    # then initialize it to new Spotlight()
    #   example: global spotlight
    #            spotlight = Spotlight()


def draw():
    pass
    # Draw the background, pumpkins, ghosts, etc. below!
    
    
    
    # DRAWING THE HAPPY HALLOWEEN MESSAGE!
    # Display "Happy Halloween" somewhere on your display.
    # *hint* you can use text(), textSize(), and fill()

  
    # Try out the other scary house backgrounds and customize
    # your scary house!
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    # There are hidden spotlight and grayscale features in this
    # recipe. See if you can figure out how to use them...
  
    # ---------------------------------------------------------
    # Here are some other methods you can try:
    #  pumpkin.set_pumpkin_color()
    #  pumpkin.bounce()
    #  pumpkin.stop()
    #  pumpkin.move_right()
    #  pumpkin.move_left()
    #  ghost.set_ghost_transparency()
    #  lightning.set_lightning_flash()
    #  rainfall.set_amount_of_rain()
    #  spotlight.set_pixel_size()
    #  spotlight.set_size()
    # ---------------------------------------------------------

def draw_background(bg_image):
    background(bg_image)
    draw_floor()


def draw_floor():
    floor_height = 30
  
    push()
  
    fill(10, 10, 30)
    rect(0, height - floor_height, width, floor_height)
  
    pop()


# Call this method at the very bottom of the draw() method!
def draw_grayscale(grayscale_enabled):
    if grayscale_enabled:
        filter( GRAY )
