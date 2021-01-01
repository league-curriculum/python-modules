import math
# When you are done, this program will draw an ellipse 
# that jumps to new location each time you click on it.
 
# 1. Create three integer variables to represent the x, y, and the size of the ellipse
x = 500
y = 500
sz = 100
              
def setup():
    # 2. Set the size of your sketch
    
    pass
     
def draw():
    # 3. Set the background color of your sketch

    # 4. Draw an ellipse using the variables created at the top of the sketch for the
    #    location and size of your ellipse.  Make sure it fits in the window.
    #    Change the variables if it does not.

    
    pass

#******** This method gets called automatically when you press the mouse ************/
def mousePressed():
    # 5. Change these variables to the names of the x and y variables you made
    
    # 6. Create an integer variable called distance
    
    # 7. The get_distance_from_mouse() function below returns a number.
    #    Set the value of your distance variable to the value returned by the
    #    get_distance_from_mouse function. You will need to pass the x and y location 
    #    of your ellipse to this method.
    distance = get_distance_from_mouse(x,y)
          

    # 8.  Use an if statement to check if your distance variable is < the radius of the ellipse
    #     If it is, make a new x AND y for the ellipse, for a new random location on the window
    #     Hint: Use code like this, x = random(width)
    if distance < sz/2:
        x = random(0,width)
        y = random(0,height)

    
    #********  This function gives you the number of pixels between the mouse and the x,y point ***********/
def get_distance_from_mouse(x, y):
    return math.sqrt(math.pow((mouseX-x),2) + math.pow((mouseY-y),2))
    
