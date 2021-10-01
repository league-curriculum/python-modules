global bg_color, sun_colors, sun_radius, y, h

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
    size(800, 800)

    """
    * PART I: Drawing the sun
    * See 1st image 
    """

    # TODO 2) Draw the bg_color background color using the background() function
    background(bg_color)
    
    # TODO 3) Draw an ellipse for the sun in the center of the window
    # Use fill(sun_colors[0]) to make it yellow
    # Use noStroke() to remove the black outline
    noStroke()
    fill(sun_colors[0])
    ellipse(width/2, height/2, 2*sun_radius, 2*sun_radius)
    
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
    loadPixels()
    
    # Loop through all the pixels in your window.
    # A pixel is a 1x1 square, so if your window width is 600 and the 
    # height is 400 (600x400), then there are 600 * 400 = 240,000 pixels
    for i in range(width * height):
        
        # We want to change the color of our sun so use an if statement
        # to check if the pixel is the color of the yellow circle.
        # pixels[i] is the color of the pixel.
        # sun_colors[0] is the color of the sun.
        if pixels[i] == sun_colors[0]:
            
            # If it's the same color we need to map the pixel to a
            # color in our sun_colors list (see 2nd gradient image)
       
            # The top of the sun is yellow (sun_colors[0]) and the bottom
            # of the sun is red (sun_colors[len(sun_colors) - 1]
            
            # In order to get the right color, the y value from the top of
            # the sun to the bottom has to be mapped to a range from 0 to 1.
            # Use the map() function to do that:
            # y = i / width
            # step = map(y, sun_top_y, sun_bottom_y, 0, 1)
            step = map(i / width, (height/2) - sun_radius, (height/2) + sun_radius, 0, 1)

            # Call interpolateColor(sun_colors, step) and save the color
            # variable that's returned into a variable
            c = interpolate_color(sun_colors, step)
            
            # Set the pixel at pixels[i] to the color from the previous step
            pixels[i] = c


    # Call updatePixels() to apply the changes made to the pixels list
    updatePixels()


    global rectangles, num_rectangles
    rectangles = list()

    num_rectangles = 5
    h = 1
    w = 2 * sun_radius
    x = (width/2) - sun_radius
    y = (height/2) - (sun_radius/4)
    
    y_increment = (sun_radius + (sun_radius/4)) / num_rectangles 
    
    for i in range(num_rectangles):
        rectangles.append(Rectangle(x, y, w, h))
        
        y += y_increment
        h = map(y, (height/2) - (sun_radius/4), (height/2) + sun_radius, 1, 40)


    global ref
    ref = Reflection(sun_radius, 4, (width/2) - sun_radius, (height/2) + sun_radius, 1)
    
    global stars
    stars = list()
    for i in range(100):
        stars.append(Star(random(width), random(height), 255))

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
    updatePixels()

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
    for r in rectangles:
        r.update()
        r.draw()
   
    for s in stars:
        s.draw()

    """
    * PART VI: Adding extras
    *
    * If you want to make your retro sun look more unique, try adding
    * reflections and stars.
    """
    ref.draw()
    


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
            
            
class Star:
    def __init__(self, x, y, col):
        self.x = x
        self.y = y
        self.star_color = col
        self.diameter = random(0.1, 3)
        self.start_alpha = random(1, 200)
        self.alpha = self.start_alpha

    def setAlpha(self, new_alpha):
        self.alpha = constrain(new_alpha, self.start_alpha, 255)

    def draw(self):
        noStroke()
        fill(self.star_color, self.alpha)
        blink = random(0, 0.8)
        ellipse(self.x, self.y, self.diameter + blink, self.diameter + blink)


class Reflection:
    # RGB colors
    bar_colors = [
        color(45, 2, 59),   
        color(109, 0, 88),  
        color(154, 51, 86), 
        color(158, 79, 62), 
        color(154, 51, 86), 
        color(109, 0, 88),  
        color(45, 2, 59)    
    ]

    def __init__(self, sun_radius, num_bars, top_x, top_y, speed):
        self.sun_radius = sun_radius;
        self.top_x = top_x;
        self.top_y = top_y;
        self.speed = speed;
        self.num_bars = num_bars
    
        self.top_width = 2 * (self.sun_radius + self.sun_radius/3)
        self.max_height = 10
        self.bottom_y = self.top_y + (self.num_bars * 2 * self.max_height)
        self.bars = list()
    
        self.initialize()

    def initialize(self):
        # Setup bottom relection bars
        x = self.top_x
        y = self.top_y
        w = self.top_width
        h = self.max_height
        
        for i in range(self.num_bars):   
            y += (self.bottom_y - self.top_y) / self.num_bars;
            x += self.sun_radius / 16;
            w -= 2 * (self.sun_radius / 16);

            r = Rectangle(x, y, w, h);
            self.bars.append(r);
  
    def draw(self):
        strokeWeight(1)
    
        for bar in self.bars:
            for i in range(bar.w):
                alpha_max = -255 - (bar.y - self.top_y)
                alpha_min =  255 + (bar.y - self.top_y)
                alpha = map(bar.x + i, bar.x, bar.x + bar.w, alpha_min, alpha_max)
                step = map(bar.x + i, bar.x, bar.x + bar.w, 0, 1)
                lc = interpolate_color(Reflection.bar_colors, step)
    
                stroke(lc, 255 - abs(alpha))
                line(i, bar.y, bar.x + i, bar.y + bar.h)

            bar.y += self.speed
            bar.x += self.speed
            bar.w -= 2 * self.speed

            if bar.y > self.bottom_y:
                # Bar at bottom, reset to top
        
                bar.x = self.top_x;
                bar.y = self.top_y + self.max_height;
                bar.w = self.top_width;
                bar.h = 1;
            elif bar.y > self.bottom_y - self.max_height:
               # Bar near bottom
        
                bar.h -= self.speed
            elif bar.h < self.max_height:
                # Bar height just reset and at top
        
                bar.y -= self.speed;
                bar.h += self.speed;
