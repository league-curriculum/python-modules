import math
# When you are done, this program will draw an ellipse 
# that jumps to new location each time you click on it.
 
# 1. Create three variables to represent the x, y, and
# size of the ellipse
              
def setup():
    # 2. Set the size of your sketch using the size function
    # size(width, height)
    
    pass
     
def draw():
    # 3. Set the background color of your sketch

    # 4. Draw an ellipse using the variables created at the top
    # of the sketch for the location and size of your ellipse. 
    # Make sure it fits in the window. Change the variables
    # if it does not.
    
    pass

# This method gets called automatically when you press the mouse
def mousePressed():
    # 5. Change these variables to the names of the x and y
    # variables you made in step 1
    global x
    global y
    
    # 6. The get_distance_from_mouse() function below returns a number.
    # Set the value of your distance variable to the value returned
    # by the get_distance_from_mouse function. You will need to pass the
    # x and y location of your ellipse to this method.
          

    # 7. Use an if statement to check if your distance variable is
    # less than the radius of the ellipse. If it is, set new values for
    # x AND y for the ellipse, for a new random location on the window
    # Hint: Use code like this, x = random(width)

    
# ========  This function gives you the number of pixels between =========
#                    between the mouse and the x,y point 
def get_distance_from_mouse(x, y):
    return math.sqrt(math.pow((mouseX-x),2) + math.pow((mouseY-y),2))
    
