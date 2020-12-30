import math
# When you are done, this program will draw an ellipse 
# that jumps to new location each time you click on it.
 
# 1. Create three integer variables to represent the x, y, and the size of the ellipse

              
def setup():
    # 2. Set the size of your sketch
    
     
def draw():
    # change these variables to the names of your variables defined above
    global x
    global y
    global sz
    # 3. Set the background color of your sketch
   
    # 4. Draw an ellipse using the variables created at the top of the sketch for the location and size of your ellipse. 
    # Make sure it fits in the window. Change the variables if it does not.
    
    
    #******** This method gets called automatically when you press the mouse ************/
def mousePressed():
    # change these variables to the names of the x and y variables you made
    global x;
    global y;
    # 5. Create an integer variable called distance
    
    # 6. The getDistanceFromMouse() method below returns a number.
    # Set the value of your distance variable to the value returned by the getDistance method
    # You will need to pass the x and y location of your ellipse to this method.
      
          

    # 7.  Use an if statement to check if your distance variable is < the radius of the ellipse
    # If it is, make a new x AND y for the ellipse, for a new random location on the window
    # Hint: Use code like this      x = random(width)
    

    
    #********  This method gives you the number of pixels between the mouse and the x,y point ***********/
def getDistanceFromMouse(x, y):
    return math.sqrt(math.pow((mouseX-x),2) + math.pow((mouseY-y),2))
    
