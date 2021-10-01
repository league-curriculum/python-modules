global bg_color, sun_colors, sun_radius

sun_radius = 250
bg_color = color(31, 0, 48)

# RGB colors
sun_colors = [
  color(212, 202, 11), 
  color(214, 198, 30), 
  color(211, 170, 26), 
  color(216, 157, 51), 
  color(217, 124, 64), 
  color(213, 104, 81), 
  color(212, 51, 98), 
  color(215, 29, 121), 
  color(217, 11, 139), 
  color(217, 0, 151)
]

"""
*
* LOOK AT RetroSun.html IN THIS FOLDER to see what you will be creating!
*
"""

def setup():
    pass
    # TODO 1) Set the size of your sketch

    """
    * PART I: Drawing the sun
    * See 1st image 
    """

    # TODO 2) Draw the bg_color background color using the background() function
    
    # TODO 3) Draw an ellipse for the sun in the center of the window
    # Use fill(sun_colors[0]) to make it yellow
    # Use noStroke() to remove the black outline
    
    # Do you see a yellow sun like in the 1st image?
    # If not, fix your code before proceeding.
    
    """
    * PART II: Drawing a color gradient on the sun
    * See 2nd image
    *
    * This will make the sun have gradually different colors from the 
    * top to bottom
    """
    
    # Call the loadPixels() function to load the pixels list variable.
    
    # Loop through all the pixels in your window.
    # A pixel is a 1x1 square, so if your window width is 600 and the 
    # height is 400 (600x400), then there are 600 * 400 = 240,000 pixels
        
        # We want to change the color of our sun so use an if statement
        # to check if the pixel is the color of the yellow circle.
        # pixels[i] is the color of the pixel.
        # sun_colors[0] is the color of the sun.
            
            # If it's the same color we need to map the pixel to a
            # color in our sun_colors list (see 2nd gradient image)
       
            # The top of the sun is yellow (sun_colors[0]) and the bottom
            # of the sun is red (sun_colors[len(sun_colors) - 1]
            
            # In order to get the right color, the y value from the top of
            # the sun to the bottom has to be mapped to a range from 0 to 1.
            # Use the map() function to do that:
            # y = i / width
            # step = map(y, sun_top_y, sun_bottom_y, 0, 1)

            # Call interpolateColor(sun_colors, step) and save the color
            # variable that's returned into a variable
            
            # Set the pixel at pixels[i] to the color from the previous step


    # Call updatePixels() to apply the changes made to the pixels list


def draw():
    pass
    """
    * PART III: Drawing the missing sections at the bottom of the sun
    * See 3rd image
    *
    * The missing parts of the sun are created by drawing rectangles
    * over the sun with the same color as the background.
    """

    # Call updatePixels() to redraw the background and sun
    
    # Set the fill() color to bg_color

    # To draw each rectangle we need to find its x, y, width, height
    # *The y position can be any value within the sun:
    #   y = width / 2
    # *The height can be any value you choose:
    #   h = 40
    # *The x position can be the center of the sun's x position minus the radius:
    #   x = sun_center_x - sun_radius
    # * The width can be 2 times the radius
    #   w = 2 * sun_radius
   
    # Do you see a section missing from the sun like in the 3rd image?

    """
    * PART IV: Moving the missing sun sections
    *
    * To move a section upwards each rectangle's y value needs to decrease.
    * To make the section get smaller, its height needs to also decrease.
    """
   
    # Decrease the y variable of the rectangular section created in part III.
    # If there isn't a variable declare a variable OUTSIDE of the draw
    # function AND initialize it in the setup() function.
    # *HINT* You will have to put 'global y', where y is your variable,
    #        in setup() and draw()
   
    # Do you see the rectangle moving upwards?
    # See image 4
   
    # Pick a y positon to be the location when the sections stop moving up.
    # If the rectangle's y positon is above this, move the rectangle's
    # y position back to the bottom of the sun.

    # Does the rectangle move back to the bottom?
   
    # Decrease the the height of the rectangle as it moves upwards.
    # Similar to the y positon, a variable for the height needs to be
    # created if it doesn't already exist.

    # Adjust the amount to decrease so that it disappears close to the top.
    
    # Add code to reset the height of the rectangle when it moves back to
    # the bottom of the sun.
    # See image 5
   
    """
    * PART V: Moving more missing sun sections
    *
    * Using a loop to manage moving multiple missing sun sections 
    """
   
    # Figure out how to create the other missing sun sections using the
    # code you wrote for the 1 missing sun section.
    # *HINT* You can use the Rectangle class defined below to create
    #        a list of rectangles and a loop to iterate through each one.


    """
    * PART VI: Adding extras
    *
    * If you want to make your retro sun look more unique, try adding
    * reflections and stars.
    """    


# Variable step should be between 0 and 1, inclusive
def interpolate_color(color_list, step):
    sz = len(color_list)
  
    if sz == 1 or step <= 0.0:
        return color_list[0]
    elif step >= 1.0:
        return color_list[sz - 1]
  
    scl = step * (sz - 1)
    i = int(scl)
  
    return lerpColor(color_list[i], color_list[i + 1], scl - i)

# Feel free to use this class to create a list of missing
# sections in the sun, for example:
# sections = list()
# for i in range(5):
#     sections.append(Rectangle(x, y, w, h)) # Create your own x, y, w, h variables
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def draw(self):
        noStroke()
        fill(bg_color)
        rect(self.x, self.y, self.w, self.h)

    def update(self):
        self.y -= 1
        self.h -= 40.0 / (sun_radius + (sun_radius/4))
        
        if self.y < (height / 2) - (sun_radius / 4):
            self.y = (height / 2) + sun_radius
            self.h = 40
