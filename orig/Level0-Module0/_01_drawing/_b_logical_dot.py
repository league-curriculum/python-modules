import random
import turtle as turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

def screenClicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    myTurtle.penup()
    
    # 4. Move the turtle to a new location using .goto(x, y)
    myTurtle.goto(x, y)  # ;

def turtleClicked(x, y):
    print('turtle clicked!')  # ;
    
    # Make a for loop to run the next instructions 3 times
    for i in range(3):  # ;
        
        # Make the turtle spin using the .right() function
        myTurtle.right(360)  # ;
        
        # Use the .color() and getRandomColor() functions to change the color of the turtle
        myTurtle.color(getRandomColor())  # ;


window = turtle.Screen()  # ;
window.setup(width=0.75, height=0.8, startx=0, starty=0)  # ;

# Make a new turtle
myTurtle = turtle.Turtle()  # ;

# Make your turtle's shape 'turtle', .shape('turtle')
myTurtle.shape('turtle')  # ;

# Set your turtle's color using .color('green') and .pencolor('blue')
myTurtle.color('green')  # ;
myTurtle.pencolor('blue')  # ;

# Set and new width, length, and outline of our turtle
myTurtle.turtlesize(stretch_wid=10, stretch_len=10, outline=4)  # ;

# ===================== DO NOT EDIT THE CODE BELOW ============================
window.onclick(screenClicked)
myTurtle.onclick(turtleClicked)
turtle.done()
