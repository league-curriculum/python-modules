from Ghost import Ghost
from Lightning import Lightning
from Pumpkin import Pumpkin
from Rain import Rain
from Spotlight import Spotlight

global gray
gray = False

def setup():
    # START HERE!
    #
    # Set the size of your sketch to at least 600, 400 using
    # the size() method.
    size(800, 600)

    # Make a global variable for the scary house background
    #  example: global scary_house
    global scary_house
  
    # Pick a scary house and initialize it using loadImage,
    #  example: scary_house = loadImage("scaryHouse1.jpg")
    scary_house = loadImage("scaryHouse1.jpg");
  
    # Resize your scary house to the window size using
    #  scary_house.resize(width, height);
    scary_house.resize(width, height)
  
    # DRAWING THE SCARY HOUSE
    #
    # In the draw function below, call draw_background() with your
    # scary house as an input parameter
    # Do you see your scary house??
  
    # DRAWING THE PUMPKINS
    #
    # Create a new variable for a pumpkin at the top of this sketch
    # then initialize it to a new Pumpkin(x, pumpkinColor)
    #   example: pumpkin = Pumpkin(350, '#E26238')
    global pumpkin1, pumpkin2, pumpkin3
    pumpkin1 = Pumpkin(350, '#E26238')
    pumpkin2 = Pumpkin(550, '#BE1DF0')
    pumpkin3 = Pumpkin(850, '#1DF029')
  
    # In the draw function below, call the pumpkin's draw() method
    # Do you see your pumpkin?
  
    # DRAWING THE GHOSTS
    #
    # Create a new variable for a ghost at the top of this sketch
    # then initialize it to a new Ghost(y, speed, flying_direction)
    #   example: ghost = Ghost(50, 5, "right")
    global ghost1, ghost2, ghost3
    ghost1 = Ghost(50, 5, "right")
    ghost2 = Ghost(100, 3, "right")
    ghost3 = Ghost(150, 8, "left")
  
    # In the draw function below, call the ghost's draw() method
    # Do you see your ghost?
  
    # DRAWING THE RAIN
    #
    # Create a new variable for the rain at the top of this sketch
    # then initialize it to new Rain(color)
    #   example: rainfall = new Rain('#ADD8E6')
    global rainfall
    rainfall = Rain('#ADD8E6')
  
    # In the draw function below, call the rain's draw() method
    # Do you see rain falling?
  
    # DRAWING THE LIGHTNING
    #
    # Create a new variable for the lightning at the top of this
    # sketch then initialize it to new Lightning()
    #   example: lightning = Lightning()
    global lightning
    lightning = Lightning()
  
    # In the draw function below, call the lightnings's draw()
    # method ONLY when the mouse is pressed
    # Do you see the lightning?
  
    # DRAWING THE SPOTLIGHT
    #
    # Create a new variable for the spotlight at the top of this
    # sketch then initialize it to new Spotlight()
    #   example: spotlight = Spotlight()
    global spotlight
    spotlight = Spotlight()


def draw():
    draw_background(scary_house)
  
    pumpkin1.draw()
    pumpkin2.draw()
    pumpkin3.draw()
  
    ghost1.draw()
    ghost2.draw()
    ghost3.draw()
  
    #rainfall.draw()
  
    # DRAWING THE HAPPY HALLOWEEN MESSAGE!
    # Display "Happy Halloween" somewhere on your display.
    # *hint* you can use text(), textSize(), and fill()
    textSize(70)
    fill('#08FF3F')
    text("HAPPY HALLOWEEN!", 50, 300)
  
    if mousePressed:
        if mouseButton == LEFT:
            lightning.draw()
        if mouseButton == RIGHT:
            spotlight.draw()
  
    if keyPressed:
        if keyCode == LEFT:
            pumpkin1.move_left(5)
        elif keyCode == RIGHT:
            pumpkin1.move_right(5)
        elif keyCode == UP:
            pumpkin1.bounce()
        elif keyCode == DOWN:
            pumpkin1.stop()
    
        if key == 'g':
            global gray
            gray = not gray
        elif key == 'a':
            spotlight.set_size(spotlight.get_size() + 3)
        elif key == 's':
            spotlight.set_size(spotlight.get_size() - 3)
  

    if gray:
        draw_grayscale(True)

  
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
